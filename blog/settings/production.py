from Django.conf import settings
import os

DEBUG = False
TEMPLATE
DATABASES = settings.DATABASES
# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSLHEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# STATIC_URL = '/static/'
#
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )
