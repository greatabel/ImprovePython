def null_decorator(func):
    return func

def greet():
    return "Hello!"

a_greet = null_decorator(greet)
r = a_greet()
print(r)