import turtle

t = turtle.Turtle()
t.pensize(10)
t.pencolor("black")
t.penup()
t.goto(0, 100)
t.pendown()
t.goto(0, -100)
t.penup()
t.goto(-100, 0)
t.pendown()
t.goto(100, 0)
turtle.done()
