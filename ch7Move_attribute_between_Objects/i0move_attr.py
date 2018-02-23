import random
from termcolor import colored

random_int = random.randint(5,20)
random_bool = random.choice([True, False])

def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])

'''
假设有几种账户，每一种都有自己的‘透支金额计费计划‘
'''
class Account:
    def __init__(self, days_overdrawn=0):
        self.type = AccountType()
        self.days_overdrawn = days_overdrawn

    def over_draft_charge(self):
        if self.type.is_premium():
            result = 10
            if self.days_overdrawn > 7:
                result + (self.days_overdrawn - 7) * 0.85
            return result
        else:
            return self.days_overdrawn * 1.75

    def bank_charge(self):
        result = 4.5
        if self.days_overdrawn > 0:
            result += self.over_draft_charge()
        return result

class AccountType:
    def is_premium(self):
        return random_bool

at = Account(random_int)
print('旧模式下：' + show(at.bank_charge()))

print(show('开始改造：---------->>>>>>>>>'))
class Account_afterRefactory:
    def __init__(self, days_overdrawn=0):
        self.type = AccountType_afterRefactory()
        self.days_overdrawn = days_overdrawn

    def bank_charge(self):
        result = 4.5
        if self.days_overdrawn > 0:
            result += self.type.over_draft_charge(self.days_overdrawn)
        return result

class AccountType_afterRefactory:
    def is_premium(self):
        return random_bool

    def over_draft_charge(self, days_overdrawn):
        if self.is_premium():
            result = 10
            if days_overdrawn > 7:
                result + (days_overdrawn - 7) * 0.85
            return result
        else:
            return days_overdrawn * 1.75

at1 = Account_afterRefactory(random_int)
print('新式下：' + show(at1.bank_charge(), 'red'))
