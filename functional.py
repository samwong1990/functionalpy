from functools import reduce

def compose(*functions,has_args=True):
    """from http://mathieularose.com/function-composition-in-python/

    But I don't agree with his composition definition
    I think f o g = g(f(x)) is a more useful composition

    """
    if has_args:
    	return reduce(lambda f, g: lambda args: g(f(args)), functions)
    else:
    	return reduce(lambda f, g: g(f), functions)

flip = lambda f: lambda *a: f(*reversed(a))

do_in_order = compose