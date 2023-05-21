import types
from enum import Enum


INT_TYPE = int
FLOAT_TYPE = float
BOOL_TYPE = bool
STRING_TYPE = str
NONE_TYPE = types.NoneType
BYTES_TYPE = bytes
CODE_TYPE = types.CodeType
FUNC_TYPE = types.FunctionType
METHOD_TYPE = types.MethodType
CLASS_TYPE = type
GENERATOR_TYPE = types.GeneratorType
MODULE_TYPE = types.ModuleType

# COLLECTIONS
LIST_TYPE = list
TUPLE_TYPE = tuple
DICT_TYPE = dict
SET_TYPE = set
FROZENSET_TYPE = frozenset
BYTEARRAY_TYPE = bytearray


class Serializer(Enum):
    Json = 1,
    Xml = 2
