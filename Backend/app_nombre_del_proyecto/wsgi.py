"""
WSGI config for app_nombre_del_proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
import os
import json

from django.core.exceptions import ImproperlyConfigured
from django.core.wsgi import get_wsgi_application

with open("configuracion_global.json") as f:
    value = json.loads(f.read())


def get_value(value_title, values=value):
    try:
        return values[value_title]
    except:
        msg = f"The name of {value_title} doesn't exists"
        raise ImproperlyConfigured(msg)


if get_value("ENVIRONMENT") == "dev":
    print("wsgi dev")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'app_nombre_del_proyecto.settings.dev')


if get_value("ENVIRONMENT") == "local":
    print("wsgi local")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'app_nombre_del_proyecto.settings.local')


if get_value("ENVIRONMENT") == "produccion":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'app_nombre_del_proyecto.settings.produccion')


if get_value("ENVIRONMENT") == "qa":
    print("wsgi qa")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'app_nombre_del_proyecto.settings.qa')


application = get_wsgi_application()
