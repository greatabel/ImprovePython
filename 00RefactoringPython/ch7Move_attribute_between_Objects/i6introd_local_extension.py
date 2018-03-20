from dateutil import parser
import datetime
from mycolor import show

class MyDate(datetime.datetime):
    def next_day(self):
        newstart = self + datetime.timedelta(days=1) 
        return newstart

d = MyDate(2018, 2, 24, 14, 37)
print('new way:', show(d.next_day(), 'red')) 