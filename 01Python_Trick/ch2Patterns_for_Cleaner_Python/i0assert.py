def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount)) 
    assert 0 <= price <= product['price']
    return price

if __name__ == "__main__":
    shoes = {'name': 'Fancy shoes', 'price': 14900}
    r = apply_discount(shoes, 0.25)
    print(r)
    apply_discount(shoes, 2.0)