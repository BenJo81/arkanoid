from turtle import Turtle

MOVE_DISTANCE = 10


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=4)
        self.goto(0, -180)

    def left(self):
        if self.xcor() > -250:
            x_cor = self.xcor()
            y_cor = self.ycor()
            self.goto(x_cor - MOVE_DISTANCE, y_cor)

    def right(self):
        if self.xcor() < 250:
            x_cor = self.xcor()
            y_cor = self.ycor()
            self.goto(x_cor + MOVE_DISTANCE, y_cor)