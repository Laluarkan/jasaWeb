"""
Django settings for webagency_project project.
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# Ambil SECRET_KEY dari .env. 
# Gunakan fallback (kunci default) HANYA untuk development lokal
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-!y0(q6$e-#9cvs7agtr!964=20j(^xu#&hm(5(10h@-$so*i-u')


# === PENGATURAN PRODUKSI vs LOKAL (Logika Baru) ===

# Deteksi mode Produksi jika DATABASE_URL ada di environment
IS_PRODUCTION = os.environ.get('DATABASE_URL')

if IS_PRODUCTION:
    # --- PENGATURAN PRODUKSI ---
    # (Saat di-deploy di hosting)
    print("Running in PRODUCTION mode")
    DEBUG = False
    ALLOWED_HOSTS = ['webkan-wmnm.onrender.com'] # Domain Render Anda
    
    # Konfigurasi Database PostgreSQL dari DATABASE_URL
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL')
        )
    }

else:
    # --- PENGATURAN LOKAL (DEVELOPMENT) ---
    # (Saat di laptop Anda: 'python manage.py runserver')
    print("Running in DEVELOPMENT mode (using SQLite)")
    DEBUG = True
    ALLOWED_HOSTS = [] # Kosongkan untuk 127.0.0.1
    
    # Konfigurasi Database SQLite lokal
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
# === AKHIR BLOK PENGATURAN ===


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Whitenoise butuh ini di atas
    'core.apps.CoreConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'portfolio.apps.PortfolioConfig',
    'contract.apps.ContractConfig',
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'cloudinary',
    'cloudinary_storage',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'webagency_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webagency_project.wsgi.application'


# Password validation
# ... (Blok AUTH_PASSWORD_VALIDATORS Anda di sini) ...
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ==================================================================
# === PENGATURAN STATIC (CSS/JS) & MEDIA (UPLOAD GAMBAR) ===
# ==================================================================

# --- Pengaturan Static (CSS/JS) ---
# URL untuk file statis
STATIC_URL = '/static/'
# Folder sumber file statis Anda di lokal
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]
# Folder tujuan 'collectstatic' (tempat Whitenoise mengambil file)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

if IS_PRODUCTION:
    # --- PRODUKSI (Cloudinary & Whitenoise) ---
    
    # Penyimpanan file STATIS (CSS/JS)
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    # Penyimpanan file MEDIA (Upload)
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    # Konfigurasi Cloudinary (Metode Manual yang Aman)
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    }
    
    # (MEDIA_URL dan MEDIA_ROOT tidak diperlukan di produksi,
    # karena Cloudinary menanganinya)

else:
    # --- LOKAL (Development) ---
    
    # Penyimpanan file STATIS (CSS/JS)
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    
    # Penyimpanan file MEDIA (Upload)
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==================================================================


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Pengaturan Allauth ---
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
LOGIN_REDIRECT_URL = '/' 
LOGOUT_REDIRECT_URL = '/' 

# --- Pengaturan Email & Notifikasi ---
if IS_PRODUCTION:
    # Di Render, gunakan 'Console Backend' untuk mencegah timeout/crash.
    # Ini akan MENCETAK email ke LOG Render, bukan mengirimkannya.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Di lokal, gunakan SMTP untuk pengiriman nyata (pengujian)
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 465 
    EMAIL_USE_SSL = True
    EMAIL_USE_TLS = False

# Kredensial dibaca dari .env (digunakan oleh lokal atau Telegram)
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')