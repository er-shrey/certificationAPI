from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from openAPIs.models import *
from openAPIs.serializers import *
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
def getCourses(request):
	session = postgresconnection()
	course_list = session.query(Courses.course_name, Courses.course_details, Courses.course_pic, CourseCategory.category_name).join(CourseCategory, and_(CourseCategory.category_id==Courses.course_category)).filter(and_(Courses.disable_flag==False)).limit(10).all()
	session.close()
	fewCourses = getFewCoursesSerializer(course_list,many=True)
	return Response(fewCourses.data)
	
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def getPlatformInfo(request):
	data = {
		"platformDetails":{"totalUsers":4,"totalCourses":2,"totalCertificates":8,"totalMentors":4},
		"mentorList":[{"name":"Shrey Kumar Jain","designation":"Programmer","mentorDetail":"3 Years of experience in Fullstack development, expertise includes Angular, JavaScript, NojeJs, Python and Postgres","profilePic":"person_1.jpg"},{"name":"Shrey Kumar Jain","designation":"Programmer","mentorDetail":"3 Years of experience in Fullstack development, expertise includes Angular, JavaScript, NojeJs, Python and Postgres","profilePic":"person_1.jpg"},{"name":"Shrey Kumar Jain","designation":"Programmer","mentorDetail":"3 Years of experience in Fullstack development, expertise includes Angular, JavaScript, NojeJs, Python and Postgres","profilePic":"person_1.jpg"}]
	}
	return Response(data)