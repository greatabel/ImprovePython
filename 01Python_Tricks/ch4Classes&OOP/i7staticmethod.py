class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()

print(obj.method())
print(MyClass.method(obj))
print(obj.classmethod())
print(obj.staticmethod())

print('\n')
print(MyClass.classmethod())
print(MyClass.staticmethod())


import math 

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza{self.radius!r}, '
            f'Pizza({self.ingredients!r})' )

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r**2 * math.pi

    @classmethod
    def margherita(cls):
        return cls(2, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(2, ['mozzarella', 'tomatoes', 'ham'])


print('\n')
print(Pizza(2, ['mozzarella', 'tomatoes']))
print(Pizza(2, ['mozzarella', 'tomatoes', 'ham', 'mushrooms']))
print(Pizza(2, ['mozzarella'] * 4))

print('\n')
print(Pizza.margherita())
print(Pizza.prosciutto())

print('\n')
p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p.area(), p.circle_area(4))
