"""
This program contains functions to draw shapes with colors.
Welcome to Paint!
Press one of the following keys to change color.
K -> BLACK
W -> WHITE
G -> GREEN
B -> BLUE
R -> RED
O -> ORANGE
Press one of the following keys to set the shape to draw.
l -> line
s -> square
c -> circle
r -> rectangle
t -> triangle
With a color and a shape set, you just have to click once to
set the starting point and click a second time to draw the shape.
Good luck!
"""

# Standard library imports.
import math

# Third party related imports.
from turtle import up, down, goto, begin_fill,   \
                   end_fill, forward, left,      \
                   setup, onscreenclick, listen, \
                   onkey, color, undo, done
import turtle
from freegames import vector

print(__doc__)  # Print usage information.


def line(start, end):
    """
    Draws line from start to end.
    The line is drawn from the position of the first tap to 
    the position of the second tap.
    Parameters:
    start: vector -- Vector containing coordinates
                         x, y of start position.
    end: vector -- Vector containing coordinates
                       x, y of end position.
    Returns:
    None
    """

    up()  # Not drawing when moving.
    goto(start.x, start.y)
    down()  # Drawing when moving.
    goto(end.x, end.y)


def square(start, end):
    """
    Draws a square.
    The magnitude of the difference between the starting point and
    the end point along the x-axis is the size of the side of the
    square. The square is drawn with 4 lines. The first line is drawn
    from the start position in the direction of the x-axis. It will
    point to the right if the end position is further right than
    the start position, and left otherwise. The following lines are
    drawn by rotating the direction 90 degrees clockwise.
    Parameters:
    start: vector -- Vector containing coordinates
                         x, y of start position.
    end: vector -- Vector containing coordinates
                       x, y of end position.
    Returns:
    None
    """

    up()
    goto(start.x, start.y)
    down()

    begin_fill()  #  Draw line, rotate 90 deg. and repeat 4 times.
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()


def circle(start, end):
    """
    Draws a circle.
    The distance between the 2 taps is the diameter of the circle.
    The function draws this line for better visualization and then
    draws the circle.
    Parameters:
    start: vector -- Vector containing coordinates
                         x, y of start position.
    end: vector -- Vector containing coordinates
                       x, y of end position.
    Returns:
    None
    """
    
    line(start, end)
    # Distance between vectors.
    diameter = math.sqrt((end.x - start.x) ** 2
                       + (end.y - start.y) ** 2)
    radius = diameter / 2
    # Center through decomposition.
    center = [start.x + (end.x - start.x) / 2,
              start.y + (end.y - start.y) / 2]
    bottom = [center[0]] + [center[1] - radius]

    up()
    goto(bottom[0], bottom[1])
    down()

    turtle.circle(radius)


def rectangle(start, end):
    """
    Draws a rectangle.
    
    The magnitude of the first and third lines is the magnitude
    of the difference between the end and start positions along
    the x-axis. The same applies with the second and last lines
    along the y-axis.
    The rectangle is drawn with 4 lines. The first line is drawn
    from the start position in the direction of the x-axis. It will
    point to the right if the end position is further right than
    the start position, and left otherwise. The following lines are
    drawn by rotating the direction 90 degrees clockwise.
    Parameters:
    start: vector -- Vector containing coordinates
                         x, y of start position.
    end: vector -- Vector containing coordinates
                       x, y of end position.
    Returns:
    None
    """

    up()
    goto(start.x, start.y)
    down()
    
    begin_fill()
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)
    forward(end.x - start.x)
    left(90)
    forward(end.y - start.y)
    left(90)
    end_fill()


def triangle(start, end):
    """
    Draws a right angled scalene triangle from start to end
    
    Parameters:
    start: vector -- Vector containing coordinates
                         x, y of start position.
    end: vector -- Vector containing coordinates
                       x, y of end position.
    Returns:
    None
    """
    up()
    goto(start.x, start.y)
    down()
    
    hip = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)
    alpha = math.acos((end.x - start.x) / hip) * 180 / math.pi
    
    if (end.y - start.y) >= 0:
        begin_fill()
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90 + alpha)
        forward(hip)
        left(180 - alpha)
        end_fill()
    else:
        begin_fill()
        forward(end.x - start.x)
        left(-90)
        forward(abs(end.y - start.y))
        left(-(90 + alpha))
        forward(hip)
        left(-(180 - alpha))
        end_fill()
        


def tap(x, y):
    """
    Does the necessary operations after a tap.
    
    If the tap is the first one, it just stores is,
    otherwise it stores it as the last tap, calls the
    shape function and resets the start.
    Parameters:
    x: -- The position of the screen click in the x-axis.
    y: -- The position of the screen click in the y-axis.
    Returns:
    None
    """

    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Stores the given value in the state dictionary using the key"""
    state[key] = value


# Initial steps.
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)

onscreenclick(tap)  # Function to do when screen is clicked.
listen()  # Collect key events.

# Functions to  respond to a key being pressed.
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color("orange"), "O")  # Adding extra color.
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()  # The event loop.
