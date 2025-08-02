import turtle

turtle.Screen().bgcolor("pink")

turtle.Screen().setup(500, 500)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()
board.forward(100) 

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

rectangle = turtle.Turtle()
rectangle.penup()
rectangle.left(300)
rectangle.forward(100)
rectangle.pendown()
rectangle.forward(100)

rectangle.left(90)
rectangle.forward(50)

rectangle.left(90)
rectangle.forward(100)

rectangle.left(90)
rectangle.forward(50)

hexagon = turtle.Turtle()
hexagon.penup()
hexagon.left(200)
hexagon.forward(100)
hexagon.pendown()
hexagon.forward(100) 

hexagon.left(60)
hexagon.forward(100)

hexagon.left(60)
hexagon.forward(100)

hexagon.left(60)
hexagon.forward(100)

hexagon.left(60)
hexagon.forward(100)

hexagon.left(60)
hexagon.forward(100)