from django.conf import settings


def default(var_name, value):
    if hasattr(settings, var_name):
        return getattr(settings, var_name)
    return value


GARUDA_DIR = default('GARUDA_DIR', 'garuda_dir')
GARUDA_PORT = default('GARUDA_PORT', '50051')
GARUDA_SUFFIX = default('GARUDA_SUFFIX', 'Garuda')
GARUDA_CUSTOM = default('GARUDA_CUSTOM', 'garuda_custom')
GARUDA_AUTO_PACKAGE = default('GARUDA_AUTO_PACKAGE', 'auto_garuda')

# Derived constants
GARUDA_AUTO_MODULE = f'{GARUDA_DIR}.{GARUDA_AUTO_PACKAGE}'
GARUDA_AUTO_FILE = f'{GARUDA_DIR}/{GARUDA_AUTO_PACKAGE}.py'

# Fields to ifnore while dictifying
GARUDA_IGNORE_FIELDS = default(
    'GARUDA_IGNORE_FIELDS', ['created_on', 'updated_on', 'id'])

# Fields to remove while generating model
GARUDA_REMOVE_FIELDS = default('GARUDA_REMOVE_FIELDS', [])


# `GARUDA_AST_MAP` basically says how to extract data
# from a given AST `Assign` object
GARUDA_AST_MAP = default('GARUDA_AST_MAP', dict(
    Num=lambda kw: kw.value.n,
    Str=lambda kw: kw.value.s,
    Name=lambda kw: kw.value.id,
    NameConstant=lambda kw: kw.value.value,
    Attribute=lambda kw: '%s.%s' % (kw.value.value.id, kw.value.attr),
))


GARUDA_CRUD_TEMPLATE = default('GARUDA_CRUD_TEMPLATE', '''
from %(app)s.models import %(model_name)s  # NOQA
GARUDA_IGNORE_FIELDS = %(ignore_fields)s  # NOQA


def read_%(model_name_lower)s(*args, **kwargs):
    try:
        return %(model_name)s.objects.get(*args, **kwargs)
    except %(model_name)s.DoesNotExist:
        return None

true
def read_%(model_name_lower_plural)s_filter(*args, **kwargs):
    return %(model_name)s.objects.filter(*args, **kwargs)


def create_%(model_name_lower)s(*args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return %(model_name)s.objects.create(*args, **kwargs)


def update_%(model_name_lower)s(id, *args, **kwargs):
    for ignore_field in GARUDA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return %(model_name)s.objects.filter(id=id).update(*args, **kwargs)


def delete_%(model_name_lower)s(id):
    return %(model_name)s.objects.get(id=id).delete()
''')