import json
import os.path

def init():
    """ Initialize the datastorage module.
    """
    _load_items()


def _load_items():
    """ Load the list of inventory items from disk.
    """
    global _items

    if os.path.exists("items.json"):
        f = open("items.json", "r")
        _items = json.loads(f.read())
        f.close()
    else:
        _items = []


def set_products(products):
    """ Set the (currently hardwired) list of inventory products.

        Each item in the 'products' list should be a (code, description,
        desired_number) tuple, where 'code is a code identifying the product,
        'description' is a string describing that product so the user can
        identify it, and 'desired_number' is the desired number of items that
        you want to keep in the inventory.
    """
    global _products
    _products = products

def set_locations(locations):
    """ Set the (currently hardwired) list of inventory locations.

        Each item in the 'locations' list should be a (code, description)
        tuple, where 'code is the code for an inventory location, and
        'description' is a string describing that location so that the user
        knows where it is.
    """
    global _locations
    _locations = locations