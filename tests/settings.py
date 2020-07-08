DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'maat_test'
    }

}
ROOT_URLCONF = ''
SITE_ID = 1
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'djangomaat',
)

SECRET_KEY = 'sk'

MIDDLEWARE_CLASSES = ()

MAAT_FLUSH_BATCH_SIZE = 100 # To avoid sqlite issues

# This will prevent the tests from running the migrations that come with the app
# otherwise the test models won't be created.
# http://stackoverflow.com/questions/25161425/disable-migrations-when-running-unit-tests-in-django-1-7
MIGRATION_MODULES = {'djangomaat': None}
