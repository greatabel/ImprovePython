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


def special_calculate_with_assert(x):
    assert x > 0
    return math.sqrt(x) * 10

t2 = special_calculate_with_assert(4)
# t2 = special_calculate_with_assert(-4)
print(t0, t2)