from termcolor import colored
from myfinal import MyPyFinal


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])
