class Dog:
    num_legs = 4 # <- class var

    def __init__(self, name):
        self.name = name # instance var

jack = Dog('Jack')
jill = Dog('Jill')
print(jack.num_legs, jill.num_legs)
print(jack.name, jill.name)