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
