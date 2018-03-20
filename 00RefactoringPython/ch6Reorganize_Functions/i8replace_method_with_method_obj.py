from termcolor import colored
from myfinal import MyPyFinal


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])

class Account:
    def delta(self):
        return 100
    def gamma(self, input_val, quantity, year_to_date):
        
        import_val1 = (input_val * quantity) + self.delta()
        import_val2 = (input_val * year_to_date) + 100
        if year_to_date - import_val1 > 100:
            import_val2 -= 20
        import_val3 = import_val2 * 7
        return import_val3 - 2 * import_val1

a = Account().gamma(200, 100, 2017)
print('old way which need to refactory:', show(a))


class Gamma:
    def __init__(self, input_val, quantity, year_to_date):
        self.input_val = input_val
        self.quantity = quantity
        self.year_to_date = year_to_date
        self.import_val1 = None
        self.import_val2 = None
        self.import_val3 = None

    def compute(self, account):
        def import_thing():
            if self.year_to_date - self.import_val1 > 100:
                self.import_val2 -= 20
                
        self.import_val1 = (self.input_val * self.quantity) +account.delta()
        self.import_val2 = (self.input_val * self.year_to_date) + 100
        import_thing()
        self.import_val3 = self.import_val2 * 7
        return self.import_val3 - 2 * self.import_val1

class Account_after_Refactory:
    def delta(self):
        return 100
    def gamma(self, input_val, quantity, year_to_date):
        return Gamma(input_val, quantity, year_to_date).compute(Account_after_Refactory())

t_after = Account_after_Refactory().gamma(200, 100, 2017)
print('the way which after refactory:', show(t_after, 'red'))
