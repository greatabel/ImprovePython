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