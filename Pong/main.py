from turtle import Screen,Turtle
# from pedal import Pedal

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")

pedal1 = Turtle()
pedal1.shape("square")
pedal1.color("white")
pedal1.shapesize(200,100)
pedal1.goto(0,350)
screen.exitonclick()