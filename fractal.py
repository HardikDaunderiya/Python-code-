import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set up the turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)  # Fastest drawing
pen.color("green")
pen.left(90)  # Start pointing upwards

# Function to draw a fractal tree
def draw_tree(branch_length, pen):
    if branch_length > 5:  # Base case for recursion
        pen.forward(branch_length)
        pen.right(20)
        draw_tree(branch_length - 15, pen)
        pen.left(40)
        draw_tree(branch_length - 15, pen)
        pen.right(20)
        pen.backward(branch_length)

# Initial settings for tree size and depth
pen.penup()
pen.goto(0, -200)  # Start at the bottom of the screen
pen.pendown()
pen.setheading(90)  # Face upward to draw the trunk

# Draw the fractal tree
draw_tree(100, pen)

# Hide the turtle after drawing
pen.hideturtle()

# Finish drawing
screen.exitonclick()
