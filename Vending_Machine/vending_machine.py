"""
vending_machine.py
Model class for a Vending Machine.

This file contains the VendingMachine class, which tracks products,
credit, revenue, and supports vending operations. The model never
interacts directly with the user.
"""


class InvalidProductError(Exception):
    """Raised when a user selects a product number that does not exist."""
    pass

class OutOfStockError(Exception):
    """Raised when the selected product has quantity 0."""
    pass

class InsufficientCreditError(Exception):
    """Raised when the user does not have enough credit to purchase."""
    pass


class VendingMachine:
    """Represents a vending machine storing multiple products."""

    # Valid money accepted by the vending machine
    VALID_DENOMINATIONS = [0.05, 0.10, 0.25, 1.00, 2.00, 5.00, 10.00, 20.00]

    # Initialization
    def __init__(self, products):
        """
        Initializes the Vending Machine.

        :param products: list of [name, quantity, price]
        """
        self.__products = products

        # internal state
        self.__credit = 0
        self.__revenue = 0


    ## Getters
    def get_credit(self):
        """Returns the current credit in the machine."""
        return self.__credit

    def get_revenue(self):
        """Returns the total revenue collected."""
        return self.__revenue

    def get_products(self):
        """Returns a copy of the product list (read-only external use)."""
        return self.__products


    ## Vending Machine Operations
    def credit_amount(self, amount):
        """
        Attempts to add credit to the machine.

        :param amount: float – amount inserted
        :return: True if valid denomination, False otherwise
        """

        # Check if amount is valid
        if amount in VendingMachine.VALID_DENOMINATIONS:

            # Add to credit
            self.__credit += amount
            return True
        else:
            return False


    # Vend a product
    def vend_product(self, product_number):
        """
        Attempts to vend a product.

        :param product_number: int (1-based index)
        :return: product name on success
        :raises InvalidProductError, OutOfStockError, InsufficientCreditError
        """

        # Convert to 0-based index
        index = product_number - 1

        # Validate product number
        if index < 0 or index >= len(self.__products):

            # Invalid product number
            raise InvalidProductError("Invalid product number.")

        # Get the product
        product = self.__products[index]

        # Unpack product details
        name, quantity, price = product

        # Check stock
        if quantity == 0:

            # Out of stock
            raise OutOfStockError("Product is out of stock.")

        # Check credit
        if self.__credit < price:

            # Not enough credit
            raise InsufficientCreditError("Not enough credit.")

        # Vend the product
        product[1] -= 1

        # Update revenue and credit
        self.__revenue += price
        self.__credit -= price

        return name

    # Refund all credit
    def refund(self):
        """
        Returns all credit to the user and resets credit to 0.
        """

        # Store refunded amount
        refunded_amount = self.__credit

        # Reset credit
        self.__credit = 0
        return refunded_amount


    # String representation
    def __str__(self):

        # Build string representation
        result = "Vending Machine Products:\n"

        # List products
        for i in range(len(self.__products)):

            # Get product details
            product = self.__products[i]

            # Append product info
            result += f"{i + 1}. {product[0]} - Quantity: {product[1]:.2f}, Price: ${product[2]}\n"

        # Append credit and revenue info
        result += f"Current Credit: ${self.__credit:.2f}\n"
        result += f"Total Revenue: ${self.__revenue:.2f}\n"

        return result


