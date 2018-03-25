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

print('Python attaches a string identifier to every function\
 at creation time for debugging purposes')
print('bark.__name__ = ', bark.__name__)

