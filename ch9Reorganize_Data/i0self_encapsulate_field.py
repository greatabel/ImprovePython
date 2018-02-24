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


class CappedRange(IntRange):
    def __init__(self, low, high, cap):
        IntRange.__init__(self, low, high)
        self.cap = cap
    
    def get_high(self):
        return min(self.cap, self.high)

c = CappedRange(0, 10, 5)
print(c.includes(2), c.includes(100), c.get_high())