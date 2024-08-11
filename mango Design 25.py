import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Draw the mango
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
t.color("black")
t.circle(50)

# Draw the stem
t.penup()
t.goto(0, 70)
t.pendown()
t.color("green")
t.begin_fill()
t.goto(-15, 100)
t.goto(0, 130)
t.goto(15, 100)
t.goto(0, 70)
t.end_fill()

# Draw the leaf
t.penup()
t.goto(10, 80)
t.pendown()
t.color("green")
t.begin_fill()
t.goto(20, 120)
t.goto(30, 80)
t.goto(10, 80)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until it is clicked
turtle.done()
