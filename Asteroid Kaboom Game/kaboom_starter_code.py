""" This is your starter code for the Asteroid Kaboom assignment.

You should rename this file and replace this docstring with your own,
as per the documentation standards.

To use this template, make sure that both this file and pixels.py are in the
same folder. From Pyzo, choose Run File as Script.

This template allows you to use a special check_pixel_color function.

For example, check_pixel_color(0, 0, "green") will return 1 if the pixel
at location (0,0) is "green", or 0 if it is not. When you are assigning
points for shots in the assignment, you can multiply the return value by
the number of points for hitting that color.

Sam Scott, McMaster, 2025"""

# Import the turtle module
import turtle
from pixels import check_pixel_color

# Constants (you can change these)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "My First Turtle Program"

# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)

# Create the turtle object
t = turtle.Turtle()

## Start of your code

# example of how to use check_pixel_color
print( check_pixel_color(100, 0, "white") ) # returns 1
print( check_pixel_color(0, 0, "white") )   # returns 0

## End of your code

# Make a clean exit
screen.exitonclick()
