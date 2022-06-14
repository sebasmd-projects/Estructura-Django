"""
ASGI config for app_nombre_del_proyecto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import json
from django.core.exceptions import ImproperlyConfigured
from django.core.asgi import get_asgi_application

with open("configuracion_global.json") as f:
    value = json.loads(f.read())


def get_value(value_title, values=value):
    try:
        return values[value_title]
    except:
        msg = f"The name of {value_title} doesn't exists"
        raise ImproperlyConfigured(msg)


if get_value("ENVIRONMENT") == "dev":
    print("asgi dev")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'app_nombre_del_proyecto.settings.dev')

if get_value("ENVIRONMENT") == "local":
    print("asgi local")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'app_nombre_del_proyecto.settings.local')

if get_value("ENVIRONMENT") == "produccion":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'app_nombre_del_proyecto.settings.produccion')

if get_value("ENVIRONMENT") == "qa":
    print("asgi qa")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'app_nombre_del_proyecto.settings.qa')

application = get_asgi_application()
