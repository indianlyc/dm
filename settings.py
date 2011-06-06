#-*- coding: utf-8 -*-
# чтобы можно было в файле писать по-русский
# Django settings for dm project.

from os import path
PATH_PROJECT = path.dirname(__file__) + '/' # Получаем путь до текущего файла, считаем что файл settings
                                            # лежит в папке проекта, в нашем случае в dm.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('dm', 'dmitriy.shikhalev@gmail.com'),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Yekaterinburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PATH_PROJECT + 'media' # медиа файлы располагаются в папке dm/media

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/' # для загрузки медиа сайту нужно обратиться по этому url

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/' # url по которому нужно обращаться админке до своих
                                     # файлов, должен отличаться от MEDIA_URL

# Make this unique, and don't share it with anybody.
SECRET_KEY = '&&$m(ke!7!ju7ofm!ydlm=4675h)%pw378*4(9s&bf-p(p06sl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'dm.urls'


TEMPLATE_DIRS = (
    # общие для всех приложений шаблоны удобно располагать в папке dm/templates.
    PATH_PROJECT + 'templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # админку лучше подключать до собственных приложений.
    'django.contrib.admin',
    'polls',
    # Uncomment the next line to enable the admin:
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

try:
    from local_settings import *
except ImportError:
    pass
