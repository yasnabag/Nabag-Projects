# Name: Yaseen Nabag
# Bank Simulator ATM
# This program creates an interactive ATM using Turtle.
# Users can create accounts, deposit/withdraw money, check balances,
# view transactions, and apply interest or fees.

import turtle
import csv
import random
from datetime import datetime


# ============================================================
# ACCOUNT CLASS
# ============================================================

# Parent class that stores the information and behaviours
# shared by all bank accounts.
class Account:

    # Class variable that keeps track of how many accounts
    # have been created.
    total_accounts = 0

    # Default interest rate.
    interest_rate = 0.015


    # Static method used to generate an 18-digit account number.
    # It does not require an Account object to be created first.
    @staticmethod
    def generate_account_number():

        # Generate 18 random digits, convert each digit to a String,
        # and join them together into one account number.
        return ''.join([str(random.randint(0, 9)) for _ in range(18)])


    # Constructor for an Account object.
    # Takes an account number and an optional starting balance.
    def __init__(self, account_number, initial_balance=0.0):

        # Private instance variable that stores the account number.
        self.__account_number = account_number

        # Store the initial balance.
        # max() prevents the account from starting with a negative balance.
        self.__balance = max(0.0, float(initial_balance))

        # List used to store this account's transaction history.
        self.__transactions = []

        # Increase the total number of accounts.
        Account.total_accounts += 1

        # Record the creation of the account as the first transaction.
        self.__log_transaction(
            f"Account opened with initial balance: ${initial_balance:.2f}"
        )


    # Deposit money into the account.
    def deposit(self, amount):

        try:

            # Convert the entered amount into a float.
            amount = float(amount)

            # A deposit must be greater than zero.
            if amount <= 0:
                return False

            # Add the deposit to the current balance.
            self.__balance += amount

            # Record the deposit in the transaction history.
            self.__log_transaction(f"Deposit: +${amount:.2f}")

            # Return True to indicate the deposit was successful.
            return True

        # If the amount cannot be converted to a number,
        # the deposit fails.
        except ValueError:
            return False


    # Withdraw money from the account.
    def withdraw(self, amount):

        try:

            # Convert the entered amount into a float.
            amount = float(amount)

            # Withdrawal amounts must be positive.
            if amount <= 0:
                return False

            # Do not allow the user to withdraw more money
            # than they currently have.
            if amount > self.__balance:
                return False

            # Subtract the withdrawal from the balance.
            self.__balance -= amount

            # Record the withdrawal.
            self.__log_transaction(f"Withdrawal: -${amount:.2f}")

            return True

        # Return False if an invalid amount is provided.
        except ValueError:
            return False


    # Apply the account's interest rate to its current balance.
    def apply_interest(self):

        # Calculate the amount of interest earned.
        interest = self.__balance * self.interest_rate

        # Only add interest if the calculated amount is positive.
        if interest > 0:
            self.deposit(interest)


    # Private helper method used to record transactions.
    def __log_transaction(self, message):

        # Get the current date and time.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create the transaction message.
        log_entry = (
            f"{timestamp} | "
            f"Account #{self.__account_number} | "
            f"{message}"
        )

        # Store the transaction inside the account object's list.
        self.__transactions.append(log_entry)

        try:

            # Open the transaction log in append mode so old
            # transactions are not deleted.
            with open("transactions.log", "a") as f:

                # Write the new transaction to the file.
                f.write(log_entry + "\n")

        # Display a warning if the transaction file cannot be written.
        except IOError as e:
            print(f"Warning: Could not write transaction log: {e}")


    # Getter method for the account balance.
    def get_balance(self):
        return self.__balance


    # Getter method for the account number.
    def get_account_number(self):
        return self.__account_number


    # Getter method for the transaction history.
    def get_transactions(self):

        # Return a copy so outside code does not directly modify
        # the original transaction list.
        return self.__transactions.copy()


    # Defines how an Account object is displayed as a String.
    def __str__(self):

        return (
            f"Account #{self.__account_number} | "
            f"Balance: ${self.__balance:.2f}"
        )


    # Save all existing accounts into a CSV file.
    @classmethod
    def save_to_file(cls, accounts, filename="accounts.csv"):

        try:

            # Open the CSV file in write mode.
            with open(filename, "w", newline="") as f:

                # Create a CSV writer.
                writer = csv.writer(f)

                # Write the column headings.
                writer.writerow(
                    ["account_number", "balance", "account_type"]
                )

                # Go through every account in the accounts list.
                for acc in accounts:

                    # Determine which subclass the account belongs to.
                    if isinstance(acc, SavingsAccount):
                        acc_type = "Savings"
                    else:
                        acc_type = "Checking"

                    # Save the account's information as one row.
                    writer.writerow([
                        acc.get_account_number(),
                        acc.get_balance(),
                        acc_type
                    ])

        # Display an error if the file cannot be saved.
        except IOError as e:
            print(f"Error saving accounts: {e}")


    # Load previously saved accounts from the CSV file.
    @classmethod
    def load_from_file(cls, filename="accounts.csv"):

        # Start with an empty list.
        accounts = []

        try:

            # Open the saved account file.
            with open(filename, "r") as f:

                # DictReader allows values to be accessed using
                # column names such as "account_number".
                reader = csv.DictReader(f)

                # Read each saved account.
                for row in reader:

                    try:

                        # Retrieve the saved account information.
                        acc_num = row["account_number"]
                        balance = float(row["balance"])
                        acc_type = row["account_type"]

                        # Recreate the correct type of account.
                        if acc_type == "Savings":

                            account = SavingsAccount(
                                acc_num,
                                balance
                            )

                        else:

                            account = CheckingAccount(
                                acc_num,
                                balance
                            )

                        # Add the recreated account to the list.
                        accounts.append(account)

                    # Ignore rows containing invalid information.
                    except (KeyError, ValueError):
                        pass

        # If the program has never saved accounts before,
        # there may not be an accounts.csv file yet.
        except FileNotFoundError:
            pass

        # Handle other file-related errors.
        except IOError as e:
            print(f"Could not load accounts: {e}")

        # Return all loaded accounts.
        return accounts


# ============================================================
# SAVINGS ACCOUNT CLASS
# ============================================================

# SavingsAccount inherits the variables and methods from Account.
class SavingsAccount(Account):

    # Constructor for a savings account.
    def __init__(self, account_number, initial_balance=0.0):

        # Call the constructor of the parent Account class.
        super().__init__(account_number, initial_balance)

        # Savings accounts use a 2.5% interest rate.
        self.interest_rate = 0.025


    # Override the Account apply_interest() method.
    def apply_interest(self):

        # Calculate interest using the savings interest rate.
        interest = self.get_balance() * self.interest_rate

        # Add the interest if it is greater than zero.
        if interest > 0:
            self.deposit(interest)


# ============================================================
# CHECKING ACCOUNT CLASS
# ============================================================

# CheckingAccount also inherits from Account.
class CheckingAccount(Account):

    # Monthly fee shared by checking accounts.
    monthly_fee = 15.00


    # Constructor for a checking account.
    def __init__(self, account_number, initial_balance=0.0):

        # Call the parent Account constructor.
        super().__init__(account_number, initial_balance)


    # Apply the monthly checking account fee.
    def apply_monthly_fee(self):

        # Only charge the fee if the account has enough money.
        if self.get_balance() >= self.monthly_fee:

            self.withdraw(self.monthly_fee)


# ============================================================
# TURTLE ATM SETUP
# ============================================================

# Set the size and title of the ATM window.
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Bank Simulator ATM"


# Create the Turtle window.
screen = turtle.Screen()

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title(WINDOW_TITLE)
screen.bgcolor("black")


# Load any accounts that were previously saved.
accounts = Account.load_from_file()


# Create a Turtle object used to draw the ATM interface.
drawer = turtle.Turtle()

# Hide the Turtle arrow because we only need its drawing.
drawer.hideturtle()

# Use the fastest drawing speed.
drawer.speed(0)


# Create another Turtle object specifically for displaying messages.
display = turtle.Turtle()

display.hideturtle()
display.penup()


# ============================================================
# BUTTON CLASS
# ============================================================

# Represents one clickable button on the ATM screen.
class Button:

    # Store the button's location, size, text, and function.
    def __init__(self, x, y, width, height, text, function):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        # Store the function that should run when this button is clicked.
        self.function = function

        # Draw the button immediately after it is created.
        self.draw()


    # Draw the button on the Turtle window.
    def draw(self):

        drawer.penup()

        # Move to the bottom-left corner of the button.
        drawer.goto(
            self.x - self.width / 2,
            self.y - self.height / 2
        )

        drawer.setheading(0)

        drawer.color("white")
        drawer.pensize(2)

        drawer.pendown()

        # Draw the four sides of the rectangle.
        for side in range(2):

            drawer.forward(self.width)
            drawer.left(90)

            drawer.forward(self.height)
            drawer.left(90)

        drawer.penup()

        # Move to approximately the center of the button.
        drawer.goto(
            self.x,
            self.y - 10
        )

        drawer.color("white")

        # Write the button's label.
        drawer.write(
            self.text,
            align="center",
            font=("Arial", 14, "bold")
        )


    # Determine whether a mouse click occurred inside this button.
    def clicked(self, x, y):

        return (
            self.x - self.width / 2 <= x <= self.x + self.width / 2
            and
            self.y - self.height / 2 <= y <= self.y + self.height / 2
        )


# ============================================================
# DISPLAY MESSAGE
# ============================================================

# Display a message near the top of the ATM.
def show_message(message):

    # Remove the previous message.
    display.clear()

    # Move to the message area.
    display.goto(0, 165)

    display.color("lime")

    # Display the new message.
    display.write(
        message,
        align="center",
        font=("Arial", 16, "bold")
    )


# ============================================================
# FIND ACCOUNT
# ============================================================

# Ask the user for an account number and return the matching account.
def find_account():

    # Open a Turtle input box.
    acc_num = screen.textinput(
        "Account Login",
        "Enter your 18-digit account number:"
    )

    # If the user presses Cancel, stop the operation.
    if acc_num is None:
        return None

    # Search through the accounts.
    for account in accounts:

        # Return the account if its number matches.
        if account.get_account_number() == acc_num:
            return account

    # If the loop finishes without finding an account,
    # display an error message.
    show_message("Account not found.")

    return None


# ============================================================
# CREATE ACCOUNT
# ============================================================

# Create either a savings or checking account.
def create_account():

    # Ask which type of account the user wants.
    account_type = screen.textinput(
        "Create Account",
        "Enter S for Savings or C for Checking:"
    )

    # Cancel the operation if the user closes the input box.
    if account_type is None:
        return

    # Convert the answer to uppercase so "s" and "S" both work.
    account_type = account_type.upper()

    # Validate the account type.
    if account_type != "S" and account_type != "C":

        show_message("Invalid account type.")

        return


    # Ask the user for their opening deposit.
    initial_balance = screen.numinput(
        "Initial Deposit",
        "Enter initial deposit (minimum $5):",
        minval=5
    )

    if initial_balance is None:
        return


    # Generate an account number.
    acc_num = Account.generate_account_number()


    # Keep generating numbers until a unique one is found.
    while any(
        acc.get_account_number() == acc_num
        for acc in accounts
    ):

        acc_num = Account.generate_account_number()


    # Create a SavingsAccount if S was selected.
    if account_type == "S":

        account = SavingsAccount(
            acc_num,
            initial_balance
        )

    # Otherwise create a CheckingAccount.
    else:

        account = CheckingAccount(
            acc_num,
            initial_balance
        )


    # Add the new account to the account list.
    accounts.append(account)

    # Save the updated account list.
    Account.save_to_file(accounts)

    # Display the newly generated account number.
    show_message(
        f"Account created! Account #: {acc_num}"
    )


# ============================================================
# CHECK BALANCE
# ============================================================

def check_balance():

    # Ask the user to identify their account.
    account = find_account()

    # Stop if the account could not be found.
    if account is None:
        return

    # Display the account's current balance.
    show_message(
        f"Balance: ${account.get_balance():.2f}"
    )


# ============================================================
# DEPOSIT
# ============================================================

def deposit():

    # Find the account receiving the deposit.
    account = find_account()

    if account is None:
        return


    # Ask how much money the user wants to deposit.
    amount = screen.numinput(
        "Deposit",
        "Enter deposit amount:",
        minval=0.01
    )

    if amount is None:
        return


    # deposit() returns True if the transaction succeeds.
    if account.deposit(amount):

        # Save the updated balance.
        Account.save_to_file(accounts)

        show_message(
            f"Deposit successful! Balance: "
            f"${account.get_balance():.2f}"
        )

    else:

        show_message("Deposit failed.")


# ============================================================
# WITHDRAW
# ============================================================

def withdraw():

    # Find the account making the withdrawal.
    account = find_account()

    if account is None:
        return


    # Ask how much money the user wants to withdraw.
    amount = screen.numinput(
        "Withdraw",
        "Enter withdrawal amount:",
        minval=0.01
    )

    if amount is None:
        return


    # Attempt the withdrawal.
    if account.withdraw(amount):

        # Save the new balance.
        Account.save_to_file(accounts)

        show_message(
            f"Withdrawal successful! Balance: "
            f"${account.get_balance():.2f}"
        )

    else:

        # This can happen if the account does not contain enough money.
        show_message(
            "Withdrawal failed. Check your balance."
        )


# ============================================================
# APPLY INTEREST / FEES
# ============================================================

def interest_or_fee():

    # Find the account.
    account = find_account()

    if account is None:
        return


    # Savings accounts receive interest.
    if isinstance(account, SavingsAccount):

        account.apply_interest()

        show_message(
            f"Interest applied! Balance: "
            f"${account.get_balance():.2f}"
        )

    # Checking accounts receive their monthly fee.
    else:

        account.apply_monthly_fee()

        show_message(
            f"Monthly fee processed. Balance: "
            f"${account.get_balance():.2f}"
        )


    # Save the changed balance.
    Account.save_to_file(accounts)


# ============================================================
# VIEW TRANSACTIONS
# ============================================================

def view_transactions():

    # Find the account whose history should be displayed.
    account = find_account()

    if account is None:
        return


    # Retrieve the account's transactions.
    transactions = account.get_transactions()

    # Remove the previous ATM message.
    display.clear()

    display.goto(0, 190)
    display.color("lime")


    # Check whether the account has any transactions.
    if len(transactions) == 0:

        display.write(
            "No transactions found.",
            align="center",
            font=("Arial", 14, "normal")
        )

        return


    # Starting vertical position for the transaction history.
    y = 190


    # Display only the five most recent transactions.
    for transaction in transactions[-5:]:

        display.goto(0, y)

        display.write(
            transaction,
            align="center",
            font=("Arial", 10, "normal")
        )

        # Move down before displaying the next transaction.
        y -= 25


# ============================================================
# EXIT ATM
# ============================================================

def exit_atm():

    # Save account information before closing the program.
    Account.save_to_file(accounts)

    # Close the Turtle window.
    screen.bye()


# ============================================================
# DRAW ATM TITLE
# ============================================================

drawer.color("white")
drawer.penup()

# Move to the top of the screen.
drawer.goto(0, 250)

# Draw the bank name.
drawer.write(
    "PYTHON BANK",
    align="center",
    font=("Arial", 28, "bold")
)


# Move underneath the bank name.
drawer.goto(0, 215)

drawer.color("lime")

# Draw the ATM title.
drawer.write(
    "ATM",
    align="center",
    font=("Arial", 20, "bold")
)


# ============================================================
# CREATE ATM BUTTONS
# ============================================================

# Create each button and connect it to the function
# that should run when the button is clicked.
buttons = [

    Button(
        -220, 70,
        250, 55,
        "CREATE ACCOUNT",
        create_account
    ),

    Button(
        220, 70,
        250, 55,
        "CHECK BALANCE",
        check_balance
    ),

    Button(
        -220, 0,
        250, 55,
        "DEPOSIT",
        deposit
    ),

    Button(
        220, 0,
        250, 55,
        "WITHDRAW",
        withdraw
    ),

    Button(
        -220, -70,
        250, 55,
        "TRANSACTIONS",
        view_transactions
    ),

    Button(
        220, -70,
        250, 55,
        "INTEREST / FEE",
        interest_or_fee
    ),

    Button(
        0, -160,
        250, 55,
        "EXIT",
        exit_atm
    )
]


# ============================================================
# MOUSE CLICK HANDLER
# ============================================================

# This function receives the x and y coordinates
# whenever the user clicks inside the Turtle window.
def handle_click(x, y):

    # Check every button.
    for button in buttons:

        # Determine whether this button was clicked.
        if button.clicked(x, y):

            # Run the function connected to that button.
            button.function()

            # Stop checking the remaining buttons.
            break


# Tell Turtle to call handle_click() whenever
# the user clicks the screen.
screen.onclick(handle_click)


# Display the starting message.
show_message(
    "Welcome! Please select an option."
)


# Keep the Turtle window open and listening
# for user interactions.
turtle.done()
