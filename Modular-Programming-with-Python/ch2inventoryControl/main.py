import datastorage
import userinterface


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


    datastorage.set_locations([
        ("S1A1", "Shelf 1, Aisle 1"),
        ("S2A1", "Shelf 2, Aisle 1"),
        ("S3A1", "Shelf 3, Aisle 1"),
        ("S1A2", "Shelf 1, Aisle 2"),
        ("S2A2", "Shelf 2, Aisle 2"),
        ("S3A2", "Shelf 3, Aisle 2"),
        ("BIN1", "Storage Bin 1"),
        ("BIN2", "Storage Bin 2"),
    ])

    while True:
        action = userinterface.prompt_for_action()
        if action == "QUIT":
            break

if __name__ == "__main__":
    main()