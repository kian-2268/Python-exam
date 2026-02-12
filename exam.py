class Item:
    def __init__(self):
        # Dictionary to store items
        self.inventory = {}

    def add_item(self):
        try:
            name = input("Enter item name: ").strip()

            if name in self.inventory:
                print("Item already exists! Use update option instead.")
                return

            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))

            if quantity < 0 or price < 0:
                print("Quantity and price must not be negative.")
                return

            self.inventory[name] = {
                "quantity": quantity,
                "price": price
            }

            print("Item added successfully!\n")

        except ValueError:
            print("Invalid input! Quantity must be an integer and price must be a number.\n")

    def update_quantity(self):
        try:
            name = input("Enter item name to update: ").strip()

            if name not in self.inventory:
                print("Item not found!\n")
                return

            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.\n")
                return

            self.inventory[name]["quantity"] = quantity
            print("Quantity updated successfully!\n")

        except ValueError:
            print("Invalid input! Quantity must be an integer.\n")

    def display_items(self):
        if not self.inventory:
            print("Inventory is empty.\n")
            return

        print("\n------ INVENTORY LIST ------")
        for name, details in self.inventory.items():
            quantity = details["quantity"]
            price = details["price"]
            total_price = quantity * price

            print(f"Item: {name}")
            print(f"Quantity: {quantity}")
            print(f"Price: {price}")
            print(f"Total Value: {total_price}")
            print("----------------------------")
        print()

    def calculate_total_inventory_value(self):
        total_value = 0

        for details in self.inventory.values():
            total_value += details["quantity"] * details["price"]

        print(f"\nTotal Inventory Value: {total_value}\n")


# Main Program
def main():
    shop = Item()

    while True:
        print("=== INVENTORY MANAGEMENT SYSTEM ===")
        print("1. Add Item")
        print("2. Update Quantity")
        print("3. Display Items")
        print("4. Calculate Total Inventory Value")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            shop.add_item()
        elif choice == "2":
            shop.update_quantity()
        elif choice == "3":
            shop.display_items()
        elif choice == "4":
            shop.calculate_total_inventory_value()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please select 1-5.\n")


if __name__ == "__main__":
    main()
