from pathlib import Path





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8z-p$kcq3*tr*3^f_^1tx_o9i3*j+v*+u!=1=&+yk=riqp_m_-'

DEBUG = True

ALLOWED_HOSTS = [ '*',]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'PROJECT.web',
    'PROJECT.accounts',

    'phone_field',
    'phonenumber_field',
    'crispy_forms',
    'PROJECT.accounts.tests',

]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PROJECT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PROJECT.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project-db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'ec2-63-32-248-14.eu-west-1.compute.amazonaws.com',
#         'NAME': 'd3uoqmn1eghlf8',
#         'USER': 'uqbmizuxnfdktg',
#         'PASSWORD': '5e6637da3d3ffc77252c950c30723bdc61133def7b4bd85929864f84241f1363',
#         'HOST': 'ec2-63-32-248-14.eu-west-1.compute.amazonaws.com',
#         'PORT': '5432',
#     }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DJANGO_SETTINGS_MODULE = 'PROJECT.settings'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_ROOT = BASE_DIR / 'staticfile'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# CRISPY_TEMPLATE_PACK = 'uni_form'
CRISPY_TEMPLATE_PACK = 'bootstrap'
AUTH_USER_MODEL = 'accounts.ProjectUser'

LOGOUT_REDIRECT_URL = "/"

MEDIA_ROOT = BASE_DIR / 'mediafiles'
MEDIA_URL = 'media/'

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

