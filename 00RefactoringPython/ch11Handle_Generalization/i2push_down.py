from mycolor import show

class JobItem_old:
    def __init__(self, unit_price, quantity,
                 is_labor, employee):
        self.unit_price = unit_price
        self.quantity = quantity
        self.is_labor = is_labor
        self.employee = employee

    def get_total_price(self):
        return self.get_unit_price() * self.quantity

    def get_unit_price(self):
        return self.employee.rate if self.is_labor else self.unit_price

class Employee:
    def __init__(self, rate):
        self.rate = rate


j = JobItem_old(9.8, 10000, True, Employee(0.99))
t = j.get_total_price()
print(show(t))
print('-------------改造开始-----------------')
class JobItem:
    def __init__(self, unit_price, quantity):
        self.unit_price = unit_price
        self.quantity = quantity
        self.is_labor = False
        # self.employee = employee

    def get_total_price(self):
        return self.get_unit_price() * self.quantity

    def get_unit_price(self):
        return  self.unit_price

class LaborItem(JobItem):
    def __init__(self, unit_price, quantity, employee):
        super(LaborItem, self).__init__(unit_price, quantity)
        self.is_labor = True
        self.employee = employee

    def get_unit_price(self):
        return self.employee.rate

l = LaborItem(9.8, 10000, Employee(0.99))
t1 = l.get_total_price()
print(show(t1, 'red'))
