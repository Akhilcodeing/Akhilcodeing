import turtle
screen = turtle.Screen()

screen.setup(width = 1.0, height = 1.0)
turtle.bgcolor('black')
tr = turtle.Turtle()
tr.speed("fastest")
tr.up()
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(-500, .0)
        tr.down()
        tr.color("purple")
        tr.forward(100)
        tr.circle(5, steps =4)
        tr.right(60)
        tr.color("white")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()
for i in range(10):
    for i in range(2):
        tr.pensize(7)
        tr.goto(470, 0)
        tr.down()
        tr.color("red")
        tr.forward(100)
        tr.circle(5, steps = 4)
        tr.right(60)
        tr.color("white")
        tr.forward(50)
        tr.right(120)
    tr.right(30)
tr.up()
turtle.up()
turtle.color('white')
turtle.goto(-320, 40)
turtle.write("Happy",font=(None, 60))
turtle.goto(-60, 40)
turtle.color('white')
turtle.write("New", font=(None, 60))
turtle.goto(145, 40)
turtle.color('white')
turtle.write("year", font=(None, 60))
turtle.goto(-74, -60)
turtle.color('white')
turtle.write("2024", font=(None, 60))
turtle.done()
























        
    
        
        
