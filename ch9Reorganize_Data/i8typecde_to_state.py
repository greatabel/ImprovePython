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
print(show('开始改造'),'- > -'*5)