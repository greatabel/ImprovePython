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

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft 
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                        f'{self.bottomright!r})')

rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
print(rect, srect)
print(rect == srect)
print(rect is srect)

rect.topleft.x = 999
print(rect, srect)

drect = copy.deepcopy(rect)
print(rect, drect)
drect.topleft.x = 1000
rect.bottomright.x = 2000
print(rect, drect)
