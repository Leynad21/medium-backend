from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="FsSewD67k9nigteNn8B0l9DPKoL-vPalQJICa5eXDt8YHtk7i0U",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CRSF_TRUSTED_ORIGINS = ["http://localhost:8080"]

