import os

###############
# Build paths #
###############

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#####################
# Security settings #
#####################

SECRET_KEY = '<fake-secret-key>'

DEBUG = True

ALLOWED_HOSTS = ['*']

#################
# Core settings #
#################

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
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.google',
]

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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#######################
# Password validation #
#######################

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


########################
# Internationalization #
########################

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


################
# Static files #
################

STATIC_URL = '/static/'


##################
# Authentication #
##################

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',  # django-allauth を追加
)

################
# 1: 認証⽅式を 「メールアドレスとパスワード」 に変更しユーザー名は使⽤しない設定にします。
# 2: django-allauthに必要記述
# 3: ログイン、リダイレクトURLの設定
# 4: ログアウトリンクの設定
# 5: ユーザー登録時にメールアドレス確認。ユーザー登録画面でにEmailを必須項目
################

# 1
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

# 2
SITE_ID = 1

# 3
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

# 4
ACCOUNT_LOGOUT_ON_GET = True

# 5
ACCOUNT_EMAIL_VARIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True


##################
# Email settings #
##################

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'