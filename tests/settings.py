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