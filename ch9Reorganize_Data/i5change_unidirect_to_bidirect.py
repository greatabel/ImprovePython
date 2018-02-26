from mycolor import show

class Order:
    def __init__(self, customer):
        self.customer = customer

class Customer:
    def __init__(self, name):
        self.name = name

d0 = Order(Customer('xiaoming'))
print(d0.customer.name)

print(show('开始改造'),'- > '*10)

class Order_afterRF:
    def __init__(self, customer):
        self.customer = customer

class Customer_afterRF:
    def __init__(self, name):
        self.name = name