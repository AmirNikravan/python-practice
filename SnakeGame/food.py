from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__() 
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color(color="blue")
        self.speed("fastest")
        x_random = random.randint(-280,280)
        y_random = random.randint(-280,280)
        self.goto(x_random,y_random)