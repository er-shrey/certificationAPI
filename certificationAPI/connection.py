from django.conf import settings
from sqlalchemy.orm import *
from sqlalchemy import *
import sqlalchemy, sqlalchemy.orm
		
engine = 0
def getPoolEngine():
	try:
		return engine
	except:
		return ("Could not establish connection")
		
def postgresconnection_pool():
	global engine
	dialect = settings.CERTIFICATE_POSTGRE_DATABASE['dialect']
	driver = settings.CERTIFICATE_POSTGRE_DATABASE['driver']
	username = settings.CERTIFICATE_POSTGRE_DATABASE['username']
	password = settings.CERTIFICATE_POSTGRE_DATABASE['password']
	server = settings.CERTIFICATE_POSTGRE_DATABASE['host']
	port = settings.CERTIFICATE_POSTGRE_DATABASE['port']
	database = settings.CERTIFICATE_POSTGRE_DATABASE['database']
	url=dialect+'+'+driver+'://'+username+':'+password+'@'+server+':'+port+'/'+database
	try:
		engine = create_engine(url, pool_size=20, max_overflow=10, pool_recycle=1800) #, pool_pre_ping=True making overhead and pool_use_lifo=True is not behaving properly with postgres
	except:
		return ("Could not establish connection")