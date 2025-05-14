
inventory = {}

def display_menu():
    print("________________________________________________")
    print("---BRII BRII WAREHOUSE---")
    print("________________________________________________")
    print("--- MENU ---")
    print("1. Add products")
    print("2. Remove products")
    print("3. View products")
    print("4. Calculate total inventory value")
    print("5. Change product price")
    print("6. Search product")
    print("7. Exit")
    print("________________________________________________")

#Function to add or update a product
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

#Function to remove a product
def remove_product():
    print("________________________________________________")
    print("---REMOVE PRODUCT---")
    product_to_remove = input("---Which product would you like to remove?\n").strip()
    if product_to_remove in inventory:
        inventory.pop(product_to_remove)
        print(f"---Product '{product_to_remove}' removed.\n")
    else:
        print(f"---Product '{product_to_remove}' does not exist in the inventory.\n")

#Function to view all products
def view_products():
    print("________________________________________________")
    print("---VIEW PRODUCTS---")
    if inventory:
        for product, details in inventory.items():
            print(f"Product: {product}, Price: ${details['price']}, Units: {details['Units']}")
    else:
        print("---The inventory is empty.\n")

#Function to calculate total inventory value
def calculate_total_value():
    print("________________________________________________")
    print("---CALCULATE TOTAL INVENTORY VALUE---")
    total_value = sum(details['price'] * details['Units'] for details in inventory.values())
    print(f"---The total inventory value is: ${total_value:.2f}\n")

#Function to change product price
def change_product_price():
    print("________________________________________________")
    print("---CHANGE PRODUCT PRICE---")
    product_to_change = input("---Which product would you like to change the price?\n").strip()
    if product_to_change in inventory:
        try:
            new_price = float(input("---Enter the new price for the product:\n"))
            inventory[product_to_change]['price'] = new_price
            print(f"---Product '{product_to_change}' price changed to ${new_price:.2f}.\n")
        except ValueError:
            print("---Invalid input. Price must be a number.\n")
    else:
        print(f"---Product '{product_to_change}' does not exist in the inventory.\n")

#Function to search product
def search_product():
    print("________________________________________________")
    print("---SEARCH PRODUCT---")
    product_to_search = input("---Which product would you like to search?\n").strip()
    if product_to_search in inventory:
        print(f"---Product '{product_to_search}' found.")
        print(f"Product: {product_to_search}, Price: ${inventory[product_to_search]['price']}, Units: {inventory[product_to_search]['Units']}\n")
    else:
        print(f"---Product '{product_to_search}' does not exist in the inventory.\n")

#Main program loop
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
                change_product_price()
            elif selected_option == 6:
                search_product()
            elif selected_option == 7:
                print("---Exiting the program. Goodbye!")
                continue_program = False
            else:
                print("---Invalid option. Please select a valid option.\n")
        except ValueError:
            print("---Invalid input. Please enter a number.\n")

#Run the program
if __name__ == "__main__":
    main()
