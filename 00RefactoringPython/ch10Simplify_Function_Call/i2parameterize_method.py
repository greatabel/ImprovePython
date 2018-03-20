from mycolor import show

class Employee(object):
    def __init__(self):
        self.salary = 0

    def ten_percent_raise(self):
        self.salary *= 1.1

    def five_percent_raise(self):
        self.salary *= 1.05

e = Employee()
e.salary = 10000
e.ten_percent_raise()
print(e.salary)
e.five_percent_raise()
print(e.salary)

print('-------------改造开始-----------------')
class Employee_afterRF:
    def __init__(self):
        self.salary = 0

    def raise_salary(self, factor):
        self.salary *= factor 

e1 = Employee_afterRF()
e1.salary = 10000
e1.raise_salary(1.1)
print(e1.salary)
e1.raise_salary(1.05)
print(e1.salary)
