import turtle
dashline=turtle.Turtle()
for _ in range (15):
    dashline.forward(15)
    dashline.penup()
    dashline.forward(15)
    dashline.pendown()
screen = turtle.Screen()
screen.exitonclick()