"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9^avbgo%bueu+ujz-p97+rwxwwe86#o5xmqbo1ak37b)_^^%91'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# django-allauth setting
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

#=======================Django allauth mail settings =============================--


#djangoallauthでメールでユーザー認証する際に必要になる認証バックエンド
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

#ログイン時の認証方法はemailとパスワードとする
ACCOUNT_AUTHENTICATION_METHOD   = "email"

#ログイン時にユーザー名(ユーザーID)は使用しない
ACCOUNT_USERNAME_REQUIRED       = "False"

#ユーザー登録時に入力したメールアドレスに、確認メールを送信する事を必須(mandatory)とする
ACCOUNT_EMAIL_VARIFICATION  = "mandatory"

#ユーザー登録画面でメールアドレス入力を要求する(True)
ACCOUNT_EMAIL_REQUIRED      = True


#ここにメール送信設定を入力する(Sendgridを使用する場合)
EMAIL_BACKEND   = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST      = 'smtp.sendgrid.net'
EMAIL_USE_TLS   = True
EMAIL_PORT      = 587


"""
Sendgrid APIキーを使用したメール送信

0、pip install django-sendgrid-v5 を実行してAPIで送信用のライブラリをインストール

1、.gitignoreにlocalsettings.pyを指定する。

2、localsettings.pyに下記を記述する

EMAIL_BACKEND       = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY    = "APIKEY"

3、import文で読み込み

4、SENDGRID_SANDBOX_MODE_IN_DEBUG = False でサンドボックス無効化

"""
from . import localsettings

EMAIL_BACKEND       = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY    = localsettings.SENDGRID_API_KEY


#DEBUGがTrueのとき、メールの内容は全て端末に表示させる。デプロイ後(DEBUG=False)で、メールを実際に送信したいときはSENDGRIDのサンドボックスモードを無効化する。
"""
if DEBUG:
    EMAIL_BACKEND   = "django.core.mail.backends.console.EmailBackend"
else:
    SENDGRID_SANDBOX_MODE_IN_DEBUG = False
"""
SENDGRID_SANDBOX_MODE_IN_DEBUG = False


#CHECK:メール認証時のメールの本文等の編集は templates/allauth/account/email/ から行うことができる


#=======================Django allauth mail settings =============================--



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'users.apps.UsersConfig',

    'mysite.apps.MysiteConfig'
]

#↓カスタムユーザーモデルを適用する。対象はuserアプリのCustomUserクラス
AUTH_USER_MODEL = 'users.CustomUser'
#↓アカウントフォームの指定。userアプリのforms.pyのSignupFormクラス
ACCOUNT_FORMS   = { "signup":"users.forms.SignupForm"}





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"), os.path.join(BASE_DIR, "templates", "allauth")],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
