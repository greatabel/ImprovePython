class Quantity(object):
    def __init__(self, value, units):
        self.value = value
        self.units = units

    def __str__(self):
        return "{} {}".format(self.value, self.units)