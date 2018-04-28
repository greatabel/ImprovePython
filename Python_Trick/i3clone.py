print('shallow copy')

xs = [[1, 2, 3], [4, 5, 6]]
ys = list(xs)
print(xs, ys)

xs.append(['new sublist'])
print(xs, ys)

xs[1][0] = 'X'
print(xs, ys)

print('Making Deep Copies')
import copy
zs = copy.deepcopy(xs)
print(xs, zs)

xs[1][0] = 'XX'
print(xs, zs)