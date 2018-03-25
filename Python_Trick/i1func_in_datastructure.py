def bark(text):
    return (text.upper() + "!!!")

funcs = [bark, str.lower, str.capitalize]

print('funcs = ', funcs)

for f in funcs:
    print(f, f('hey there'))

print(funcs[0]('hey 0'))


print('Functions Can Be Passed to Other Functions')

def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

greet(bark)

def whisper(text):
    return text.lower() + '...'

greet(whisper)