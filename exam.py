class Item:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.items = []

    def add_item(self):
        self.items.append(self.item_name, self.quantity, self.price)

    def update_quantity(self):
        quantity = int(input("Enter updated quantity: "))
        self.items[quantity] = quantity

    def display_items(self):
        print("\nItems In The Inventory:")
        for i in self.items in enumerate:
            print(self.items[i])
    
    def calculate_total_inventory_value(self):
        result = self.quantity * self.price
        print("Total inventory value: ", result)
        self.items.append(result)

def Main():
    try:
        item_name = input("Enter item name: ")
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
        except ValueError:
            print("Please enter numerical values only.")

        item = Item(item_name, quantity, price)

        while True:
            print("\nWelcome to Inventory Management System!")
            print("Please choose an action: ")
            print("[1] Add item")
            print("[2] Update quantity")
            print("[3] Display items")
            print("[4] Calculate total inventory value")
            print("[5] Exit")

            choice = input("Please choose a number: ")

            if choice == "1":
                item.add_item()
            elif choice == "2":
                item.update_quantity()
            elif choice == "3":
                item.display_items()
            elif choice == "4":
                item.calculate_total_inventory_value()
            elif choice == "5":
                print("Thank you for using our system! Have a nice day!")
            else:
                print("Invalid input. Please choose only from 1 to 5.")

    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    Main()