"""
DCA dbapi template.
It's used to generate a dbapi for a model.
DBAPIs are functions used to communicate to django ORM.
"""


# App imports.
from dca.utils import default


DCA_CRUD_TEMPLATE = default('DCA_CRUD_TEMPLATE', '''
from %(app)s.models import %(model_name)s  # NOQA
DCA_IGNORE_FIELDS = %(ignore_fields)s  # NOQA


def read_%(model_name_lower)s(*args, **kwargs):
    try:
        return %(model_name)s.objects.get(*args, **kwargs)
    except %(model_name)s.DoesNotExist:
        return None

def read_%(model_name_lower_plural)s_filter(*args, **kwargs):
    return %(model_name)s.objects.filter(*args, **kwargs)


def create_%(model_name_lower)s(*args, **kwargs):
    for ignore_field in DCA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return %(model_name)s.objects.create(*args, **kwargs)


def update_%(model_name_lower)s(id, *args, **kwargs):
    for ignore_field in DCA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return %(model_name)s.objects.filter(id=id).update(*args, **kwargs)


def delete_%(model_name_lower)s(id):
    return %(model_name)s.objects.get(id=id).delete()
''')