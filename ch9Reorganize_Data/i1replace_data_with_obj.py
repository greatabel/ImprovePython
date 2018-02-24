from mycolor import show

class Order:
    def __init__(self, customer):
        self.customer = customer


d = Order('xiaoming')
print(show(d.customer))

class Order_afterRF:
    def __init__(self, customer):
        self.customer = customer

class Customer:
    def __init__(self, name):
        self.name = name

d1 = Order(Customer('xiaoming1'))
print(show(d1.customer.name, 'red'))