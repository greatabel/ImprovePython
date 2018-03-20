class Order:
    def __init__(self, price=0):
        self.price = price

    def base_price(self):
        return self.price

def demo():
    an_order = Order()
    base_price = an_order.base_price()
    return base_price > 1000


print('一个临时变量，只被简单表达赋值一次，而它妨碍了其他重构\
    将所有对该变量的引用作用，替换为对它赋值的表达式自身')

def demo_refactory():
    an_order = Order()
    return an_order.base_price() > 1000


