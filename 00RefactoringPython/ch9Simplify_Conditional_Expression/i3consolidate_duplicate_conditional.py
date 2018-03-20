import random
from mycolor import show

price = 9.8

def is_special_deal():
    return random.choice([True, False])

def send():
    print('send')

if is_special_deal():
    total = price * 0.5
    send()
else:
    total = price * 0.8
    send()

print('在表达式的每个分支上又相同的代码，将重复代码搬移到表达式之外')
print('- · - - · - - · - - · - ')


if is_special_deal():
    total = price * 0.5
else:
    total = price * 0.8
send()