from colors import colors
import random
import turtle
def color():
    return random.choices(colors)
def cal():
    lists = [0,90,180,270]
    # x= random.choices(lists)
    return random.choices(lists)[0]

def draw():
    new = turtle.Turtle()

    # for i in range(200):
    #     new.color(color())
    #     new.forward(100)
    #     new.right(cal())
    # or :
    
    for i in range(200):
        new.color(color())
        new.forward(100)
        new.setheading(cal())
    
draw()
screen = turtle.Screen()
screen.exitonclick()