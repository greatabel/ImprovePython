from mycolor import show

senirotiy  = 1
months_disabled = 13
is_parttime = True

def disability_amount():
    if senirotiy < 2:
        return 0
    if months_disabled > 12:
        return 0
    if is_parttime:
        return 0

print(show(disability_amount()))

print('有一系列条件测试，都得到相同结果；'+
    '你可以将测试合并为一个条件表达式， 将这个条件表达式提炼为独立函数')
print('- · - - · - - · - - · - ')

def isnot_eligable_for_disability():
    if senirotiy < 2 or months_disabled > 12 \
        or is_parttime:
        return True

def disability_amount_afterRF():
    if isnot_eligable_for_disability():
        return 0

print(show(disability_amount_afterRF(), 'red') )