# Name: Yaseen Nabag
# Date: 2024-10-01
# Asteroid Kaboom Game
# File Name : Nabag_ComputingAssignment1.py
# Description: A game where players shoot at randomly placed asteroids

## Imports
import time
import random
import turtle
from pixels import check_pixel_color

## Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "Asteroid Kaboom"


## Screen Setup
# Initialize screen
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)
screen.bgcolor("Black")

# Initial starting message
turtle.hideturtle()
turtle.penup()
turtle.goto(-225, 0)
turtle.pendown()
turtle.pencolor("Red")
turtle.write("Asteroid Kaboom!!!!", font=("Arial", 50, "bold"))
time.sleep(4)

# Clear inital message
turtle.clear()

# Set color mode and turn off animation for faster drawing
turtle.colormode(255)
turtle.tracer(0, 0)


##Turtle Setup

t = turtle.Turtle()
t.hideturtle()
t.left(90)


## Functions

# Return a random grey color value
def random_grey():

    return random.randint(0, 255)

# Draw a small star
def draw_star():

    # Loop to create star shape
    for _ in range(5):
        t.forward(2)
        t.right(152)
        t.forward(2)
        t.left(80)

# Draw a 7-sided asteroid of random size and rotation
def draw_asteroid(size):

    t.begin_fill()

    # Random rotation for asteroid
    t.right(random.randint(0, 360))

    # Loop to create 7-sided shape
    for _ in range(7):
        t.forward(size)
        t.right(360 / 7)
    t.end_fill()
    return size

# Draw an explosion at given coordinates
def draw_explosion(x, y):

    # Draw an explosion centered on (x, y)
    t.penup()
    t.goto(x, y)

    # reset orientation
    t.setheading(0)
    t.pendown()

    # half of explosion size
    offset = 10
    t.penup()
    t.goto(x - offset, y - offset)
    t.pendown()

    # Explosion effect
    t.color("White")
    t.shape("circle")
    t.turtlesize(2.5)
    t.stamp()
    t.turtlesize(2)
    t.color("Red")
    t.stamp()

## Draw background stars
# Draw 100 stars
for _ in range(100):

    # Random position for star within screen bounds
    x_star = random.randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2)
    y_star = random.randint(-SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2 - 25)

    # Draw star at position with random grey color
    color_value = random_grey()
    t.color(color_value, color_value, color_value)
    t.penup()
    t.goto(x_star, y_star)
    t.pendown()

    #Call function to draw star
    draw_star()

## Draw Asteriods

# Draw 15 asteroids

for _ in range(15):

    # Randomly choose asteroid color (Pink or Purple)
    color_name = ("Pink", "Purple")[random.randint(0, 1)]
    t.color(color_name)
    size = random.randint(25, 50)


    # Random position for asteroid within screen bounds
    x_asteroid = random.randint(-SCREEN_WIDTH // 2 + 130, SCREEN_WIDTH // 2 - 130)
    y_asteroid = random.randint(-SCREEN_HEIGHT // 2 + 130, SCREEN_HEIGHT // 2 - 130)

    t.penup()

    # Position turtle to center the asteroid at (x_asteroid, y_asteroid)
    t.goto(x_asteroid - size/2, y_asteroid - size/2)

    t.pendown()
    draw_asteroid(size)

t.penup()
t.goto(0,0)
t.pendown()
draw_asteroid(size)

# Update screen with all drawings
turtle.update()

## Shooting phase

# Get number of shots from player
shots = int(screen.numinput("SHOTS", "How many shots would you like to take?"))
score = 0

# Loop for each shot
for i in range(shots):

    # Get shot coordinates from player
    x = screen.numinput("X Coordinate", f"Shot {i+1}: Enter X coordinate:")
    y = screen.numinput("Y Coordinate", f"Shot {i+1}: Enter Y coordinate:")

    # Calculate score based on asteroid color
    shot_pink = check_pixel_color(x, y, "Pink") * 100
    shot_purple = check_pixel_color(x, y, "Purple") * 10
    total = shot_pink + shot_purple
    score += total

    # Draw explosion at shot location
    draw_explosion(x, y)

    # Display score above explosion
    t.color("Yellow")
    t.write(f"+{total}", font=("Arial", 12, "bold"), align="center")

turtle.update()

## Display final score

t.penup()
t.goto(-110, 200)
t.pencolor("Red")
t.pendown()
t.write(f"You scored {score} points!", font=("Arial", 20, "bold"))


## Clean Exit
screen.exitonclick()
