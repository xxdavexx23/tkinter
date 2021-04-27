import turtle

wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Indicator")

# create an arrow
the_pointer = turtle.Turtle()
the_pointer.shape = "arrow"

# set the arrow's size
the_pointer.shapesize(10,5,10)

# bring the pen up
the_pointer.up()

# rotate clockwise
for angle in range(360):
    the_pointer.right(1)

# rotate counter-clockwise
for angle in range(360):
    the_pointer.left(1)

turtle.done()