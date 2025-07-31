import turtle

# creating canvas
turtle.Screen().bgcolor("pink")

turtle.Screen().setup(500, 500)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board= turtle.Turtle()

n = 6
# creating a square
for i in range(n):
    board.forward(100)
    board.left(360/n)

turtle.done()