add = lambda x, y: x + y

r = add(5, 3)
print(r)


tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
r1 = sorted(tuples, key=lambda x: x[1])
print(r1)

r2 = sorted(range(-5, 6), key=lambda x: x * x)
print(r2)