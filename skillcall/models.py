from django.db import models
from django.contrib.auth.models import AbstractUser
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from sqlalchemy import types

Base = declarative_base()	

class User(AbstractUser):
	email = models.CharField(max_length=254)
	first_name = models.CharField(max_length=254)
	last_name = models.CharField(max_length=254)
	class Meta:
		db_table = 'auth_user'
		
class AuthUser(Base):
	__tablename__ = 'auth_user'
	id = Column(Integer, primary_key=True, server_default=text("nextval('auth_user_id_seq'::regclass)"))
	password = Column(String(128), nullable=False)
	last_login = Column(DateTime(True))
	is_superuser = Column(Boolean, nullable=False)
	username = Column(String(150), nullable=False, unique=True)
	first_name = Column(String(30), nullable=False)
	last_name = Column(String(30), nullable=False)
	email = Column(String(254), nullable=False)
	is_staff = Column(Boolean, nullable=False)
	is_active = Column(Boolean, nullable=False)
	date_joined = Column(DateTime(True), nullable=False)