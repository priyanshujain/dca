"""
Constants for DCA
"""


# App imports.
from dca.utils import default


DCA_DIR = default('DCA_DIR', 'dca_dir')
DCA_PORT = default('DCA_PORT', '50051')
DCA_SUFFIX = default('DCA_SUFFIX', 'dca')
DCA_CUSTOM = default('DCA_CUSTOM', 'dca_custom')
DCA_AUTO_PACKAGE = default('DCA_AUTO_PACKAGE', 'auto_dca')

# Derived constants
DCA_AUTO_MODULE = f'{DCA_DIR}.{DCA_AUTO_PACKAGE}'
DCA_AUTO_FILE = f'{DCA_DIR}/{DCA_AUTO_PACKAGE}.py'

# Fields to ifnore while dictifying
DCA_IGNORE_FIELDS = default(
    'DCA_IGNORE_FIELDS', ['created_on', 'updated_on', 'id'])

# Fields to remove while generating model
DCA_REMOVE_FIELDS = default('DCA_REMOVE_FIELDS', [])


# `DCA_AST_MAP` basically says how to extract data
# from a given AST `Assign` object
DCA_AST_MAP = default('DCA_AST_MAP', dict(
    Num=lambda kw: kw.value.n,
    Str=lambda kw: kw.value.s,
    Name=lambda kw: kw.value.id,
    NameConstant=lambda kw: kw.value.value,
    Attribute=lambda kw: '%s.%s' % (kw.value.value.id, kw.value.attr),
))