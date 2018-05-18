from collections import namedtuple


Car = namedtuple('Car', [
    'color', 'mileage'])

my_car = Car('red', 3456.7)
print(my_car.color, my_car.mileage)