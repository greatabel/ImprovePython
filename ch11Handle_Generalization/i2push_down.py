from mycolor import show

class JobItem:
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


j = JobItem(9.8, 10000, True, Employee(0.99))
t = j.get_total_price()
print(show(t))
print('-------------改造开始-----------------')

