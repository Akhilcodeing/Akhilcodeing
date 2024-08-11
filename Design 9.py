from turtle import *
import colorsys
bgcolor("black")
pen()
h = 0
speed(0)
tracer(50)
for i in range(200):
    width(i / 100 + 1)
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    pencolor(c)
    left(1000)
    pu()
    forward(i)
    pd()
    circle(i, -90)
    right(200)
    pu()
    forward(i)
    left(120)
    pd()
    fd(7)
    lt(909)
    h+=0.009
done()
    
    
    
