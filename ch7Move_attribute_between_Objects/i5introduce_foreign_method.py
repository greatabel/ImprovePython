from dateutil import parser
import datetime
from mycolor import show

yourinput_date = '2018-02-24 14:19'

dt = parser.parse(yourinput_date)
newstart = dt + datetime.timedelta(days=1)
print('old way:', show(newstart))

print('如果这种事情发生太多次；重复代码是万恶之源，重复代码应该被抽出来放在一个函数,\
    这个函数原本应该在提供服务的类中实现，只不过无法修改\
    不要忘记：这只是权宜之计')
def next_day(input_date):
    dt = parser.parse(input_date)
    newstart = dt + datetime.timedelta(days=1) 
    return newstart

print('new way:', show(next_day(yourinput_date), 'red'))   

