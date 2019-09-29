from django.db import models
from django.contrib.auth.models import AbstractUser
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from sqlalchemy import types

Base = declarative_base()

class CourseCategory(Base):
	__tablename__ = 'course_category'
	category_id = Column(Integer, primary_key=True, server_default=text("nextval('course_category_category_id_seq'::regclass)"))
	category_name = Column(String)
	category_description = Column(String)
	created_by = Column(Integer)
	created_date = Column(DateTime)
	disable_flag = Column(Boolean)
	
class Courses(Base):
	__tablename__ = 'courses'
	course_id = Column(Integer, primary_key=True, server_default=text("nextval('courses_course_id_seq'::regclass)"))
	course_name = Column(String)
	course_details = Column(String)
	course_pic = Column(String)
	created_by = Column(Integer)
	created_date = Column(DateTime)
	updated_date = Column(DateTime)
	disable_flag = Column(Boolean)
	course_category = Column(Integer)