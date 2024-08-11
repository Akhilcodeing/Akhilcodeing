import turtle

t = turtle.Turtle()
t.pensize(10)
t.pencolor("black")
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(100, 180)
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(-100, 180)
t.penup()
t.goto(30, 30)
t.pendown()

for i in range(5):
    t.forward(60)
    t.right(144)

turtle.done()
