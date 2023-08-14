import os
from decouple import config, Csv
from dj_database_url import parse as dburl
#from .configs import DEFAULT_DATABASE_URL, DEFAULT_FROM_EMAIL, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS
from pathlib import Path
#import django_heroku


APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(APP_ROOT))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p@a=a!_uwa(c3bk(^xon9+9u57tv8_wbrx%a@%1ziu4pla5hkl'

DEFAULT_FROM_EMAIL = ''
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

# if not DEFAULT_DATABASE_URL:
#     DEFAULT_DATABASE_URL = 'sqlite:///' + os.path.join(APP_ROOT, 'db.sqlite3')

# DATABASES = {
#     'default': config('DATABASE_URL', default=DEFAULT_DATABASE_URL, cast=dburl),
# }
# #
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'norli_timesheet_feedback',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

LEGADO = {}
# LEGADO['SISTEMA'] = 'q_LEGADO'
# LEGADO['DATABASE_ENGINE'] = 'sqlserver_ado'
LEGADO['DATABASE_NAME'] = 'nGestao'
LEGADO['DATABASE_USER'] = 'sa'
LEGADO['DATABASE_PASSWORD'] = 'J9j7A%caojuly1'
LEGADO['DATABASE_HOST'] = 'localhost:1433'

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cpf_field',
    'django_cpf_cnpj',

    # djangosige apps:
    'djangosige.apps.base',
    'djangosige.apps.login',
    'djangosige.apps.cadastro',
    'djangosige.apps.vendas',
    'djangosige.apps.compras',
    'djangosige.apps.fiscal',
    'djangosige.apps.financeiro',
    'djangosige.apps.estoque',

    #zeppelin
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

    # Janela unica
    'djangosige.apps.janela_unica',
    'django_fsm',
    'django_fsm_log',
    'fsm_admin',
    'simple_history',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Middleware para paginas que exigem login
    'djangosige.middleware.LoginRequiredMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'simple_history.middleware.HistoryRequestMiddleware',
]

SIMPLE_HISTORY_REVERT_DISABLED=True

ROOT_URLCONF = 'djangosige.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'pt-br'

#TIME_ZONE = 'UTC'
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

#teste
#django_heroku.settings(locals())