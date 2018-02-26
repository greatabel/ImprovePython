from mycolor import show

class Old_Employee:
    engineer = 0
    salesman = 1
    manager  = 2

    def __init__(self, type):
        self.type = type

e = Old_Employee(2)
print(e.type)
print(show('开始改造'),'- > -'*5)

class Employee:
    instance = None

    def __init__(self, type):
        self.type = type

    @staticmethod
    def get_instnace(type):
        if Employee.instance is None:
            if type == 0:
                Employee.instance = Engineer(type)
            elif type == 1:
                Employee.instance = Salesman(type)
            else:
                Employee.instance = Manager(type)
        return Employee.instance

class Engineer(Employee):
    pass

class Salesman(Employee):
    pass

class Manager(Employee):
    pass

c2 = Employee.get_instnace(2)
print(show(c2.type))