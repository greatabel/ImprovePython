from mycolor import show

class IntRange:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def includes(self, arg):
        return arg >= self.low and arg <= self.high

    def grow(self, factor):
        self.high = self.high * factor

r = IntRange(0, 10)
print(r.includes(2), r.includes(100))