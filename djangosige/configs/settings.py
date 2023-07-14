from mglib.utils import try_load_config
import os
from decouple import config, Csv
from dj_database_url import parse as dburl
# from .configs import DEFAULT_DATABASE_URL, DEFAULT_FROM_EMAIL, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS
from pathlib import Path
# import django_heroku
from configula import Configula

APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(APP_ROOT))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p@a=a!_uwa(c3bk(^xon9+9u57tv8_wbrx%a@%1ziu4pla5hkl'

DEFAULT_FROM_EMAIL = ''
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

# if not DEFAULT_DATABASE_URL:
#     DEFAULT_DATABASE_URL = 'sqlite:///' + os.path.join(APP_ROOT, 'db.sqlite3')

# DATABASES = {
#     'default': config('DATABASE_URL', default=DEFAULT_DATABASE_URL, cast=dburl),
# }
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'norli_timesheet',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

LEGADO = {}
# LEGADO['SISTEMA'] = 'q_LEGADO'
# LEGADO['DATABASE_ENGINE'] = 'sqlserver_ado'
LEGADO['DATABASE_NAME'] = 'nGestao'
LEGADO['DATABASE_USER'] = 'sa'
LEGADO['DATABASE_PASSWORD'] = 'J9j7A%caojuly1'
LEGADO['DATABASE_HOST'] = 'localhost:1433'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'knox',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cpf_field',
    'django_cpf_cnpj',
    'django.contrib.sites',

    # djangosige apps:
    'djangosige.apps.base',
    'djangosige.apps.login',
    'djangosige.apps.cadastro',
    'djangosige.apps.vendas',
    'djangosige.apps.compras',
    'djangosige.apps.fiscal',
    'djangosige.apps.financeiro',
    'djangosige.apps.estoque',

    # zeppelin
    'djangosige.apps.exemplo',
    'djangosige.apps.zeppelin',
    'djangosige.apps.zpfaturamento',

    # Tattico
    'djangosige.apps.taticca_cv',

    # norli
    'djangosige.apps.norli_projeto',
    'djangosige.apps.timesheet',

    'djangosige.apps.viagem',

    # Utilitarios e Importacao
    'djangosige.apps.util',
    'djangosige.apps.janela_unica',

    # papermerge
    'papermerge.core',
    'papermerge.contrib.admin',
    'allauth',
    'allauth.account',
    'dynamic_preferences',
    'polymorphic_tree',
    'polymorphic',
    'mptt',
    'mgclipboard'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mgclipboard.middleware.ClipboardMiddleware',
    # Middleware para paginas que exigem login
    'djangosige.middleware.LoginRequiredMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'djangosige.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # contexto para a versao do sige
                'djangosige.apps.base.context_version.sige_version',
                # contexto para a foto de perfil do usuario
                'djangosige.apps.login.context_user.foto_usuario',
                'dynamic_preferences.processors.global_preferences',
                'papermerge.contrib.admin.context_processors.extras',
                'papermerge.contrib.admin.context_processors.user_perms',
                'papermerge.contrib.admin.context_processors.user_menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangosige.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(APP_ROOT, 'static'),
]

FIXTURE_DIRS = [
    os.path.join(APP_ROOT, 'fixtures'),
]

MEDIA_ROOT = os.path.join(APP_ROOT, 'media/')
MEDIA_URL = 'media/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

LOGIN_NOT_REQUIRED = (
    r'^/login/$',
    r'/login/esqueceu/',
    r'/login/trocarsenha/',
    r'/logout/',
)

#################


WSGI_APPLICATION = 'djangosige.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

#
# django_heroku.settings(locals())


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# teste
# django_heroku.settings(locals())
PDFTOPPM_STEP = 100
PDFTOPPM_MIN_HEIGHT = 100
PDFTOPPM_DEFAULT_HEIGHT = 900
PDFTOPPM_MAX_HEIGHT = 1500
PDFTOPPM_JPEG_QUALITY = 90
MAX_STORAGE_SIZE = 1 * 1024 * 1024

UPLOAD_FILE_SIZE_MAX = 12 * 1024 * 1024
UPLOAD_FILE_SIZE_MIN = 1
UPLOAD_ALLOWED_MIMETYPES = ['application/pdf']

FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler'
]

PAPERMERGE_TASK_QUEUE_DIR = os.path.join(BASE_DIR, "queue")

# even if other than filesystem message brokers will be used
# TASK_QUEUE_DIR queue dir will be created. This is because, at this point
# django cannot tell if CELERY_BROKER_URL will stay filesystem:// or it
# will change later (e.g. in production.py which inherits from base.py)
if not os.path.exists(PAPERMERGE_TASK_QUEUE_DIR):
    os.makedirs(
        PAPERMERGE_TASK_QUEUE_DIR, exist_ok=True
    )

# For each user create a specil folder called Inbox
# Useful only in dev/production (must be False in testing environment)
PAPERMERGE_CREATE_INBOX = True

CELERY_BROKER_URL = "filesystem://"
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'data_folder_in': PAPERMERGE_TASK_QUEUE_DIR,
    'data_folder_out': PAPERMERGE_TASK_QUEUE_DIR,
}

CELERY_WORKER_HIJACK_ROOT_LOGGER = False
CELERY_WORKER_CONCURENCY = 1
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_CREATE_MISSING_QUEUES = True
CELERY_TASK_DEFAULT_EXCHANGE = 'papermerge'
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'papermerge'

CELERY_INCLUDE = 'papermerge.core.tasks'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_TASK_RESULT_EXPIRES = 86400

AUTHENTICATION_BACKENDS = (
    'papermerge.core.auth.NodeAuthBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

REST_KNOX = {
    'AUTH_TOKEN_CHARACTER_LENGTH': 32,
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
}

PAPERMERGE_DEFAULT_FILE_STORAGE = "mglib.storage.FileSystemStorage"
BINARY_FILE = "/usr/bin/file"
BINARY_CONVERT = "/usr/bin/convert"
BINARY_PDFTOPPM = "/usr/bin/pdftoppm"
BINARY_PDFINFO = "/usr/bin/pdfinfo"
BINARY_IDENTIFY = "/usr/bin/identify"
BINARY_OCR = "/usr/bin/tesseract"
BINARY_PDFTK = "/usr/bin/pdftk"
PAPERMERGE_OCR_LANGUAGES = {"pt": "Português", "eng": "English", }
PAPERMERGE_OCR_DEFAULT_LANGUAGE = "pt"
PAPERMERGE_IMPORT_MAIL_HOST = ""
PAPERMERGE_IMPORT_MAIL_USER = ""
PAPERMERGE_IMPORT_MAIL_PASS = ""
PAPERMERGE_IMPORT_MAIL_INBOX = "INBOX"
PAPERMERGE_IMPORT_MAIL_SECRET = ""
DEFAULT_CONFIG_PLACES = [
    "/etc/papermerge.conf.py",
    "papermerge.conf.py"
]
DEFAULT_PAPERMERGE_CONFIG_ENV_NAME = "PAPERMERGE_CONFIG"
cfg_papermerge = try_load_config(
    config_locations=DEFAULT_CONFIG_PLACES,
    config_env_var_name=DEFAULT_PAPERMERGE_CONFIG_ENV_NAME
)

# do not remove this assignment. It is used in core checks to
# figure out if papermerge configuration file was successfully load.
CFG_PAPERMERGE = cfg_papermerge
# AUTH_USER_MODEL = 'core.User'
AUTH_USER_MODEL = 'auth.User'

PAPERMERGE_METADATA_DATE_FORMATS = [
    'dd.mm.yy',
    'dd.mm.yyyy',
    'dd.M.yyyy',
    'month'  # Month as locale’s full name, January, February
]

PAPERMERGE_METADATA_CURRENCY_FORMATS = [
    'dd.cc',
    'dd,cc'
]

PAPERMERGE_METADATA_NUMERIC_FORMATS = [
    'dddd',
    'd,ddd',
    'd.ddd'
]

PAPERMERGE_MIMETYPES = [
    'application/octet-stream',
    'application/pdf',
    'image/png',
    'image/jpeg',
    'image/jpg',
    'image/tiff'
]
cfg_papermerge = Configula(
    prefix="PAPERMERGE",
    config_locations=[
        "/etc/papermerge.conf.py",
        "papermerge.conf.py"
    ],
    config_env_var_name="PAPERMERGE_CONFIG"
)

# do not remove this assignment. It is used in core checks to
# figure out if papermerge configuration file was successfully load.
CFG_PAPERMERGE = cfg_papermerge