from constants import *


def repr_object(obj):
    """This function returns dictionary of difficult object options of string type"""
    if type(obj) in (INT_TYPE, FLOAT_TYPE, BOOL_TYPE, STRING_TYPE, NONE_TYPE):
        return obj
    
    elif type(obj) in (LIST_TYPE, TUPLE_TYPE, SET_TYPE, FROZENSET_TYPE, DICT_TYPE):
        return obj
    
    elif type(obj) is FUNC_TYPE:
        return repr_object(func_data(obj))
    
    elif type(obj) is CODE_TYPE:
        return repr_object(code_data(obj))
    
    elif type(obj) is CLASS_TYPE:
        return
    
    else:
        return
    

def pack_iterable(obj):
    if obj is DICT_TYPE:
        packed = {}

        for key, value in obj:
            packed[key] = repr_object(value)

        return packed
    
    else:
        packed = []

        for value in obj:
            packed.append(repr_object(value))

        if obj is TUPLE_TYPE:
            return tuple(packed)
        
        elif obj is SET_TYPE:
            return set(packed)
        
        elif obj is FROZENSET_TYPE:
            return frozenset(packed)
        
        else:
            return packed

    
def func_data(obj : FUNC_TYPE):
    result = {"type": "function"}

    if type(obj) is METHOD_TYPE:
        obj = obj.__func__

    result["__name__"] = obj.__name__

    globals = {}

    used_globals = obj.__code__.co_names

    for global_var in used_globals:
        if global_var in obj.__globals__:
            globals[global_var] = obj.__globals__[global_var]
                
    result['__globals__'] = globals
    result['__code__'] = code_data(obj.__code__)
    result['__closure__'] = obj.__closure__
    result['__argdefs__'] = obj.__defaults__

    return result


def create_function(dictionary : dict):

    args = [
        create_code(dictionary["__code__"]),
        dictionary["__globals__"],
        dictionary["__name__"],
        dictionary["__argdefs__"],
        dictionary["__closure__"]
    ]
    
    return types.FunctionType(*args)
    

def code_data(obj : CODE_TYPE):
    "This function returns dictionary of code options"
    result = {
        "co_argcount": obj.co_argcount,
        "co_posonlyargcount": obj.co_posonlyargcount,
        "co_kwonlyargcount": obj.co_kwonlyargcount,
        "co_nlocals": obj.co_nlocals,
        "co_stacksize": obj.co_stacksize,
        "co_flags": obj.co_flags,
        "co_code": list(obj.co_code),
        "co_consts": obj.co_consts,
        "co_names": obj.co_names,
        "co_varnames": obj.co_varnames,
        "co_filename": obj.co_filename,
        "co_name": obj.co_name,
        "co_firstlineno": obj.co_firstlineno,
        "co_linetable": list(obj.co_linetable),
        "co_freevars": obj.co_freevars,
        "co_cellvars": obj.co_cellvars
    }

    return result


def create_code(dictionary : dict):
    args = [
        dictionary["co_argcount"],
        dictionary["co_posonlyargcount"],
        dictionary["co_kwonlyargcount"],
        dictionary["co_nlocals"],
        dictionary["co_stacksize"],
        dictionary["co_flags"],
        bytes(dictionary["co_code"]),
        dictionary["co_consts"],
        dictionary["co_names"],
        dictionary["co_varnames"],
        dictionary["co_filename"],
        dictionary["co_name"],
        dictionary["co_firstlineno"],
        bytes(dictionary["co_linetable"]),
        dictionary["co_freevars"],
        dictionary["co_cellvars"]
    ]

    return types.CodeType(*args)


def class_data(obj : CLASS_TYPE):
    result = {"type": "class"}
    result = {"__name__": obj.__name__}

    # TODO#1 Base classes

    # TODO#2 Dictionary of options


def create_class(dictionary : DICT_TYPE):
    pass


def foo(a = 20, b = 30):
    return a + b


if __name__ == '__main__':
    data = func_data(foo)
    print(data)
