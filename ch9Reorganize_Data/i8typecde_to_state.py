from mycolor import show

class Old_Employee:
    engineer = 0
    salesman = 1
    manager  = 2


    def __init__(self, type):
        self.type = type

    def pay_amount(self, type):
        monthly_salary = 10000
        commission = 5000
        bonus = 20000

        if type == Old_Employee.engineer:
            return monthly_salary
        elif type == Old_Employee.salesman:
            return monthly_salary + commission
        elif type == Old_Employee.manager:
            return monthly_salary + bonus
        else:
            raise ValueError('what happened?')


e = Old_Employee(2)
print(e.type, e.pay_amount(e.type))
print('假设工程师可以晋升为经理，对象类型是可变，我们不能' +
    '使用继承方式处理类型码')

print(show('开始改造'),'- > -'*5)



class Employee:
    engineer = 0
    salesman = 1
    manager  = 2

    monthly_salary = 10000
    commission = 5000
    bonus = 20000
    def __init__(self, code):
        self.type = EmployeeType().new_type(code)

    def pay_amount(self):
        return self.type.pay_amount()
        

class EmployeeType:
    def new_type(self, code):
        if code == Employee.engineer:
            return Engineer()
        elif code == Employee.salesman:
            return Salesman()
        elif code == Employee.manager:
            return Manager()
        else:
            raise ValueError('what happened?')

class Engineer(EmployeeType):
    def pay_amount(self):
        return Employee.monthly_salary

class Salesman(EmployeeType):
    def pay_amount(self):
        return Employee.monthly_salary + Employee.commission

class Manager(EmployeeType):
    def pay_amount(self):
        return Employee.monthly_salary + Employee.bonus

n = Employee(2)
print(n.type, n.pay_amount())