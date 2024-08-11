from turtle import *
import colorsys
bgcolor("black")
tracer(10)
pensize(3)
h = 0
for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h+=0.005
    color(c)
    goto(0,0)
    fd(i)
    rt(144)
    for j in range(5):
        fd(30)
        lt(143)
done()
