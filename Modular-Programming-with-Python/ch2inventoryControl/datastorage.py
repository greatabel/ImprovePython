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