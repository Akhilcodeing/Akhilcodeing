import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Hypnotic Spiral Pattern")

t = turtle.Turtle()
t.speed(0)  
t.color("red", "orange")
t.width(2)

for i in range(1000):
    t.circle(i, 45)
    t.left(10)

t.hideturtle()
wn.exitonclick()

    
 
