print(globals())

def test():
    print("hello")

print(globals())

import string
print(string.capwords("this is a test"))

from string import capwords
print(globals())

import math as math_ops
print(math_ops.pi)