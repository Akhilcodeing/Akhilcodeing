import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

def leaf():
    t.begin_fill()
    t.color("green")
    t.left(45)
    t.forward(50)
    t.right(135)
    t.circle(50, -90)
    t.right(135)
    t.forward(50)
    t.left(45)
    t.end_fill()
    
t.penup()
t.goto(0, -200)
t.pendown()
t.begin_fill()
t.color("#C68E17")
t.circle(200)
t.end_fill()

for i in range(12):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(30 * i)
    leaf()

t.hideturtle()
turtle.mainloop()
