import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1000, height=600)
screen.title("DMC")

# Create a turtle object
flag_turtle = turtle.Turtle()

# Set initial position
flag_turtle.penup()
flag_turtle.goto(-250, 150)
flag_turtle.pendown()

# Draw the saffron rectangle
flag_turtle.color("#FF9933")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(500)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Move to the white rectangle position
flag_turtle.penup()
flag_turtle.goto(-250, 50)
flag_turtle.pendown()

# Draw the white rectangle
flag_turtle.color("white")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(500)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Move to the green rectangle position
flag_turtle.penup()
flag_turtle.goto(-250, -50)
flag_turtle.pendown()

# Draw the green rectangle
flag_turtle.color("#138808")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(500)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()

# Draw the Ashoka Chakra (Navy Blue Circle)
flag_turtle.penup()
flag_turtle.goto(0, 0)
flag_turtle.pendown()
flag_turtle.color("navy")
flag_turtle.pensize(3)
flag_turtle.circle(50, 24)

# Draw 24 spokes of the Ashoka Chakra
for _ in range(24):
    flag_turtle.penup()
    flag_turtle.goto(0, 0)
    flag_turtle.pendown()
    flag_turtle.setheading(-_ * 15)
    flag_turtle.forward(50)
    flag_turtle.backward(50)

flag_turtle.penup()
flag_turtle.goto(-250, -180)
flag_turtle.pendown()
flag_turtle.color("black")
flag_turtle.write("DAVID MEMOMRIAL INSTITUTIONS", align="left", font=("Arial", 14, "normal"))


# Hide the turtle
flag_turtle.hideturtle()

# Display the flag
turtle.done()
