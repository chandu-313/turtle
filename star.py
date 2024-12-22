import turtle
turtle.Screen().bgcolor("yellow")
tri=turtle.Turtle()
for i in range(3):
    tri.forward(100)
    tri.left(120)
tri.left(90)
tri.penup()
tri.forward(50)
tri.right(90)
tri.pendown()
for i in range(3):
    tri.forward(100)
    tri.right(120)
turtle.done()

