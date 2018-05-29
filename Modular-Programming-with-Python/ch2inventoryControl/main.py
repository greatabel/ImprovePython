import datastorage

def main():
    datastorage.init()

    datastorage.set_products([
    ("SKU123", "4 mm flat-head wood screw",        50),
    ("SKU145", "6 mm flat-head wood screw",        50),
    ("SKU167", "4 mm countersunk head wood screw", 10),
    ("SKU169", "6 mm countersunk head wood screw", 10),
    ("SKU172", "4 mm metal self-tapping screw",    20),
    ("SKU185", "8 mm metal self-tapping screw",    20),
    ])