from mycolor import show

class Order:
    def __init__(self, customer):
        self.customer = customer

class Customer:
    def __init__(self, name):
        self.name = name

d0 = Order(Customer('xiaoming0'))
print(d0.customer.name)

print(show('开始改造'),'- > -'*5)

class Order_afterRF:
    def __init__(self, customers=None):
        self.customers = customers

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)

class Customer_afterRF:
    def __init__(self, name, orders=None):
        self.name = name
        self.orders = orders

    def add_order(self, order):
        self.orders.append(order)

    def remove_order(self, order):
        if order in self.orders:
            self.orders.remove(order)

c1 = Customer_afterRF('xiaoming1')
c2 = Customer_afterRF('xiaoming2')
c3 = Customer_afterRF('xiaoming3')
d1 = Order_afterRF([c1, c2, c3])
for customer in d1.customers:
    print(customer.name)
