from .base import *

import sys

ALLOWED_HOSTS = []
DEBUG = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mercedes_tools",
        "USER": "dev",
        "PASSWORD": get_secrets("DATABASE_PASS_LOCAL"),
    }
}
