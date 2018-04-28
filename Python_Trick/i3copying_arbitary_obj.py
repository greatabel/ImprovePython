class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


a = Point(20, 40)
import copy
b = copy.copy(a)
print(a, b)
print(a == b)
print(a is b)

