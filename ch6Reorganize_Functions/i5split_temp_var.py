from termcolor import colored

def show(s,color='green'):
    print(colored(s, color, attrs=['reverse', 'blink']))

height = 100
width = 50
temp = 2 * (height * width)
print(temp)
temp = height * width
print(temp)

show('当你程序中某个临时变量被赋值超过一次，但不是♻️循环变量，也不用于收集计算结果。')
show('针对每次赋值，创造一个独立、对应的临时变量', 'red')

