from mycolor import show

class Employee_Old:
    pass


class Salesman_Old(Employee_Old):
    def __init__(self, name):
        self.name = name

    def set_workedyears(self, year):
        self.workedyears = year
class Enginner_Old(Employee_Old):
    def __init__(self, name):
        self.name = name

    def set_workedyears(self, year):
        self.workedyears = year

s = Salesman_Old('salesman0')
e = Enginner_Old('enginner0')
print(s.name, e.name)
s.set_workedyears(2)
e.set_workedyears(5)
print(s.workedyears, e.workedyears)

print('-------------改造开始-----------------')
class Employee:
    def __init__(self, name):
        self.name = name

    def set_workedyears(self, year):
            self.workedyears = year
class Salesman(Employee):
    pass

class Enginner(Employee):
    pass

s1 = Salesman('salesman1')
e1 = Enginner('enginner1')
s1.set_workedyears(2)
e1.set_workedyears(5)
print(show(s1.name), show(e1.name))
print(s1.workedyears, e1.workedyears)