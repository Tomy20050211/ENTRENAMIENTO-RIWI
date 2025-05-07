# Empty dictionary to store products
# Each product will be a key, and the value will be another dictionary with 'price' and 'Units'
inventory = {}

# Control variable to keep the menu active
continue_program = True

# Main program loop
while continue_program:
    # Display menu options
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

    try:
        # Ask the user to choose a menu option
        selected_option = int(input("\n---SELECT AN OPTION: "))

        # Option 1: Add a product to the inventory
        if selected_option == 1:
            print("________________________________________________")
            print("---ADD PRODUCT---")
            name = input("---What product would you like to store?\n").strip()  # Product name
            if name in inventory:
                print(f"---Product '{name}' already exists. Updating its details.")
            price = float(input("---Enter a price for the product:\n"))  # Price as a float
            Units = int(input("---Enter the Units of the product:\n"))  # Units as an integer
            # Store the product in the inventory as a nested dictionary
            inventory[name] = {"price": price, "Units": Units}
            print(f"Product '{name}' successfully added/updated.\n")

        # Option 2: Remove a product from the inventory
        elif selected_option == 2:
            print("________________________________________________")
            print("---REMOVE PRODUCT---")
            product_to_remove = input("---Which product would you like to remove?\n").strip()  # Product to remove
            # Check if the product exists
            if product_to_remove in inventory:
                inventory.pop(product_to_remove)  # Remove the product
                print(f"---Product '{product_to_remove}' removed.\n")
            else:
                print(f"---Product '{product_to_remove}' does not exist in the inventory.\n")

        # Option 3: View products in the inventory
        elif selected_option == 3:
            print("________________________________________________")
            print("---VIEW PRODUCTS---")
            if inventory:
                for product, details in inventory.items():
                    print(f"Product: {product}, Price: {details['price']}, Units: {details['Units']}")
            else:
                print("---The inventory is empty.\n")

        # Option 4: Calculate total inventory value
        elif selected_option == 4:
            print("________________________________________________")
            print("---CALCULATE TOTAL INVENTORY VALUE---")
            total_value = sum(details['price'] * details['Units'] for details in inventory.values())
            print(f"---The total inventory value is: ${total_value:.2f}\n")

        # Option 5: Exit the program
        elif selected_option == 5:
            print("---Exiting the program. Goodbye!")
            continue_program = False

        # Invalid option
        else:
            print("---Invalid option. Please select a valid option.\n")

    except ValueError:
        print("---Invalid input. Please enter a number.\n")
