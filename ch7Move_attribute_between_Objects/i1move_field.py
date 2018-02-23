import random
from termcolor import colored

random_int = random.randint(5,20)


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])

'''
假设有几种账户，每一种都有自己的‘透支金额计费计划‘
'''
class Account:
    def __init__(self, interest_rate=0):
        self.type = AccountType()
        self.interest_rate = interest_rate

    def interst_for_amount_days(self, amount, days):
        return self.interest_rate * amount * days / 365

class AccountType:
    pass

at = Account(random_int)
print('旧模式下：' + show(at.interst_for_amount_days(1000, 100)))

print(show('开始改造：---------->>>>>>>>>'))

class Account_afterRefactory:
    def __init__(self, interest_rate=0):
        self.type = AccountType_afterRefactory()
        self.interest_rate = interest_rate

    def interst_for_amount_days(self, amount, days):
        return self.interest_rate * amount * days / 365

class AccountType_afterRefactory:
    pass