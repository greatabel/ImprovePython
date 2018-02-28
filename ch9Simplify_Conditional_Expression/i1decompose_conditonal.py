import random
import datetime
from dateutil import parser
from mycolor import show

winter_rate = 0.01
summer_rate = 0.02
mydate = parser.parse('2018-02-27').date()
mydate += datetime.timedelta(days=random.randint(-300, 300))
print(mydate)
myquantity = 10000

SUMMER_START = parser.parse('2018-06-01').date()
SUMMER_END = parser.parse('2018-09-01').date()
if mydate < SUMMER_START or mydate > SUMMER_END:
    charge = myquantity * winter_rate * 1.1
else:
    charge = myquantity * summer_rate

print(show(charge))
print('- · - - · - - · - - · - ')

def not_summer(mydate):
    if mydate < SUMMER_START or mydate > SUMMER_END:
        return True
    else:
        return False

def winter_charge(quantity):
    return quantity * winter_rate * 1.1

def summer_charge(quantity):
    return quantity * summer_rate

if not_summer(mydate):
    charge1 = winter_charge(myquantity)
else:
    charge1 = summer_charge(myquantity)

print(show(charge1, 'red'))