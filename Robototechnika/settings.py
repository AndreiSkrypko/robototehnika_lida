import os
from pathlib import Path

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Безопасность
SECRET_KEY = 'django-insecure-5t&d&=2*w-zc5*px-q%ierx@hu@(ufe!i_1*$@(at@4sjm$^^$'
DEBUG = True
ALLOWED_HOSTS = []

# Установленные приложения
INSTALLED_APPS = [
    'widget_tweaks',
    'main_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'forum_app',
    'login_app',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Robototechnika.urls'

# Шаблоны
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,  # Включаем отладку шаблонов
        },
    },
]

WSGI_APPLICATION = 'Robototechnika.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидация пароля
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Язык и время
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Minsk"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статика
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "main_app/static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Отключение кэширования в режиме разработки
if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    
    # Отключение кэширования статических файлов
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
