add = lambda x, y: x + y

r = add(5, 3)
print(r)


tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
r1 = sorted(tuples, key=lambda x: x[1])
print(r1)

r2 = sorted(range(-5, 6), key=lambda x: x * x)
print(r2)

def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)
plus_5 = make_adder(5)
print('plus_3(4)=', plus_3(4))
print('plus_5(4)=', plus_5(4))