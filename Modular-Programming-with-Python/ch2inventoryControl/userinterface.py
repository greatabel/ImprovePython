import datastorage

def prompt_for_action():
    """ Prompt the user to choose an action to perform.

        We return one of the following action codes:

            "QUIT"
            "ADD"
            "REMOVE"
            "INVENTORY_REPORT"
            "REORDER_REPORT"
    """
    while True:
        print()
        print("What would you like to do?")
        print()
        print("  A = add an item to the inventory.")
        print("  R = remove an item from the inventory.")
        print("  C = generate a report of the current inventory levels.")
        print("  O = generate a report of the inventory items to re-order.")
        print("  Q = quit.")
        print()
        action = input("> ").strip().upper()
        if   action == "A": return "ADD"
        elif action == "R": return "REMOVE"
        elif action == "C": return "INVENTORY_REPORT"
        elif action == "O": return "REORDER_REPORT"
        elif action == "Q": return "QUIT"
        else:
            print("Unknown action!")