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
