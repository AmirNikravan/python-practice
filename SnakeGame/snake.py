import turtle
POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = list()
        self.create()
        self.head = self.segments[0]

    def create(self):
        for possition in POS:
            newsegment = turtle.Turtle("square")
            newsegment.color("white")
            newsegment.penup()
            newsegment.goto(possition)
            self.segments.append(newsegment)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, possition):
        newsegment = turtle.Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        newsegment.goto(possition)
        self.segments.append(newsegment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]
