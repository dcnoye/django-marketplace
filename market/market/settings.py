"""
Django settings for market project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/

For deployment see https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
"""

from decouple import config
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# Site ID for allauth
SITE_ID = 1

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['ssd-farmers-live-klingj3.c9users.io',
                 'localhost',
                 '127.0.0.1',
                 '[::1]']


# APP CONFIGURATION
# ---
DJANGO_APPS = [
    # For authorization and registration
    'django.contrib.auth',
    'django.contrib.sites',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admin',
]

INSTALLED_APPS = [
    'crispy_forms',
    'django_extensions',
]

LOCAL_APPS = [
    'market',
    'market.apps.board',
    'market.apps.core',
    'market.apps.social',
]

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + INSTALLED_APPS + LOCAL_APPS


# MIDDLEWARE CONFIGURATION
# ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# DEBUG
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# FIXTURE CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-FIXTURE_DIRS
#FIXTURE_DIRS = (
#    os.path.join(BASE_DIR, 'fixtures'),
#)


# DATABASE CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# GENERAL CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#use-i18n
USE_I18N = False

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#use-tz
USE_TZ = True


# TEMPLATE CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/1.11/ref/settings/#template-debug
            'debug': config('DEBUG', cast=bool),
            # See: https://docs.djangoproject.com/en/1.11/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/1.11/ref/templates/api/#loader-types
            #'loaders': [
            #    'django.template.loaders.filesystem.Loader',
            #    'django.template.loaders.app_directories.Loader',
            #],
            # See: https://docs.djangoproject.com/en/1.11/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# DJANGO-TAGULOUS CONFIGURATION
# ---
INSTALLED_APPS += ['tagulous']
# TODO: use django-compressor to optimize these,
# TAGULOUS_AUTOCOMPLETE_JS = (
#     'tagulous/lib/jquery.js',
#     'tagulous/lib/select2-3/select2.min.js',
#     'tagulous/tagulous.js',
#     'tagulous/adaptor/select2.js',
# )

# TODO: load CSS with support for Bootstrap 4
# TAGULOUS_AUTOCOMPLETE_CSS = {
#     'all': ['tagulous/lib/select2-3/select2.css']
# }


# DJANGO-PRICES CONFIGURATION
# ---
INSTALLED_APPS += ['django_prices']


# STATIC FILE CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'cache')

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
# STATICFILES_DIRS = []

# See: https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA CONFIGURATION
# ---
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#media-url
MEDIA_URL = '/media/'


# URL CONFIGURATION
# ---
ROOT_URLCONF = 'market.urls'

# See: https://docs.djangoproject.com/en/1.11/ref/settings/#wsgi-application
WSGI_APPLICATION = 'market.wsgi.application'


# AUTHENTICATION CONFIGURATION
# ---
AUTHENTICATION_BACKENDS = [
    # allauth authentication
    'allauth.account.auth_backends.AuthenticationBackend',
    # Still needed for Django Admin
    'django.contrib.auth.backends.ModelBackend',
]

# Some really nice defaults
#ACCOUNT_AUTHENTICATION_METHOD = 'username'
#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

#ACCOUNT_ALLOW_REGISTRATION = True
#ACCOUNT_ADAPTER = 'market.users.adapters.AccountAdapter'
#SOCIALACCOUNT_ADAPTER = 'market.users.adapters.SocialAccountAdapter'

# Logged in users redirected here if they view login/signup pages
LOGIN_REDIRECT_URL = 'board:list'


# DJANGO-ALLAUTH CONFIGURATION
# ---
INSTALLED_APPS += ['allauth',
                   'allauth.account',
                   'allauth.socialaccount'
                   # 'allauth.socialaccount.providers.google'
                   ]
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_FORMS = {
    'login': 'market.apps.core.forms.MarketLoginForm',
    'signup': 'market.apps.core.forms.MarketSignupForm',
}
# We use a custom signup form but this is an integrated way to customize the behavior afterward
ACCOUNT_SIGNUP_FORM_CLASS = 'market.apps.social.forms.UserProfileForm'
# Don't display the logout confirmation
ACCOUNT_LOGOUT_ON_GET = True
# User display value is name from the associated profile
ACCOUNT_USER_DISPLAY = lambda user: user.profile.name

# PASSWORD STORAGE SETTINGS
# ---
# See https://docs.djangoproject.com/en/1.11/topics/auth/passwords/#using-argon2-with-django
#PASSWORD_HASHERS = [
#    'django.contrib.auth.hashers.Argon2PasswordHasher',
#    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
#    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
#    'django.contrib.auth.hashers.BCryptPasswordHasher',
#]


# PASSWORD VALIDATION
# ---
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 7,
        },
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# EMAIL CONFIGURATION
# ---
# For development, send all emails to the console instead of sending them
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


########## CELERY
#INSTALLED_APPS += ['market.taskapp.celery.CeleryConfig']
#CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='django://')
#if CELERY_BROKER_URL == 'django://':
#    CELERY_RESULT_BACKEND = 'redis://'
#else:
#    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
########## END CELERY


# DJANGO-COMPRESSOR CONFIGURATION
# ---
INSTALLED_APPS += ['compressor']
# Enable compress when not debug
COMPRESS_ENABLED = not DEBUG
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
STATICFILES_FINDERS += ['compressor.finders.CompressorFinder']


# DJANGO-LIBSASS CONFIGURATION
# ---
# See: https://github.com/torchbox/django-libsass
LIBSASS_SOURCE_COMMENTS = False
# Use compressed output style when not debug
if not DEBUG:
    LIBSASS_OUTPUT_STYLE = 'compressed'


# DJANGO-ADMIN CONFIGURATION
# Location of root django.contrib.admin URL
ADMIN_URL = r'^admin/'


# GEOPOSITION CONFIGURATION
# ---
INSTALLED_APPS += ['geoposition']
GEOPOSITION_GOOGLE_MAPS_API_KEY = config('GEOPOSITION_GOOGLE_MAPS_API_KEY')


