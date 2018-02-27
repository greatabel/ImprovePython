import random
import datetime
from dateutil import parser
from mycolor import show


mydate = parser.parse('2018-02-27').date()
mydate += datetime.timedelta(days=random.randint(-300, 300))
print(mydate)

SUMMER_START = parser.parse('2018-06-01').date()
SUMMER_END = parser.parse('2018-09-01').date()
if mydate < SUMMER_START or mydate > SUMMER_END:
    charge = 10
else:
    charge = 100

print(show(charge))