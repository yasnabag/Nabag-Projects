# Name: Yaseen Nabag
# Date: 2025-10-05
# Vending Machine Simulation
# File Name : break_room.py
# Description: This program simulates two vending machines allowing users to view products, insert money, purchase products, and return change.


# Import the VendingMachine class and exceptions
from vending_machine import (
    VendingMachine,
    InvalidProductError,
    OutOfStockError,
    InsufficientCreditError
)


# Print the program signature
def print_signature():
    print('''

Name: Yaseen Nabag
_______________________________________________________________________
''')


# display the status of both vending machines`
def display_machines(vm1, vm2):
    """Prints the status of both vending machines."""
    print("\n----------------------")
    print("Vending Machine 1:")
    print("----------------------\n")
    print(vm1)
    print("----------------------")
    print("Vending Machine 2:")
    print("----------------------\n")
    print(vm2)
    print("______________________")
    print()


# Adds money to a vending machine
def handle_add_money(vm):
    """Handles inserting credit into a machine."""
    try:
        amount = float(input("Enter amount to insert: "))
        if vm.credit_amount(amount):
            print(f"Inserted ${amount:.2f}.")
        else:
            print("Invalid denomination.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")


# Handles purchasing a product from a vending machine
def handle_purchase(vm):
    """Handles vending with exceptions."""

    # Display products
    print("\nProducts:")
    try:
        num = int(input("Enter product number: "))

        # Attempt to vend the product
        product_name = vm.vend_product(num)

        print(f"You got {product_name}!")

    except ValueError:
        print("Product number must be a number.")

    except InvalidProductError:
        print("Invalid product number.")

    except OutOfStockError:
        print("Sorry, that product is out of stock.")

    except InsufficientCreditError:
        print("Not enough credit. Insert more money first.")


# Handles refunding credit from a vending machine
def handle_refund(vm):
    """Handles refunding all credit."""

    # Refund the credit
    refunded = vm.refund()

    print(f"Refunded ${refunded:.2f}.")


# Allows user to choose a vending machine
def choose_machine(vm1, vm2):
    """Returns the chosen machine object."""

    # Prompt user for choice
    try:
        choice = int(input("Select Vending Machine (1 or 2): "))
        if choice == 1:
            return vm1
        elif choice == 2:
            return vm2
        else:
            print("Invalid choice.")
            return None

    # Handle non-integer input
    except ValueError:
        print("Enter a number (1 or 2).")
        return None


# Main menu loop
def run(vm1, vm2):
    """Main menu loop."""

    # while loop for menu
    while True:

        display_machines(vm1, vm2)

        print("1. Add Money")
        print("2. Purchase Product")
        print("3. Return Change")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            machine = choose_machine(vm1, vm2)

            if machine:


                handle_add_money(machine)

        elif choice == "2":
            machine = choose_machine(vm1, vm2)

            if machine:
                handle_purchase(machine)

        elif choice == "3":
            machine = choose_machine(vm1, vm2)

            if machine:
                handle_refund(machine)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")


# Main function to create vending machines and start the program
def main():
    """Creates machines and starts program."""

    # Vending 1 machine instances : name, quantity, price
    vm1 = VendingMachine([
        ["Coke", 10, 3.50],
        ["Sprite", 8, 3.50],
        ["Chips", 23, 2.25],
        ["Candy", 15, 1.75],
        ["Water", 20, 2.00]
    ])

    # Vending 2 machine instances : name, quantity, price
    vm2 = VendingMachine([
        ["Juice", 12, 4.00],
        ["Gum", 30, 1.00],
        ["Cookies", 18, 2.50],
        ["Nuts", 25, 3.00],
        ["Tea", 10, 2.75],
    ])


    # Run the main menu loop
    run(vm1, vm2)


# Main program entry point
if __name__ == "__main__":
    print_signature()
    main()
