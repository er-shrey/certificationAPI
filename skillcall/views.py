from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from skillcall.models import *
from skillcall.serializers import *
from sqlalchemy.orm import *
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import sqlalchemy, sqlalchemy.orm
from sqlalchemy.dialects.postgresql import array
from django.http import JsonResponse
import urllib
import urllib2
import json
from datetime import datetime
import collections
from sqlalchemy.pool import NullPool
from sqlalchemy.sql.functions import coalesce
from datetime import datetime, timedelta
from datetime import *
import time
from rom import util
import requests
import base64
import math
import tzlocal
import time
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from sqlalchemy.engine.url import URL
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.utils.crypto import get_random_string

# Create your views here.
from certificationAPI.emailDispatcher import *
from certificationAPI.connection import *
def postgresconnection():
	engine = getPoolEngine()
	Session = sqlalchemy.orm.sessionmaker(bind=engine)
	session = Session()
	return session

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def signup(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	session = postgresconnection()
	if(session.query(exists().where(AuthUser.username == username).where(AuthUser.is_active == True)).scalar()):
		response = {'status':'ERROR','message':'User Already Registered'}
	else:
		userPass = make_password(password)
		tokenInLink = get_random_string(length=64,allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
		userRecord = AuthUser(username = username, password = userPass, email = username, is_active = False, is_staff = False, first_name = '', last_name = '', is_superuser = False, date_joined = datetime.now(), user_pass_reset_token = tokenInLink)
		session.add(userRecord)
		session.commit()
		sendSignupMail(username, tokenInLink)
		response = {'status':'SUCCESS','message':'User Successfully Registered'}
	session.close()
	return Response(response)

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def register(request):
	username = request.POST.get('username')
	tokenInLink = request.POST.get('token')
	session = postgresconnection()
	if(session.query(exists().where(AuthUser.username == username).where(AuthUser.is_active == False).where(AuthUser.user_pass_reset_token == tokenInLink)).scalar()):
		updated_values = {AuthUser.user_pass_reset_token : '', AuthUser.last_update_date : datetime.now(),AuthUser.is_active: True}
		session.query(AuthUser).filter(AuthUser.username == username).update(updated_values)
		session.commit()
		response = {'status':"SUCCESS"}
	else:
		response = {'status':"FAILED", 'message':'User Already Verified'}
	session.close()
	return Response(response)

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def forgotPassword(request):
	email = request.GET.get('email')
	session = postgresconnection()
	if(session.query(exists().where(AuthUser.email == email).where(AuthUser.is_active == True)).scalar()):
		tokenInLink = get_random_string(length=64,allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
		updated_values = {AuthUser.user_pass_reset_token : tokenInLink, AuthUser.last_update_date : datetime.now()}
		session.query(AuthUser).filter(AuthUser.email == email).update(updated_values)
		session.commit()
		sendForgotPassMail(email, tokenInLink)
		response = {'status':"SUCCESS", 'message':'Password Recovery Link has been sent to your mail.'}
	else:
		response = {'status':"FAILED", 'message':'Contact Administrator to change Password'}
	session.close()
	return Response(response)

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def changePassword(request):
	username = request.GET.get('username')
	token = request.GET.get('token')
	password = request.GET.get('password')
	print "============================="
	print username
	print token
	print password
	print "============================="
	session = postgresconnection()
	if(session.query(exists().where(AuthUser.username == username).where(AuthUser.is_active == True).where(AuthUser.user_pass_reset_token == token)).scalar()):
		userPass = make_password(password)
		updated_values = {AuthUser.user_pass_reset_token : '', AuthUser.password: userPass, AuthUser.last_update_date : datetime.now()}
		session.query(AuthUser).filter(AuthUser.username == username).update(updated_values)
		session.commit()
		response = {'status':"SUCCESS", 'message':'success'}
	else:
		response = {'status':"FAILED", 'message':'Contact Administrator to change Password'}
	session.close()
	return Response(response)