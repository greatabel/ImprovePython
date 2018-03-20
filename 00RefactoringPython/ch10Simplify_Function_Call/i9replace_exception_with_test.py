from mycolor import show

_values = ['test0', 'test1']
def get_value_for_period_old(period_number):
    try:
        return _values[period_number]
    except ValueError:
        print("Oops!  That was wrong period_number!")
        return 0

get_value_for_period_old(1)

print('异常 只应该呗用于异常、罕见的行为，'+show('不应该成为条件检查的替代品'))
print('-------------改造开始-----------------')
def get_value_for_period(period_number):
    if period_number >= len(_values):
        return 0
    return _values[period_number]

print(get_value_for_period(1))
print(get_value_for_period(2))