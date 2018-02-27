from termcolor import colored


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])