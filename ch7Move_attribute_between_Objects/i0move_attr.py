import random
from termcolor import colored


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
        return random.choice([True, False])

at = Account(random.randint(5,20))
print(at.bank_charge())