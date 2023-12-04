from turtle import Turtle

X_COR = 0
Y_COR = -160

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(X_COR, Y_COR)