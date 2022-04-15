from urllib.parse import urlparse
# import dj_database_url

from application.settings import *

DEBUG = False

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

database_url = urlparse(os.environ['DATABASE_URL'])
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': database_url.path.strip('/'),
        'USER': database_url.username,
        'PASSWORD': database_url.password,
        'HOST': database_url.hostname,
        'PORT': database_url.port,
    }
}
