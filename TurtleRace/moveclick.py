import turtle

screen = turtle.Screen()
new = turtle.Turtle()


def move_forward():

    new.forward(10)


def turn_left():
    new.left(10)


def turn_right():
    new.right(10)


def turn_back():
    new.backward(10)

def clear():
    new.home()
    new.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(turn_back, "s")
screen.onkey(clear, "c")

screen.exitonclick()
