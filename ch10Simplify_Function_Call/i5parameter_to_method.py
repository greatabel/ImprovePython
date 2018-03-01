from mycolor import show

def get_discount_level(quantity):
    if quantity > 100:
        return 2
    else:
        return 1

def discounted_price_old(base_price, discount_level):
    if discount_level == 2:
        return base_price * 0.1
    else:
        return base_price * 0.05

quantity = 1000
item_price = 9.8
base_price = quantity * item_price
discounted_level = get_discount_level(quantity)
final_price = discounted_price_old(base_price, discounted_level)
print('final_price=', show(final_price))


print('-------------改造开始-----------------')
def discounted_price(base_price):
    discount_level = get_discount_level(quantity)
    if discount_level == 2:
        return base_price * 0.1
    else:
        return base_price * 0.05

final_price1 = discounted_price(base_price)
print(show(final_price1, 'red'))