import random


platform = 'mac osx'
browser = 'ie 10'
resize = 3

def was_initialized():
    return random.choice([True, False])

if 'MAC' in platform.upper() and \
    'IE' in browser.upper() and \
    was_initialized and resize > 0:
    print('do something')


print('表达式可能非常复杂而难以阅读，临时变量可以帮助你将表达式分解成\
    比较容易管理的形式')

isMacOs = True if 'MAC' in platform.upper() else False
isIEbrowser = True if 'IE' in browser.upper() else False
wasResize = True if resize > 0 else False

if isMacOs and isIEbrowser and was_initialized and wasResize:
    print('do something too!')
