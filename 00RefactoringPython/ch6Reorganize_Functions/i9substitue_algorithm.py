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

print(show('如果你发现做一件事有更清晰的方式，应该以更清晰的方式取代复杂的方式\
    有时候你必须壮士扼腕，删掉整个算法，代之以更简单的算法'))
def found_people_after_refactory(people):
    candidates = ['Don', 'John', 'Kent']
    for p in people:
        if p in candidates:
            return p
    return ''

p = found_people_after_refactory(people)
print('New way which need to refactory:', show(p, 'red'))