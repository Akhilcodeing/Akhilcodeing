import turtle

# Set up the screen
turtle.setup(800, 800)
turtle.bgcolor("black")

# Create a turtle object
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)

# List of colors to use in the spiral
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Function to draw a colorful spiral
def draw_spiral():
    for i in range(360):
        spiral_turtle.color(colors[i % len(colors)])
        spiral_turtle.forward(i)
        spiral_turtle.left(59)

# Move the turtle to a starting position
spiral_turtle.penup()
spiral_turtle.goto(0, 0)
spiral_turtle.pendown()

# Draw the spiral
draw_spiral()

# Hide the turtle
spiral_turtle.hideturtle()

# Keep the window open
turtle.done()
