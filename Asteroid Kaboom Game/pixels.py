""" This is helper code for the Asteroid Kaboom assignment. To use it,
include this line in your main program:

from pixels import check_pixel_color

Then in your main program, you can check the color of a pixel.

For example, check_pixel_color(0, 0, "green") will return 1 if the pixel
at location (0,0) is "green", or 0 if it is not. When you are assigning
points for shots in the assignment, you can multiply the return value by
the number of points for hitting that color.

https://github.com/furas/python-examples/tree/master/turtle/get-pixel-color

Adapted by Sam Scott and Ethan McMehen, McMaster University, 2025
"""
import turtle

def check_pixel_color(x, y, target_color):
    """Returns 1 if  pixel at location (x, y) matches the target_color string.
       Returns 0 otherwise."""
    y = -y
    canvas = turtle.getcanvas()
    color = turtle.Screen().bgcolor()
    ids = canvas.find_overlapping(x, y, x, y)
    for id in ids:
        true_color = canvas.itemcget(id, "fill")
        if true_color:
            color = true_color
    return int(color == target_color)
