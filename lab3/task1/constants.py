import types
from enum import Enum

# KEY WORDS
TYPE = "type"
SOURCE = "source"

CODE = "__code__"
GLOBALS = types.FunctionType.__globals__.__name__
NAME = "__name__"
DEFAULTS = "__defaults__"
CLOSURE = types.FunctionType.__closure__.__name__

BASES = "__bases__"
DICT = "__dict__"

CLASS = "__class__"
OBJECT = "object"


CODE_PROPERTIES = [prop.__name__ for prop in [
    types.CodeType.co_argcount,
    types.CodeType.co_posonlyargcount,
    types.CodeType.co_kwonlyargcount,
    types.CodeType.co_nlocals,
    types.CodeType.co_stacksize,
    types.CodeType.co_flags,
    types.CodeType.co_code,
    types.CodeType.co_consts,
    types.CodeType.co_names,
    types.CodeType.co_varnames,
    types.CodeType.co_filename,
    types.CodeType.co_name,
    types.CodeType.co_firstlineno,
    types.CodeType.co_lnotab,
    types.CodeType.co_freevars,
    types.CodeType.co_cellvars]
]




UNIQUE_TYPES = [
    types.MappingProxyType,
    types.WrapperDescriptorType,
    types.MemberDescriptorType,
    types.GetSetDescriptorType,
    types.BuiltinFunctionType
]


class Serializer(Enum):
    Json = 1,
    Xml = 2
