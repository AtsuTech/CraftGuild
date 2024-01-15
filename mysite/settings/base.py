"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


AUTH_USER_MODEL = 'users.User'
WAGTAIL_USER_EDIT_FORM = 'users.admin.CustomUserEditForm'
WAGTAIL_USER_CREATION_FORM = 'users.admin.CustomUserCreationForm'
WAGTAIL_USER_CUSTOM_FIELDS = ['user_id','user_type']


# Application definition

INSTALLED_APPS = [
    "accounts",#ログイン・ログアウト
    "all_pages_integration",#このアプリがが中心的なアプリで、各ページのviewやurlを管理
    "contact_form",#お問合せフォーム処理などのアプリ
    "contents",#コンテンツのモデル、テンプレート
    "creation_flow",#【教室】：作成の流れモデル
    "form",
    "mentor",#【特徴】：メンターのモデル
    "home",
    "learn",#【特徴】：身につくことのモデル
    "particular",#【特徴】：こだわりのモデル
    "price_plan",#料金プランのモデル
    "users",#ユーザーモデルをカスタマイズ
    "search",
    "trial_class_reservation",#体験授業予約のフォーム処理などのアプリ
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.modeladmin",#Djangonのプレーンなモデルを使用するために追加(app:trial_class_reservationで使用)
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "wagtailmarkdown",#markdoen
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]   

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "mysite"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'    # 追加
LOGOUT_REDIRECT_URL = '/'

# Markdownエディタ設定
WAGTAILMARKDOWN = {
    #"autodownload_fontawesome": False,
    "allowed_tags": [],  # optional. a list of HTML tags. e.g. ['div', 'p', 'a']
    "allowed_styles": [],  # optional. a list of styles
    "allowed_attributes": {},  # optional. a dict with HTML tag as key and a list of attributes as value
    "allowed_settings_mode": "extend",  # optional. Possible values: "extend" or "override". Defaults to "extend".
    "extensions": [],  # optional. a list of python-markdown supported extensions
    "extension_configs": {},  # optional. a dictionary with the extension name as key, and its configuration as value
    "extensions_settings_mode": "extend",  # optional. Possible values: "extend" or "override". Defaults to "extend".
    "extensions": ["toc", "sane_lists"],
}


# WAGTAILRICHTEXTEDITORS = {
#     'default': {
#         'WIDGET': 'wagtailmarkdown.widgets.AdminMarkdownTextarea',
#     },
#     'markdown': {
#         'WIDGET': 'wagtailmarkdown.widgets.AdminMarkdownTextarea',
#     },
# }

WAGTAIL_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.codehilite',
]

#-------------------------メール送信(SMTPを使用)の設定-------------------------
#本番の環境に合わせて内容を変更する
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # SMTPを使用する場合
MAIL_HOST='smtp.gmail.com'
MAIL_PORT=587
EMAIL_USE_TLS = True  # TLSを使用する場合
EMAIL_HOST_USER = 'your_username'
EMAIL_HOST_PASSWORD = 'lhadbpfxrdgxxhkc'
DEFAULT_FROM_EMAIL = 'atsushiabc1204@gmail.com'  # 送信元のメールアドレス
#-------------------------ここまでメール送信(SMTPを使用)の設定-------------------------

