import math
from mycolor import show

def special_calculate(x):
    if x > 0:
        return math.sqrt(x) * 10
    else:
        raise ValueError('Error here!')

t0 = special_calculate(4)
# t1 = special_calculate(-4)
print('- · - - · 开始改造 - - · - - · - ')

