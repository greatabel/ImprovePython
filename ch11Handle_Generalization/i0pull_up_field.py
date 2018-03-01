from mycolor import show

class Employee_Old:
    pass


class Salesman_Old(Employee_Old):
    def __init__(self, name):
        self.name = name

class Enginner_Old(Employee_Old):
    def __init__(self, name):
        self.name = name

s = Salesman_Old('salesman0')
e = Enginner_Old('enginner0')
print(s.name, e.name)

print('-------------改造开始-----------------')
class Employee:
    def __init__(self, name):
        self.name = name

class Salesman(Employee):
    pass

class Enginner(Employee):
    pass

s1 = Salesman('salesman1')
e1 = Enginner('enginner1')
print(show(s1.name), show(e1.name))