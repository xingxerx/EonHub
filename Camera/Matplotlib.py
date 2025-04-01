import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward
    t.right(90)     # Turn right

turtle.done()