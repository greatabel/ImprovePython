def yell(text):
    print(text.upper() + "!")

yell('hello')

bark = yell

bark('woof')

try: 
    del yell
    yell('hello again')
except:
    print("This is an error message in yell() !")

bark('hey')

print('bark.__name__ = ', bark.__name__)