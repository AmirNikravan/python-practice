from turtle import Turtle
class Pedal(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(200,100)
        self.goto(0,350)