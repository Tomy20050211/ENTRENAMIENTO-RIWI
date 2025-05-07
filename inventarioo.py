# Inventory dictionary to store products
inventory = {}

# Function to display the main menu
def display_menu():
    print("________________________________________________")
    print("---BRII BRII WAREHOUSE---")
    print("________________________________________________")
    print("--- MENU ---")
    print("1. Add products")
    print("2. Remove products")
    print("3. View products")
    print("4. Calculate total inventory value")
    print("5. Exit")
    print("________________________________________________")

# Function to add or update a product
def add_product():
    print("________________________________________________")
    print("---ADD PRODUCT---")
    name = input("---What product would you like to store?\n").strip()
    if name in inventory:
        print(f"---Product '{name}' already exists. Updating its details.")
    try:
        price = float(input("---Enter a price for the product:\n"))
        units = int(input("---Enter the units of the product:\n"))
        inventory[name] = {"price": price, "Units": units}
        print(f"---Product '{name}' successfully added/updated.\n")
    except ValueError:
        print("---Invalid input. Price must be a number and units must be an integer.\n")

# Function to remove a product
def remove_product():
    print("________________________________________________")
    print("---REMOVE PRODUCT---")
    product_to_remove = input("---Which product would you like to remove?\n").strip()
    if product_to_remove in inventory:
        inventory.pop(product_to_remove)
        print(f"---Product '{product_to_remove}' removed.\n")
    else:
        print(f"---Product '{product_to_remove}' does not exist in the inventory.\n")

# Function to view all products
def view_products():
    print("________________________________________________")
    print("---VIEW PRODUCTS---")
    if inventory:
        for product, details in inventory.items():
            print(f"Product: {product}, Price: ${details['price']}, Units: {details['Units']}")
    else:
        print("---The inventory is empty.\n")

# Function to calculate total inventory value
def calculate_total_value():
    print("________________________________________________")
    print("---CALCULATE TOTAL INVENTORY VALUE---")
    total_value = sum(details['price'] * details['Units'] for details in inventory.values())
    print(f"---The total inventory value is: ${total_value:.2f}\n")

# Main program loop
def main():
    continue_program = True
    while continue_program:
        display_menu()
        try:
            selected_option = int(input("\n---SELECT AN OPTION: "))
            if selected_option == 1:
                add_product()
            elif selected_option == 2:
                remove_product()
            elif selected_option == 3:
                view_products()
            elif selected_option == 4:
                calculate_total_value()
            elif selected_option == 5:
                print("---Exiting the program. Goodbye!")
                continue_program = False
            else:
                print("---Invalid option. Please select a valid option.\n")
        except ValueError:
            print("---Invalid input. Please enter a number.\n")

# Run the program
if __name__ == "__main__":
    main()
