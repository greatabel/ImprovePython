class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
r = plus_3(4)
print(r)
