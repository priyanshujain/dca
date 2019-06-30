"""
Global utils for DCA 
"""


# Django imports.
from django.conf import settings


def default(var_name, value):
    if hasattr(settings, var_name):
        return getattr(settings, var_name)
    return value