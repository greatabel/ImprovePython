from termcolor import colored
from myfinal import MyPyFinal


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])

class Account:

    def gamma(self, input_val, quantity, year_to_date):
        def delta():
            return 100
        import_val1 = (input_val * quantity) + delta()
        import_val2 = (input_val * year_to_date) + 100
        if year_to_date - import_val1 > 100:
            import_val2 -= 20
        import_val3 = import_val2 * 7
        return import_val3 - 2 * import_val1

a = Account().gamma(200, 100, 2017)
print('old way which need to refactory:', show(a))