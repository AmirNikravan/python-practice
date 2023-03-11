import turtle
from random import randint


def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


new = turtle.Turtle()
for _ in range(100):
    # new.color(colors())
    new.circle(100)
    new.setheading(new.heading() + 10)
screen = turtle.Screen()
screen.exitonclick()
