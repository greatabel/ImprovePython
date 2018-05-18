from collections import namedtuple


Car = namedtuple('Car', [
    'color', 'mileage'])

class MyCarWithMethod(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethod('red', 3456.7)
print(c.hexcolor())