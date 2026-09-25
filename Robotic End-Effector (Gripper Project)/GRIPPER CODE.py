"""
Authors: Aravinthan Vivekananthan, Chak Pui Sze, Ali Ashmal Molwani, Navid Rouf, Yaseen Nabag

Description: This program describes a fully-implemented package collection system, including user sign up, product look up, physical collection and delivery through interfacing with a Q-Arm, and lastly generating an order receipt and customer summary

"""

# Import needed modules
import bcrypt
import random


def sign_up():
    """
    Sign up new users and update users.csv accordingly, encoding passwords securely
    Parameters: None
    Output: Update users.csv with a  new line of userid,password
    Return: None
    """
    users_file = "users.csv"
    # Open in append mode, a+ allows for reading and writing on the file (creates a new file if it doesnt exist)
    f = open(users_file, 'a+')
    f.seek(0)  # Go to the start of the file
    if not f.readline():  # Check if the file is empty.
        f.write("userid,encrypted_password\n")
    f.close()



    # Repetively query for userid, until unique userid inputted
    while True:
        f_read = open(users_file, 'r')
        # Check if userid already exists by reading the file manually.
        user_exists = False
        userid = input("Enter a new userid: ").strip()

        # check each existing userid against entered userid, to see if chosen userid is already taken
        for line in f_read:
            # Each line is 'userid,hashed_password', this extracts just the userid
            existing_userid = line.strip().split(',')[0]
            if existing_userid == userid:
                user_exists = True
                print(" UserID already exists. Please try another one.")
                break
        f_read.close()
        if user_exists == False:
            break


    # special character in password
    legal_symbols = "!.@#$%^&*()_[]"

    # Repetitively evaluate password and list guidelines
    while True: #ends the code if password does not follow guidelines
        print("Password must be at least 6 characters long and include:")
        print(f"- 1 uppercase letter\n- 1 lowercase letter\n- 1 digit\n- 1 symbol from: {legal_symbols}")
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        password = input("Enter a password: ")

        # iterate and check through each character in password string
        for char in password: #checks to make sure password follows all guidelines
            if 'A' <= char <= 'Z':
                has_upper = True
            elif 'a' <= char <= 'z':
                has_lower = True
            elif '0' <= char <= '9':
                has_digit = True
            elif char in legal_symbols:
                has_symbol = True

        # proceed only if password completes all conditons, otherwise repeat
        if (len(password) >= 6 and has_upper and has_lower and has_digit and has_symbol):
            break

    # Hash the password
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

    #add the new userid and pass to csv file
    f_append = open(users_file, 'a')
    f_append.write(f"{userid},{hashed_pw}\n")
    f_append.close()

    print("Account created successfully!") # positive status message

    return None

def authenticate():
    """
    Authenticate the user, by allowing existing users to sign in or create new userid
    Parameters: None
    Output: Prints a success or failure message, depending on if authentication is successful
    Return: userid (string)
    """

    has_account = input("Do you have an account? (y/n)")
    if has_account.strip().lower() == "n": # remove spaces and case sensitivity from response
        sign_up() # have user create account then return back to authenticate

    # repeat continously until successful login
    while True:
        userid = input("Enter userid: ")
        password = input("Enter password: ")


        f_read = open("users.csv", 'r')


        for row in f_read:
            row = row.strip() # remove newline ("\n") character when reading file

            # Assign database variables of user and pass to check against input
            stored_user = row.split(",")[0]
            stored_password = row.split(",")[1]

            # check passwords next if userid matches
            if userid == stored_user:

                # encode strings before passing into bcrypt.checkpw(), arguments must be bytes
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    # correct userid and password combination
                    print("Login successful!")
                    f_read.close()
                    return userid
                # continue repeating until correct userid and password combination
                else:
                    break

        print("Incorrect userid/password")


def lookup_products(items):
    """
    Look up prices for valid items passed in by the items parameter
    Parameters: items (space-separated string of items to order)
    Output: Display a warning message for invalid items not found
    Return: prods_and_prices (2D list of each product and price)
    """

    # create list of item names and intialize empty list for names and prices
    item_names = items.split()
    prods_and_prices = []

    # open products.csv in read mode
    product_file = open('products.csv', 'r')

    # only certain possible objects, ensure order only contains valid items
    for item_name in item_names:
        if item_name == "Sponge" or item_name == "Bottle" or item_name == "Rook" or item_name == "D12" or item_name == "WitchHat" or item_name == "Bowl":
            product_file.seek(0) # return to top of file

            # iterate through each line in product_file, saving the name and price of each product
            for line in product_file:
                line = line.strip()
                name = line.split(",")[0]
                price = line.split(",")[1]

                # append list of the ordered item name, price
                if name == item_name:
                    # forms a 2D list of form [[item_name,price]..]
                    prods_and_prices.append([item_name,round(float(price),2)])
                    break

        # produce warning for invalid/unavailable item ordered
        else:
            print(f"Warning: \"{item_name}\" not found in \"products.csv\" file.")

    product_file.close()
    return prods_and_prices


def complete_order(userid, product_list):
    """
    Create an organized receipt for the current order, adds a random discount, and updates orders.csv
    Parameters: userid (string), product_list (2D list of each product and price)
    Output: Display order invoice, new line in orders.csv with order information
    Return: None
    """

    # sum pre-tax cost of goods for the order
    subtotal = 0
    for product in range(len(product_list)):
        subtotal += product_list[product][1]

    # calculate random discount, and tax after discount at 13%
    discount_percentage = random.randint(5,50)
    discount = subtotal * (discount_percentage/100)
    new_subtotal = subtotal - discount
    tax = new_subtotal * (13/100)

    # calculate total and round to 2 decimal places
    total = round((tax + new_subtotal),2)

    # form line comma-separated line to write to add to orders.csv
    line = userid + ", " + str(total)

    # append every ordered product in that order to the line
    for product in range(len(product_list)):
        line = line + ", " + product_list[product][0]

    # Write the line to orders.csv and add new line after to set it up for future orders
    file = open("orders.csv", "a")
    file.write(line + "\n")
    file.close()

    # printing order invoice, including layout and customer information
    print("===================================")
    print("             RECEIPT")
    print("===================================")
    print("Customer:", userid)
    print("-----------------------------------")
    print("Items:")

    # save the name and price of each product ordered to format per line in invoice
    for product in range(len(product_list)):
        name = product_list[product][0]
        price = product_list[product][1]

        # Right justify prices like on receipt, left justify product names
        print(f" - {name:<24} ${price:>6.2f}")

    # Format output using column width, to align output to column and right justify prices
    print("-----------------------------------")
    print(f"{'Subtotal:':<15} ${subtotal:>6.2f}")
    print(f"{f'Discount ({discount_percentage}%):':<15} ${discount:>6.2f}")
    print(f"{'Subtotal:':<15} ${new_subtotal:>6.2f}")

    # Allow 6 characters for numbers, leaving space for large numbers and allows alignment like on receipt
    print(f"{f'Tax ({13}%):':<15} ${tax:>6.2f}")
    print(f"{'TOTAL:':<15} ${total:>6.2f}")
    print("===================================")
    print("  Thank you for your purchase!")

    # End receipt by telling user how many orders placed so far
    orders_made = 0

    file = open("orders.csv", "r")
    file.seek(0) # Ensure iteration begins from start of file

    # count number of orders made that originate from the same userid
    for line in file:
        line = line.split(",")
        if line[0] == userid:
            orders_made += 1

    print(f"      {orders_made} orders made so far")

    print("===================================")

def customer_summary(userid):
    """
    Create an organized customer summary, with total spent and total orders, and individual amounts of item ordered, using orders.csv
    Parameters: userid (string)
    Output: Display customer summary
    Return: None
    """

    # intialize important customer statistic variables
    total_orders = 0
    total_spent = 0

    total_sponges = 0
    total_bottles = 0
    total_rooks = 0
    total_D12s = 0
    total_witchhat = 0
    total_bowls = 0


    # file contains spending and items selected per order, and corresponding userid
    file = open("orders.csv")

    # begin printing customer summary
    print("===================================")
    print("         CUSTOMER SUMMARY")
    print("===================================")

    print(f"Customer: {userid}")

    for line in file:
        # each line is comma-separated, so split by comma to create list 'args'
        args = line.split(",")
        if args[0] == userid:
            #accumulate orders and total spending
            total_orders += 1
            total_spent += float(args[1])

            # iterate through every item in each order
            for arg in range(2,len(args)): # skip userid and order cost arg

                # remove any whitespace before beginning checking
                item = args[arg].strip()

                # increment any item counter if corresponding item ordered
                if item == "Sponge":
                    total_sponges += 1
                elif item == "Bottle":
                    total_bottles += 1
                elif item == "Rook":
                    total_rooks += 1
                elif item == "D12":
                    total_D12s += 1
                elif item == "WitchHat":
                    total_witchhat += 1
                elif item == "Bowl":
                    total_bowls += 1



    # display total orders and total spending, using column width formatting
    print(f"Total Orders: {total_orders}")
    print(f"Total Spent: ${total_spent:.2f}")

    print("-----------------------------------")
    # Separate different sections of summary, display total of each item ordered by the user

    print("     Total Products Purchased\n")

    # column width formatting to to right justify total items, with 3 characters allotted for quantity
    if total_sponges:
        print(f"{'Sponges:':<15} {total_sponges:>3}")

    if total_bottles:
        print(f"{'Bottles:':<15} {total_bottles:>3}")

    if total_rooks:
        print(f"{'Rooks:':<15} {total_rooks:>3}")

    if total_D12s:
        print(f"{'D12s:':<15} {total_D12s:>3}")

    if total_witchhat:
        print(f"{'Witch Hats:':<15} {total_witchhat:>3}")

    if total_bowls:
        print(f"{'Bowls:':<15} {total_bowls:>3}")

    return None



def pack_products(product_list):
    """
    Create an organized customer summary, with total spent and total orders, and individual amounts of item ordered, using orders.csv
    Parameters: userid (string)
    Output: Display customer summary
    Return: None
    """

    # iterate through each product in product_list, and collect each with Q-Arm
    for product in product_list:
        product_name = product[0]

        # Move arm to predetermined and recorded position to capture according object
        if product_name == "Sponge":
            arm.set_arm_position([0.612541274884579, 0.14799037228348938, 0.15196687559072983])

        elif product_name == "Bottle":
            arm.set_arm_position([0.6227666323951513, 0.09386696665334929, 0.16453332394390807])

        elif product_name == "Rook":
            arm.set_arm_position([0.6296854719863997, 0.016911887291892653, 0.15049383563434124])

        elif product_name == "D12":
            arm.set_arm_position([0.6270198662795867, -0.054493610142131, 0.16061322905216935])

        elif product_name == "WitchHat":
            arm.set_arm_position([0.6146027260873403, -0.10618460345002326, 0.13085259354493084])

        elif product_name == "Bowl":
            arm.set_arm_position([0.6009553174126216, -0.1579410520366277, 0.11788014881638192])


        sleep(2)

        # Capture the object
        arm.rotate_gripper(-720)
        sleep(2)

        # Move object over basket and drop object
        arm.rotate_shoulder(-25)
        sleep(2)
        arm.rotate_base(-65)
        sleep(2)
        arm.rotate_gripper(720)
        sleep(2)

        # Return arm to home position
        arm.home()
        sleep(2)

def main():
    """
    Controls flow of entire ordering and delivery system
    Parameters: None
    Output: Displays status and warning messages during authentication and invoice/customer summary messages
    Return: None
    """

    print("Welcome!")

    # Attempt to authenticate user, if user is new, sign up is called within
    id = authenticate()

    # Scan barcode, get string of space-seperated items
    items = scan_barcode()

    # Look up prices for items
    products_and_prices = lookup_products(items)

    # Pack products
    pack_products(products_and_prices)

    # Generate order invoice and customer summary
    complete_order(id, products_and_prices)

    customer_summary(id)

if __name__ == "__main__":
    main()







