from collections import namedtuple

print('namedtuples are a memory- efficient shortcut to defining \
    an immutable class in Python manually.')

Car = namedtuple('Car', [
    'color', 'mileage'])

my_car = Car('red', 3456.7)
print(my_car.color, my_car.mileage)