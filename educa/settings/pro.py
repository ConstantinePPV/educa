from .base import *

DEBUG = False

ADMINS = (
    ('Constantine PV', 'constantine.ppv@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'educa',
       'USER': 'educa',
       'PASSWORD': 'django123',
   }
}
