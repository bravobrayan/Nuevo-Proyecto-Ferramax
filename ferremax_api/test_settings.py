# test_settings.py
from .settings import *  # Hereda toda la configuración de settings.py

# Configuración específica para pruebas

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test_db.sqlite3',  # Nueva base de datos para pruebas
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',  # Hashing más rápido para pruebas
]

# Puedes agregar más configuraciones específicas para pruebas si es necesario, por ejemplo:
# - Cambiar el backend de email para no enviar correos reales
# - Deshabilitar middleware que no necesitas en pruebas
# - Configurar un caché más simple

# Configuración para pytest-django (opcional)
INSTALLED_APPS += [
    'pytest_django',
]
