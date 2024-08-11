import turtle

# create a turtle object
t = turtle.Turtle()

# draw an Om symbol
t.pensize(10)
t.pencolor("black")
t.penup()
t.goto(-100, 100)
t.pendown()
t.circle(50)
t.penup()
t.goto(0, 150)
t.pendown()
t.circle(50)
t.penup()
t.goto(100, 100)
t.pendown()
t.circle(50)
t.penup()
t.goto(0, 0)
t.pendown()
t.write("HELLO", font=("Arial", 36))
t.done()
