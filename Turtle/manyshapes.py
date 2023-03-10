import turtle
from random import choices
from colors import colors
def color():
    return choices(colors)
def cal(lines):
    return int(360 / lines)

def draw():
    for number_of_lines in range(3,10):
        new = turtle.Turtle()
        new.color(color())
        count = cal(number_of_lines)
        for i in range(number_of_lines):
            new.forward(100)
            new.right(count)
    
draw()
screen = turtle.Screen()
screen.exitonclick()