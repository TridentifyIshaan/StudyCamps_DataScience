# Menu Item Class

class MenuItem:
    # Initialising
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    # Printing
    def __repr__(self):
        return f"{self.name} ({self.category}): ₹{self.price:.2f}"

# Order Class

class Order:
    order_id_counter = 1

    # Initialising
    def __init__(self, customer):
        self.order_id = Order.order_id_counter
        Order.order_id_counter += 1
        self.customer = customer
        self.list_of_items = []
        self.total_price = 0.0

    # Adding Menu Items
    def add_item(self, menu_item: MenuItem):
        self.list_of_items.append(menu_item)
        self.total_price += menu_item.price

    # Printing
    def __repr__(self):
        items = ', '.join([item.name for item in self.list_of_items])
        return f"Order ID: {self.order_id}, Items: [{items}], Total: ₹{self.total_price:.2f}"

# Customer Class

class Customer:

    # Initialising
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.orders = []

    # Placing Orders 
    def place_order(self, restaurant, list_of_items):
        order = Order(self)
        for item in list_of_items:
            menu_item = restaurant.get_menu_item(item)
            if menu_item:
                order.add_item(menu_item)
        self.orders.append(order)
        restaurant.add_order(order)
        return order
    
    # Printing
    def __repr__(self):
        return f"Customer: {self.name}, Phone: {self.phone_number}, Orders: {len(self.orders)}"

# Restaurant Class

class Restaurant:

    # Initialising
    def __init__(self, name: str):
        self.name = name
        self.menu = []
        self.orders = []

    # Adding New Menu Items
    def add_menu_item(self, menu_item: MenuItem):
        self.menu.append(menu_item)

    # Removing Menu Items
    def remove_menu_item(self, menu_item_name: str):
        self.menu = [item for item in self.menu if item.name != menu_item_name]

    # Getting Orders
    def get_menu_item(self, item_name: str):
        for item in self.menu:
            if item.name == item_name:
                return item
        return None

    # Add New Orders
    def add_order(self, order: Order):
        self.orders.append(order)

    # Calculating Total Sales
    def calculate_total_sales(self):
        return sum(order.total_price for order in self.orders)
    
    # To Display the Menu 
    def display_menu(self):
        if not self.menu:
            print("The menu is currently empty.")
        else:
            print("Menu Items:")
            for item in self.menu:
                print(f" - {item}")

    # Printing
    def __repr__(self):
        return f"Restaurant: {self.name}, Menu Items: {len(self.menu)}, Orders: {len(self.orders)}"

# Main Program

def main():
    restaurant = Restaurant("Gourmet Bistro")

    while True:
        print("\n--- Welcome to Restaurant Ordering System! ---")
        print("1. Add Menu Item")
        print("2. Remove Menu Item")
        print("3. Display Menu")
        print("4. Place Order")
        print("5. View Total Sales")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter the name of the menu item: ")
            price = float(input("Enter the price of the menu item: "))
            category = input("Enter the category of the menu item (e.g., Main Course, Beverage): ")
            menu_item = MenuItem(name, price, category)
            restaurant.add_menu_item(menu_item)
            print(f"Added {menu_item} to the menu.")

        elif choice == '2':
            name = input("Enter the name of the menu item to remove: ")
            restaurant.remove_menu_item(name)
            print(f"Removed {name} from the menu.")

        elif choice == '3':
            restaurant.display_menu()

        elif choice == '4':
            
            customer_name = input("Enter customer name: ")

            while True:
                phone_number = input("Enter customer phone number (10 digits): ")
                if len(phone_number) == 10 and phone_number.isdigit():
                    break
                else:
                    print("Invalid phone number. Please enter a 10-digit phone number.")

            customer = Customer(customer_name, phone_number)

            restaurant.display_menu()
            items = input("Enter the items to order (comma-separated): ").split(",")
            items = [item.strip() for item in items]

            order = customer.place_order(restaurant, items)
            print(f"Order placed successfully: {order}")

        elif choice == '5':
            total_sales = restaurant.calculate_total_sales()
            print(f"Total Sales: ₹{total_sales:.2f}")

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()