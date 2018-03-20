import random
from termcolor import colored


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])

class Person(object):
    """docstring for Person"""
    def __init__(self, name, telephone_number):
        self.name = name
        self.telephone_number = telephone_number

    def get_telephone_number(self):
        return "(" + self.telephone_number.area_code + ") " + self.telephone_number.number

class TelephoneNumber:
    def __init__(self, area_code, number):
        self.area_code = area_code
        self.number = number

p = Person('Stone', TelephoneNumber('0613', '00001'))
print('old模式下：' + show(p.get_telephone_number()))

print('incline class: 如果一个类不再承担足够责任、不再有单独存在必要的理由，我们挑选#萎缩类# 最频繁的用户\
    将它塞到另一类中')


class Person_afterRefactory(object):
    """docstring for Person"""
    def __init__(self, name, office_area_code, 
                    office_number):
        self.name = name
        self.office_area_code = office_area_code
        self.office_number = office_number

    # def get_area_code(self):
    #     return self.telephone_number.area_code

    # def get_number(self):
    #     return self.telephone_number.number

    def get_telephone_number(self):
        return "(" + self.office_area_code + ") " + self.office_number

class TelephoneNumber:
    def __init__(self, area_code, number):
        self.area_code = area_code
        self.number = number

p = Person_afterRefactory('Stone', '0613', '00001')
print('new模式下：' + show(p.get_telephone_number(), 'red'))