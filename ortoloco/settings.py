# Django settings for ortoloco project.
import os
import dj_database_url

DEBUG = os.environ.get("ORTOLOCO_DEBUG", True)

TEMPLATE_DEBUG = DEBUG

WHITELIST_EMAILS = ["mklarmann@gmail.com"]

ADMINS = (
    ('Manuel', 'mklarmann@gmail.com'),
)
SERVER_EMAIL="server@mehalsgmues.ch"


# let the users login with their emails
AUTHENTICATION_BACKENDS = (
    'my_ortoloco.helpers.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)

MANAGERS = ADMINS


DATABASES = {'default': dj_database_url.config(default='postgres://nhwoxfurjjuasx:Lz-PnvD3v_vWDM-ZtZmqOr0Kqr@ec2-54-83-58-191.compute-1.amazonaws.com:5432/dtmcgv4jhtaqd')}


EMAIL_HOST = os.environ.get('ORTOLOCO_EMAIL_HOST', 'v031278.kasserver.com')
EMAIL_HOST_USER = os.environ.get('ORTOLOCO_EMAIL_USER', 'm0358bfa')
EMAIL_HOST_PASSWORD = os.environ.get('ORTOLOCO_EMAIL_PASSWORD', 'MAG4321mag')
EMAIL_PORT = os.environ.get('ORTOLOCO_EMAIL_PORT', 587)
EMAIL_USE_TLS = os.environ.get('ORTOLOCO_EMAIL_TLS', True)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.mehalsgmues.ch']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de_CH'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/medias/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/medias/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/tosomeNotWorkingUrl/'

# Additional locations of static files
STATICFILES_DIRS = (
#"/static/",
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#tinyMCE
TINYMCE_JS_URL = '/static/js/tinymce/tinymce.min.js'

TINYMCE_DEFAULT_CONFIG = {
    'theme': "modern",
    'plugins': 'link',
    'relative_urls': False,
    'valid_styles': {
        '*': 'color,text-align,font-size,font-weight,font-style,text-decoration'
    },
    'menu': {
        'edit': {
            'title': 'Edit',
            'items': 'undo redo | cut copy paste | selectall'
        },
        'insert': {
            'title': 'Insert',
            'items': 'link'
        },
        'format': {
            'title': 'Format',
            'items': 'bold italic underline strikethrough superscript subscript | formats | removeformat'
        }
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd3w=vyfqpqmcj#&ge1d0$ch#ff7$qt#6z)lzqt=9pg8wg%d^%s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

IMPERSONATE_REDIRECT_URL = "/my/profil"

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'impersonate.middleware.ImpersonateMiddleware'
)

ROOT_URLCONF = 'ortoloco.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ortoloco.wsgi.application'

from photologue import PHOTOLOGUE_TEMPLATE_DIR

TEMPLATE_DIRS = (
    'ortoloco/templates',
    PHOTOLOGUE_TEMPLATE_DIR
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'my_ortoloco',
    'static_ortoloco',
    'photologue',
    'south',
    'django_cron',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'tinymce',
    'impersonate'
)

# logging config - copied from here: http://stackoverflow.com/questions/18920428/django-logging-on-heroku
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

GALLERY_SAMPLE_SIZE = 4
