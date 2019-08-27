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

# Create your views here.

from certificationAPI.connection import *
def postgresconnection(db):
	engine = getPoolEngine()
	Session = sqlalchemy.orm.sessionmaker(bind=engine)
	session = Session()
	return session

@api_view(['GET', 'POST'])
#@permission_classes((AllowAny,))
def getUsers(request):
	return Response({"data":"hello"})