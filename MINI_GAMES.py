# Name: Yaseen Nabag
# File Name: MINI_GAMES
# Date: oct 23rd, 2025
# Description: A collection of mini-games including Look Away, Slot Machine, and Pig Dice Game.


import random
import time

# Print Signature
def print_signature():
    """Display assignment signature information for the student.
    Parameters: None
    Returns: None (prints to screen) """


def divider():

    "Print a horizontal divider line for clarity between sections."

    print("_____________________________")


# Look Away Menu
def look_away_menu():

    """Show instructions for the Look Away game choices."""

    print("""

--------------------------

MacParty Look Away Game

--------------------------

1 = Up | 2 = Down | 3 = Left | 4 = Right

If you look differently than BOTH computers, you win the round.
_____________________________
""")


# Main Menu
def main_menu(name):

    """Display main menu options for the MacParty Game Room.
    Parameters:
        name (str): player name
    Returns: None
    """

    print(f"""
=============================

WELCOME TO MACPARTY {name} !!!

=============================
1) Look Away Game
2) Slot Machine Game
3) Pig Game
4) Exit
_____________________________
""")


# Slot Machine Menu
def slot_machine_menu():

    """Show Slot Machine rules and payouts."""

    print("""
--------------------------
MacParty Slot Machine
--------------------------
Three symbols spin.
3 match → 5x bet
2 match → 2x bet
0 match → 0
Rule: You can’t bet more than your current points.
_____________________________
""")


# Pig Game Menu
def pig_menu():

    """Show Pig Dice instructions and win/loss rules."""

    print("""
-----------------
MACPARTY PIG GAME
-----------------
Roll two dice toward your threshold.
Win: total > threshold
Loss: a single 1 appears
Catastrophic loss: snake eyes (1,1)
_____________________________
""")


# Look Away Game
def look_away(first_move, second_move, third_move):

    """Play three rounds of the Look Away game.
    Parameters:
        first_move, second_move, third_move (int, 1–4): directions chosen by player
    Returns:
        int – points earned (10 per winning round)
    """

    # Initialize score
    score = 0

    def direction_name(num):

        """Return the text name of a direction without using a list."""

        if num == 1:

            return "Up"

        elif num == 2:

            return "Down"

        elif num == 3:

            return "Left"

        else:
            return "Right"

    # Random moves for computers round 1 from 1 to 4
    computer_one_move = random.randint(1, 4)
    computer_two_move = random.randint(1, 4)

    # Round 1
    # Check if human wins
    if first_move != computer_one_move and first_move != computer_two_move:
        print(f"\nComputer 1: {direction_name(computer_one_move)} | Computer 2: {direction_name(computer_two_move)} | Human: {direction_name(first_move)} → Human wins first round!")
        score += 10


    # Computer wins
    else:
        print(f"\nComputer 1: {direction_name(computer_one_move)} | Computer 2: {direction_name(computer_two_move)} | Human: {direction_name(first_move)} → Computer wins first round!")

    # Round 2
    computer_one_move = random.randint(1, 4)
    computer_two_move = random.randint(1, 4)

    # Check if human wins
    if second_move != computer_one_move and second_move != computer_two_move:
        print(f"Computer 1: {direction_name(computer_one_move)} | Computer 2: {direction_name(computer_two_move)} | Human: {direction_name(second_move)} → Human wins second round!")
        score += 10

    # Computer wins
    else:
        print(f"Computer 1: {direction_name(computer_one_move)} | Computer 2: {direction_name(computer_two_move)} | Human: {direction_name(second_move)} → Computer wins second round!")

    # Round 3
    computer_one_move = random.randint(1, 4)
    computer_two_move = random.randint(1, 4)

    # Check if human wins
    if third_move != computer_one_move and third_move != computer_two_move:
        print(f"Computer 1: {direction_name(computer_one_move)} | Computer 2: {direction_name(computer_two_move)} | Human: {direction_name(third_move)} → Human wins third round!\n")
        score += 10

    # Computer wins
    else:
        print(f"Computer 1: {direction_name(computer_one_move)} | Computer 2: {direction_name(computer_two_move)} | Human: {direction_name(third_move)} → Computer wins third round!\n")

    # Return total score of human
    return score

# Slot Machine Game
def slot_machine(bet):

    """Simulate a slot machine spin.
    Parameters:
        bet (int): amount bet by the player
    Returns:
        int – winnings (0, 2×bet, or 5×bet)
    """

    # Initialize winnings
    won = 0

    # Slot symbols
    def get_symbol(num):
        if num == 1:
            return "🚀"
        elif num == 2:
            return "🎰"
        elif num == 3:
            return "💎"
        else:
            return "🪩"

    # Spin the slots from 1 to 4
    slot_one = random.randint(1, 4)
    slot_two = random.randint(1, 4)
    slot_three = random.randint(1, 4)

    # Display the results
    print("spinning... ", end="")
    time.sleep(0.5)
    print(get_symbol(slot_one), end=" | ")
    time.sleep(0.5)
    print(get_symbol(slot_two), end=" | ")
    time.sleep(0.5)
    print(get_symbol(slot_three),end=" | ")
    time.sleep(0.5)

    # Check for matches
    # Three matches
    if slot_one == slot_two == slot_three:
        print("JACKPOT!!!, you matched all three symbols!")
        won = bet * 5

    # Two matches
    elif slot_one == slot_two or slot_one == slot_three or slot_two == slot_three:
        print("You matched two symbols!")
        won = bet * 2

    # No matches
    else:
        print("No matches this time. Better luck next time!")
        won = 0

    # Return winnings
    return won

def pig_dice(threshold):

    """Play the Pig Dice game until win/loss occurs.
    Parameters:
        threshold (int): target score to beat
    Returns:
        int: -1 (catastrophic loss), 0 (loss), or total points (win)
    """

    scoring = 0

    # Initialize rolls text
    rolls_text = ""

    # Flag for first roll
    first = True

    # Roll dice until scoring meets or exceeds threshold
    while scoring < threshold:
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)

        # Update rolls text
        if first:

            # add first roll
            rolls_text += f"({dice_one}, {dice_two})"
            first = False

        # subsequent rolls
        else:


            rolls_text += f", ({dice_one}, {dice_two})"

        # Check for losses or update score
        if dice_one == 1 and dice_two == 1:
            print(f"\nThreshold {threshold}. Rolls: {rolls_text}. Catastrophic loss.")
            return -1

        # Single loss
        elif dice_one == 1 or dice_two == 1:
            print(f"\nThreshold {threshold}. Rolls: {rolls_text}. Loss.")
            return 0

        # Continue scoring
        else:

            # Update scoring
            scoring += dice_one + dice_two
            if scoring > threshold:
                print(f"\nThreshold {threshold}. Rolls: {rolls_text}. Win ({scoring} points).")
                return scoring


def games_room(name):

    """Run the main MacParty game loop until the player quits.
    Parameters:
        name (str): player name
    Returns:
        int – final score
    """


    # Initialize score
    score = 0

    # Main game loop
    while True:

        # Display current score and main menu
        time.sleep(1)
        print(f"\nCurrent score: {score}")
        main_menu(name)

        menu_choice = int(input("Plase select a game (1-4): "))


        # Process menu choice
        # Look Away Game
        if menu_choice == 1:
            look_away_menu()

            # Get user input for three rounds
            first_round = int(input("Please choose a direction (1-4) for the first round: "))
            second_round = int(input("Please choose a direction (1-4) for the second round: "))
            third_round = int(input("Please choose a direction (1-4) for the third round: "))


            # Validate input from user between 1 and 4
            if not (1 <= first_round <= 4 and 1 <= second_round <= 4 and 1 <= third_round <= 4):

                # if score is 0, cannot lose points
                if score == 0:
                    print("You have no points to lose. Please enter valid directions.")

                # else, deduct random points between 1 and 20
                else:
                    points_lost = random.randint(1, 20)
                    score = score - points_lost
                    print(f"Invalid input, you lost {points_lost} points. Your new score is {score}.")

                # Go back to main menu
                continue

            # Play Look Away Game
            gained = look_away(first_round, second_round, third_round)
            print(f"You earned {gained} points from this round.")
            divider()
            score += gained


        # Slot Machine Game
        elif menu_choice == 2:

            # If user has no points, they can't bet
            if score <= 0:
                print("You have 0 points — you can’t place a bet. Play another game first.")
                continue

            slot_machine_menu()

            # Get player's bet
            bet = int(input(f"How much would you like to bet? (1–{score}): "))

            # Validate the bet
            if bet < 1:
                print("Bet must be at least 1 point.")
                continue

            elif bet > score:
                print("You cannot bet more than your current points.")
                continue

            else:

                # Deduct the bet before spinning
                score -= bet

                # Play the slot machine
                won = slot_machine(bet)

                # Update total score based on winnings
                score += won

                print(f"You earned {won} points this round.")

            divider()




        # Pig Dice Game
        elif menu_choice == 3:

            # Display Pig Game Menu
            pig_menu()

            # Get user threshold
            threshold = int(input("How many points do you want to score?: "))

            # call pig dice function
            result = pig_dice(threshold)


            # Update score based on result
            if result == -1:
                print("Catastrophic loss! Your score has been reset to 0.")
                score = 0

            elif result == 0:
                print("You lost this round. No points added.")

            # Single loss
            else:
                print(f"You earned {result} points from this round.")
                score += result

            divider()



        elif menu_choice == 4:
            print("\nGOODBYE!!")
            return score

        # Make sure user inputs valid menu choice
        else:

            # if score is 0, cannot lose points
            if 20 > score :
                    print("You have no points to lose. Please enter valid directions.")

                    # Go back to main menu
                    continue

            # else, deduct random points between 1 and 20
            else:
                points_lost = random.randint(1, 20)
                score = score - points_lost
                print(f"Invalid input, you lost {points_lost} points. Your new score is {score}.")

                # Go back to main menu
                continue

## Main Program

# Call print signature
print_signature()

# Get user name and convert to uppercase
name = input("Please enter your name: ").upper()

# Start games room
final_score = games_room(name)

print(f"Final score: {final_score}")
