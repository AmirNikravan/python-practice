from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
    def increase(self):
        self.score += 1
        self.show()
    def show(self):
        self.clear()
        self.write(f"score = {self.score}")
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER")
    