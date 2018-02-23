import random
from termcolor import colored


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])

class Person(object):
    """docstring for Person"""
    def __init__(self, name, office_area_code, 
                    office_number):
        self.name = name
        self.office_area_code = office_area_code
        self.office_number = office_number

    def get_telephone_number(self):
        return "(" + self.office_area_code + ") " + self.office_number

p = Person('Stone', '0613', '00001')
print('旧模式下：' + show(p.get_telephone_number()))

class Person_afterRefactory(object):
    """docstring for Person"""
    def __init__(self, name, telephone_number,
                    office_number):
        self.name = name

        self.office_number = office_number
        self.telephone_number = telephone_number

    def get_office_areacode(self):
        return self.telephone_number.area_code

    def get_telephone_number(self):
        return "(" + self.telephone_number.area_code + ") " + self.office_number

class TelephoneNumber:
    def __init__(self, area_code):
        self.area_code = area_code

p = Person_afterRefactory('Stone', TelephoneNumber('0613'), '00001')
print('new模式下：' + show(p.get_telephone_number(), 'red'))