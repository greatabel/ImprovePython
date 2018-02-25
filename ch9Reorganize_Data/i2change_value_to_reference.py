from mycolor import show


class Order:
    def __init__(self, customer):
        self.customer = customer

class Customer:
    def __init__(self, name):
        self.name = name

d0 = Order(Customer('xiaoming1'))

print(show(d0.customer.name))

c0 = Customer('c')
c1 = Customer('c')
print( c0 == c1)


class Customer_afterRF:
    instance = None

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_instnace(name):
        if Customer_afterRF.instance is None:
            Customer_afterRF.instance = Customer_afterRF(name)
        return Customer_afterRF.instance

c2 = Customer_afterRF.get_instnace('c')
c3 = Customer_afterRF.get_instnace('c')
print(c2 == c3)
print(id(c2), id(c3))