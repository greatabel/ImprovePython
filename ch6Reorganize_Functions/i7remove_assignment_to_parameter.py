from datetime import date
from termcolor import colored
from myfinal import MyPyFinal
from dateutil import parser

def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])



def discount(input_val, quantity, year_to_date):
    if input_val > 50:
        input_val -=2
    b = date(1986,1,10)
    dt = parser.parse(year_to_date).date()
    days = (dt - b).days
    return input_val * quantity * days

r = discount(100, 10, '2018-02-22')
print('old way which need to refactory: get_distance_travelled=', show(r))

print(show('降低了代码清晰度，如果你只以参数表示 被传递进来的东西，那么代码会更清澈'))

def discount_after_refactory(input_val, quantity, year_to_date):
    result = input_val
    if input_val > 50:
        result -=2
    b = date(1986,1,10)
    dt = parser.parse(year_to_date).date()
    days = (dt - b).days
    return input_val * quantity * days

after = discount_after_refactory(100, 10, '2018-02-22')
print('old way which need to refactory: get_distance_travelled=', show(after, 'red'))