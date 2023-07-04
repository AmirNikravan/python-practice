from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        with open("E:\Programming\Python\python-practice\SnakeGame\data.txt") as data:
            self.high_score = int(data.read())

    def increase(self):
        self.score += 1
        self.show()

    def show(self):
        self.clear()
        self.write(f"score = {self.score} high score = {self.high_score}")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER")

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("E:\Programming\Python\python-practice\SnakeGame\data.txt",mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.show()
