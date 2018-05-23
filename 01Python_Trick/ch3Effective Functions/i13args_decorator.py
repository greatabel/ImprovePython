import functools

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f,'#'*3,  args, '@'*3,  kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function

@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)

greet('Hello', 'Bob')