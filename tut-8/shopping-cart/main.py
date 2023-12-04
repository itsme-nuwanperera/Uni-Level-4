OPERATIONS = ["quit", "add", "remove", "show", "clear"]


class ShoppingCart:
    __items: list[str]

    def __init__(self):
        self.__items = []

    def show_cart(self):
        
        """
        This returns items in the cart
        """
        return self.__items

    def add_item(self, item: str):
        """
        This method add given item into cart
        """
        self.__items.append(str(item))

    def remove_item(self, item: str):
        """
        This method remove item if its available in the cart and return bool 
        """
        if item not in self.__items:
            return True
        self.__items.remove(item)
        return False

    def clear_cart(self):
        """
        This method reset the cart
        """
        self.__items.clear()


def ask_operarion():
    """
    This function ask for the operation from user and then if its valid, return, else retry for get valid input
    """
    operation = input(f'{"/ ".join(OPERATIONS)} : ').lower()
    if operation not in OPERATIONS:
        print("Not a valid operation!\n")
        return ask_operarion()
    return operation


def get_item_name(operation: str):
    """
    This function use for get item name from user for add or remove, and return name
    """
    item_name = input(f"What would you like to {operation}?: ").title()
    return item_name


def main():
    operation = ask_operarion()
    if operation == "quit":
        print("Thanks for using Shopping Cart!")
        exit()

    elif operation == "add":
        item = get_item_name(operation)
        cart.add_item(item)
        print()

    elif operation == "remove":
        (done) = True
        while done:
            item = get_item_name(operation)
            (done) = cart.remove_item(item)
            print(f"{item} is successfully removed from cart!") if (
                not done
            ) else print(f"{item} is not in cart!")

    elif operation == "show":
        items = cart.show_cart()
        if (items):
            print(f"Items in cart:\n{', '.join(items)}")

        else:
            print("No items in the cart.")

    else:
        cart.clear_cart()
        print("Cart cleard!")

    return main()


cart = ShoppingCart()
print("Shopping cart!")
main()
