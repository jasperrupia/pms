from .base import *


DEBUG = False

ALLOWED_HOSTS = ['pharmacyinfo.pythonanywhere.com']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

