class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item, price):
        self.cart.append((item, price))
        print(f"'{item}' has been added to the cart.\n")

    def view_cart(self):
        print("The contents of the shopping cart are:")
        for i, (item, price) in enumerate(self.cart, 1):
            print(f"{i}. {item} - ${price:.2f}")
        print()

    def remove_item(self, index):
        try:
            del self.cart[index - 1]
            print("Item removed.\n")
        except IndexError:
            print("Invalid item number. Item not removed.\n")

    def compute_total(self):
        total = sum(item[1] for item in self.cart)
        print(f"The total price of the items in the shopping cart is ${total:.2f}\n")

def main():
    cart = ShoppingCart()

    print("Welcome to the Shopping Cart Program!\n")
    while True:
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        action = input("Please enter an action: ")

        if action == '1':
            item = input("What item would you like to add? ")
            price = float(input(f"What is the price of '{item}'? "))
            cart.add_item(item, price)
        elif action == '2':
            cart.view_cart()
        elif action == '3':
            index = int(input("Which item would you like to remove? "))
            cart.remove_item(index)
        elif action == '4':
            cart.compute_total()
        elif action == '5':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()