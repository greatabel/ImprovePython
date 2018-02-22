# python 没有final， 自己造一个只读的
class MyPyFinal( object ):
    def __init__(self, value):
        self.value= value

    def __str__(self):
        return str(self.value)

    def r(self):
        # return result
        return self.value

    def set(self, value):
        if self.value is not None:
            raise Exception( "Read Only var.")
        self.value= value


def price():
    # price is base price - quantity discount * shipping
    quantity = 510
    item_price = 600

    return quantity * item_price - max(0, quantity - 500) * item_price * 0.05 \
            + min(quantity * item_price * 0.1, 100)

t = price()
print('old way which need to refactory:', t)

print('开始改造ing:')
def price_after_refactory():
    # price is base price - quantity discount * shipping
    quantity = 510
    item_price = 600
    base_price = MyPyFinal(quantity * item_price).r()
    quantity_discount = MyPyFinal(max(0, quantity - 500) * item_price * 0.05).r()
    shipping = MyPyFinal(min(base_price * 0.1, 100)).r()
    return base_price - quantity_discount\
            + shipping

t_after = price_after_refactory()
print('old way which after refactory:', t_after)
