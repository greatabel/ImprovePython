class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

    def __repr__(self):
        return '__repr__ for Car'


if __name__ == "__main__":
    my_car = Car('red', 12345)
    print(my_car)
    print('str(my_car)=', str(my_car))
    print('{}'.format(my_car))
    print(str([my_car]))
    print(repr(my_car))

    import datetime
    today = datetime.date.today()
    print(str(today), repr(today) )
    

