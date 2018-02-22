from termcolor import colored
from myfinal import MyPyFinal


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])

def found_person(people):
    for p in people:
        if p == 'Don':
            return 'Don'
        if p == 'John':
            return 'John'
        if p == 'Kent':
            return 'Kent'

    return ''

people = ['Abel', 'Bob', 'Cook', 'Don']
p = found_person(people)
print('old way which need to refactory:', show(p))

def found_people_after_refactory(people):
    candidates = ['Don', 'John', 'Kent']
    for p in people:
        if p in candidates:
            return p
    return ''

p = found_people_after_refactory(people)
print('New way which need to refactory:', show(p, 'red'))