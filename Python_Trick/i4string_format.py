errno = 50159747054
name = 'Bob'

print('Hello, {}'.format(name))
print('Hello, {name} there is a 0x{errno:x}'.format(name=name, errno=errno))

print(f'Hello, {name}!')

a = 5
b = 10
print(f'Five + ten is {a + b} and not {2 * (a + b)}')

def greet(name, question):
    return f"Hello {name}! How 's it {question}?"

print(greet('bob', 'going'))