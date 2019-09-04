
#postgre config
CERTIFICATE_POSTGRE_DATABASE = {
    'dialect' : 'postgresql',
	'driver' : 'psycopg2',
	'database': 'skill_refinery',
	'username': 'postgres',
	'password': 'shrey74739',
	'host': 'localhost',
	'port': '5432',
}

DEBUG = True

EMAIL = {
	'host': 'smtp.gmail.com',
	'port': 587,
	'useTLS': True,
	'hostUser': '',
	'hostPassword' : ''
}