"""
DCA serializer template.
It's used to generate a serializer for a model
"""


# App imports.
from dca.utils import default


DCA_SERIALIZER_TEMPLATE = default('DCA_SERIALIZER_TEMPLATE', '''
"""
%(app)s serializers
"""


# DRF imports.
from rest_framework.serializers import ModelSerializer
from %(app)s.models import %(model_name)s  # NOQA


def %(model_name)sSerializer(ModelSerializer):
    
    class Meta:
        model = %(model_name)s
''')
