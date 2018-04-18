def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'trace: calling {func.__name__}() '
               f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'trace: {func.__name__}() '
              f'returned {original_result}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

say('Abel', 'Hello World!')