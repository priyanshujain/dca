# DCA (Django CRUD Automation)

Automagically gerenrates Django CRUD Automation.

#### Install

```sh
pipenv shell
pipenv install
```



&nbsp;

#### Setup

1. Add `dca` to installed apps

Example
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # dca
    'dca',

    # Private Apps
    'sample.core',
]
```

2. Define models in  `<app-name>/models.py`

Example
```py
# Djnago imports.
from django.db.models import (Model, TextField, CharField)


class Post(Model):
    title = CharField(max_length=280)
    content = TextField()

```

3. Add dca config to settings

Example
```py
DCA_CHOICES = 'sample.core.choices'

# List of apps for which we want to generate APIs
DCA_APPS = [
    'sample.core'
]

DCA_DIR = f'{BASE_DIR}/sample'
```

#### Run

run this

```
python managr.py generate
```
and it will gernerate dbapi file `<app-name>/dbapi.py`

```py
# DO NOT EDIT THIS FILE MANUALLY
# THIS FILE IS AUTO-GENERATED
# MANUAL CHANGES WILL BE DISCARDED
# PLEASE READ DCA DOCS


from sample.core.models import Letter  # NOQA
DCA_IGNORE_FIELDS = ['created_on', 'updated_on', 'id']  # NOQA


def read_letter(*args, **kwargs):
    try:
        return Letter.objects.get(*args, **kwargs)
    except Letter.DoesNotExist:
        return None

def read_letters_filter(*args, **kwargs):
    return Letter.objects.filter(*args, **kwargs)


def create_letter(*args, **kwargs):
    for ignore_field in DCA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Letter.objects.create(*args, **kwargs)


def update_letter(id, *args, **kwargs):
    for ignore_field in DCA_IGNORE_FIELDS:
        if ignore_field in kwargs:
            del kwargs[ignore_field]
    for key in list(kwargs):
        if kwargs[key] in [None, 'None', '']:
            del kwargs[key]
    return Letter.objects.filter(id=id).update(*args, **kwargs)


def delete_letter(id):
    return Letter.objects.get(id=id).delete()
```


We're working on auto gererating serializers and view for crud operations for any model.

## like it?

:star: this repo

## Contributors

PRs are welcomed.


## license

MIT © [priyanshujain](https://github.com/priyanshujain)


## Credits

* Inspired from [garuda](https://github.com/dhilipsiva/garuda) by [dhilipsiva](https://github.com/dhilipsiva)
