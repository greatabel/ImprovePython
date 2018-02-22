
def price():
    # price is base price - quantity discount * shipping
    quantity = 10
    item_price = 600

    return quantity * (item_price - max(0, quantity - 500)) * 0.05\
            + min(quantity * item_price * 0.1, 100)

t = price()
print(t)

