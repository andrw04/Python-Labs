from constants import *
import inspect
from types import NoneType, ModuleType, CodeType, FunctionType, \
    BuiltinFunctionType, CellType, MappingProxyType, \
    WrapperDescriptorType, MethodDescriptorType,\
    GetSetDescriptorType


class ObjectConverter:
    """
    This class provides an opportunity to pack python objects to dictionary
    which can be used to convinient serialization. So it can convert data
    from dictionary to different python objects.
    """

    @classmethod
    def get_dict(cls, obj, is_inner_func=False):
        if type(obj) in (int, float, bool, str, NoneType):
            return obj

        if type(obj) is list:
            return [cls.get_dict(elem) for elem in obj]

        result = {}
        result[TYPE] = type(obj).__name__

        if type(obj) is dict:
            result[SOURCE] = [[cls.get_dict(key), cls.get_dict(
                value)] for key, value in obj.items()]
            return result

        if type(obj) in (set, frozenset, tuple, bytes, bytearray):
            result[SOURCE] = cls.get_dict([*obj])
            return result

        if type(obj) is complex:
            result[SOURCE] = {complex.real.__name__: obj.real,
                              complex.imag.__name__: obj.imag}
            return result

        if type(obj) is ModuleType:
            result[SOURCE] = obj.__name__
            return

        if type(obj) is CodeType:
            source = cls.get_code(obj)
            result[SOURCE] = source
            return result

        if type(obj) is CellType:
            result[SOURCE] = cls.get_dict(obj.cell_contents)
            return result

        if type(obj) in (staticmethod, classmethod):
            result[SOURCE] = cls.get_dict(obj.__func__, is_inner_func)
            return result

        if inspect.isroutine(obj):
            result[SOURCE] = cls.get_routine_dict(obj, is_inner_func)
            return result

        elif inspect.isclass(obj):
            result[SOURCE] = cls.get_class_dict(obj)
            return result

        else:
            result[SOURCE] = cls.get_object_dict(obj)
            return result

    @classmethod
    def get_global_vars(cls, func, is_inner_func):
        pass

    @classmethod
    def get_obj_dict(cls, obj):
        dictionary = {key: value for key, value in obj.__dict__items()}
        dictionary2 = {}

        for key, value in dictionary.items():
            if type(value) not in UNIQUE_TYPES:
                dictionary2[cls.get_dict(key)] = cls.get_dict(
                    value, is_inner_func=True)
            else:
                dictionary2[cls.get_dict(key)] = cls.get_dict(value)

        return dictionary2

    @classmethod
    def get_object(cls, dict):
        """
        Creates object from dictionary
        """
        pass

    @classmethod
    def get_code(cls, obj: CodeType):
        result = {}

        for key, value in inspect.getmembers(obj):
            if key in CODE_PROPERTIES:
                result[key] = cls.get_dict(value)

        return result

    @classmethod
    def get_routine_dict(cls, obj, is_inner_func):
        result = {}

        # Code
        result[CODE] = cls.get_dict(obj.__code__)

        # Global vars
        global_vars = cls.get_global_vars(obj, is_inner_func)
        result[GLOBALS] = cls.get_dict(global_vars)

        # Name
        result[NAME] = cls.get_dict(obj.__name__)

        # Defaults
        result[DEFAULTS] = cls.get_dict(obj.__defaults__)

        # Closure
        result[CLOSURE] = cls.get_dict(obj.__closure__)

        return result

    @classmethod
    def get_class_dict(cls, obj):
        result = {}

        # Name
        result[NAME] = cls.get_dict(obj.__name__)

        # Bases
        result[BASES] = cls.get_dict(
            tuple(base for base in obj.__bases__ if base != object))

        # Dict
        result[DICT] = cls.get_obj_dict(obj)

        return result

    @classmethod
    def get_object_dict(cls, obj):
        result = {}

        # Class
        result[CLASS] = cls.get_dict(obj.__class__)

        # Dict
        result[DICT] = cls.get_object_dict(obj)

        return result


# def get_gvars(func, is_inner_func):
#     name = func.__name__
#     gvars = {}

#     for gvar_name in func.__code__.co_names:
#         # Separating the variables that the function needs
#         if gvar_name in func.__globals__:

#             # Module
#             if type(func.__globals__[gvar_name]) is MODULE_TYPE:
#                 gvars[gvar_name] = func.__globals__[gvar_name]

#             # Class
#             elif inspect.isclass(func.__globals__[gvar_name]):
#                 # To prevent recursion, the class in which this method is declared is replaced with the
#                 # name of the class. In the future, this name will be replaced by the class type
#                 c = func.__globals__[gvar_name]
#                 # !!!!
#                 if is_inner_func and name in c.__dict__ and func == c.__dict__[name].__func__:
#                     gvars[gvar_name] = c.__name__
#                 else:
#                     gvars[gvar_name] = c

#             # Recursion protection
#             elif gvar_name == func.__code__.co_name:
#                 gvars[gvar_name] = func.__name__

#             else:
#                 gvars[gvar_name] = func.__globals__[gvar_name]

#     return gvars


# def get_obj_dict(obj):
#     dct = {item[0]: item[1] for item in obj.__dict__.items()}
#     dct2 = {}

#     for key, value in dct.items():
#         if type(value) not in UNIQUE_TYPES:
#             if inspect.isroutine(value):
#                 # Recursion protection
#                 dct2[to_dict(key)] = to_dict(value, is_inner_func=True)
#             else:
#                 dct2[to_dict(key)] = to_dict(value)

#     return dct2


# def from_dict(obj, is_dict=False):

#     if is_dict:
#         return {from_dict(item[0]): from_dict(item[1]) for item in obj}

#     if type(obj) not in (dict, list):
#         return obj

#     elif type(obj) is list:
#         return [from_dict(o) for o in obj]

#     else:
#         obj_type = obj[TYPE_KW]
#         obj_source = obj[SOURCE_KW]

#         if obj_type == dict.__name__:
#             return from_dict(obj_source, is_dict=True)

#         # Key - type name, value - type itself. Calling by type name returns that type.
#         # This is necessary for the same creation of simple collections.
#         cols_dict = {t.__name__: t for t in [
#             set, frozenset, tuple, bytes, bytearray]}
#         if obj_type in cols_dict:
#             return cols_dict[obj_type](from_dict(obj_source))

#         if obj_type == complex.__name__:
#             return obj_source[complex.real.__name__] + \
#                 obj_source[complex.imag.__name__] * 1j

#         if obj_type == MODULE_TYPE.__name__:
#             return __import__(obj_source)

#         if obj_type == CODE_TYPE.__name__:
#             return CODE_TYPE(*[from_dict(obj_source[prop]) for prop in CODE_PROPS])

#         if obj_type == types.CellType.__name__:
#             return types.CellType(from_dict(obj_source))

#         if obj_type == staticmethod.__name__:
#             return staticmethod(from_dict(obj_source))

#         if obj_type == classmethod.__name__:
#             return classmethod(from_dict(obj_source))

#         if obj_type == FUNC_TYPE.__name__:
#             code = from_dict(obj_source[CODE_KW])
#             gvars = from_dict(obj_source[GLOBALS_KW])
#             name = from_dict(obj_source[NAME_KW])
#             defaults = from_dict(obj_source[DEFAULTS_KW])
#             closure = from_dict(obj_source[CLOSURE_KW])

#             # If there are suitable global variables, they are replaced.
#             for key in gvars:
#                 if key in code.co_name and key in globals():
#                     gvars[key] = globals()[key]

#             func = FUNC_TYPE(code, gvars, name, defaults, closure)

#             # Restoring recursion
#             if func.__name__ in gvars:
#                 func.__globals__.update({func.__name__: func})

#             return func

#         if obj_type == type.__name__:
#             name = from_dict(obj_source[NAME_KW])
#             bases = from_dict(obj_source[BASES_KW])
#             dct = obj_source[DICT_KW]
#             dct = {from_dict(item[0]): from_dict(item[1])
#                    for item in dct.items()}

#             cl = type(name, bases, dct)

#             # Restore a reference to the current class in the nested method __globals__
#             for attr in cl.__dict__.values():
#                 if inspect.isroutine(attr):
#                     if type(attr) in (staticmethod, classmethod):
#                         fglobs = attr.__func__.__globals__
#                     else:
#                         fglobs = attr.__globals__

#                     for gv in fglobs.keys():
#                         if gv == cl.__name__:
#                             fglobs[gv] = cl

#             return cl

#         else:
#             clas = from_dict(obj_source[CLASS_KW])
#             dct = obj_source[DICT_KW]
#             dct = {from_dict(item[0]): from_dict(item[1])
#                    for item in dct.items()}

#             o = object.__new__(clas)
#             o.__dict__ = dct

#             return o


def foo(a=1, b=10):
    return a + b


if __name__ == "__main__":
    d = ObjectConverter.get_dict(foo)
    print(d)
