# ----------------------------
# TURTLE SPIRAL ART WITH COMMENTS
# ----------------------------

# Import everything from the turtle module
# 'turtle' is a built-in Python library for graphics/drawing
# The '*' imports all turtle functions (forward, left, color, etc.) so we can use them directly
from turtle import *

# Set the drawing speed of the turtle
# 0 = fastest, 1 = slowest, up to 10
speed(0)  # built-in turtle function

# Set the background color of the canvas
bgcolor("black")  # built-in turtle function

# Create a Python list of colors to alternate
# This is user-defined (not built-in)
colors = ['orange', 'white']

# Hide the turtle cursor so we only see the drawing
hideturtle()  # built-in turtle function

# Start a for-loop in Python (built-in keyword)
# Loop 122 times to create the spiral pattern
for i in range(122):  # i goes from 0 to 121

    # Move the turtle to the center of the canvas (0,0)
    # built-in turtle function
    goto(0, 0)

    # Set the pen color
    # colors[i % 2] alternates between 'orange' and 'white'
    # built-in turtle function
    color(colors[i % 2])

    # Move turtle forward by 130 units (pixels)
    # built-in turtle function
    forward(130)

    # Rotate turtle 3 degrees to the left (counter-clockwise)
    # built-in turtle function
    left(3)

    # Draw a circle of radius 40 units
    # built-in turtle function
    circle(40)

    # Move forward again by 130 units
    # built-in turtle function
    forward(130)

    # Rotate turtle 180 degrees to face opposite direction
    # built-in turtle function
    right(180)

# End the drawing and keep the window open
# built-in turtle function
done()

# ----------------------------
# SUMMARY OF COMMANDS:
# ----------------------------
# from turtle import *      --> imports all turtle functions
# speed()                   --> sets drawing speed
# bgcolor()                 --> sets background color
# colors = [...]            --> Python list (user-defined)
# hideturtle()              --> hides the turtle icon
# for i in range(n):        --> Python for-loop
# goto(x, y)                --> move turtle to coordinates
# color()                   --> set pen color
# forward(n)                --> move turtle forward
# left(angle) / right(angle)--> rotate turtle
# circle(radius)            --> draw a circle of given radius
# done()                    --> finish drawing and keep window open
