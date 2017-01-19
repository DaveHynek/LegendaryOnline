from legendary.settings.base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# [START dbconfig]
DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'legendaryDB.sqlite3',
    }
}
# [END dbconfig]