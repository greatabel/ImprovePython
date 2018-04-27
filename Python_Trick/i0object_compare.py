a = [1, 2, 3]
b = a 

assert a == b
assert a is b

print('We can do that by calling list() on the existing list to create a copy we’ll name c')
c = list(a)

assert a == c
assert a is c