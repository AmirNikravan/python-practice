import turtle
import random
screen = turtle.Screen()
screen.setup(width=500, height=400)
t1 = turtle.Turtle(shape="turtle")
t1.penup()
t1.goto(x=-500, y=400)
t1.color("red")
t2 = turtle.Turtle(shape="turtle")
t2.penup()
t2.goto(-500, 300)
t2.color("blue")

t3 = turtle.Turtle(shape="turtle")
t3.penup()
t3.goto(x=-500, y=200)
t3.color("green")

t4 = turtle.Turtle(shape="turtle")
t4.penup()
t4.goto(x=-500, y=100)
t4.color("yellow")

t5 = turtle.Turtle(shape="turtle")
t5.penup()
t5.goto(x=-500, y=0)
t5.color("orange")


t6 = turtle.Turtle(shape="turtle")
t6.penup()
t6.goto(x=-500, y=-100)
t6.color("purple")
user_bet = screen.textinput("BET","who do you think will win the game?")

# t1.pendown()
# t2.pendown()
# t3.pendown()
# t4.pendown()
# t5.pendown()
# t6.pendown()
while True :
    t1.forward(random.randint(0,10))
    t2.forward(random.randint(0,10))
    t3.forward(random.randint(0,10))
    t4.forward(random.randint(0,10))
    t5.forward(random.randint(0,10))
    t6.forward(random.randint(0,10))
screen.exitonclick()
