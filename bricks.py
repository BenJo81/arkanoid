from turtle import Turtle

BOARD_BRICKS = []
STARTING_COORDINATES = [-228, -163, -98, -33, 32, 97, 162, 227]


class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def row_1(self):
        for position in STARTING_COORDINATES:
            new_brick = Turtle()
            new_brick.penup()
            new_brick.shape("square")
            new_brick.shapesize(stretch_len=3)
            new_brick.color("green")
            new_brick.goto(position, 25)
            BOARD_BRICKS.append(new_brick)

    def row_2(self):
        for position in STARTING_COORDINATES:
            new_brick = Turtle()
            new_brick.penup()
            new_brick.shape("square")
            new_brick.shapesize(stretch_len=3)
            new_brick.color("magenta")
            new_brick.goto(position, 50)
            BOARD_BRICKS.append(new_brick)

    def row_3(self):
        for position in STARTING_COORDINATES:
            new_brick = Turtle()
            new_brick.penup()
            new_brick.shape("square")
            new_brick.shapesize(stretch_len=3)
            new_brick.color("LightSkyBlue")
            new_brick.goto(position, 75)
            BOARD_BRICKS.append(new_brick)

    def row_4(self):
        for position in STARTING_COORDINATES:
            new_brick = Turtle()
            new_brick.penup()
            new_brick.shape("square")
            new_brick.shapesize(stretch_len=3)
            new_brick.color("yellow")
            new_brick.goto(position, 100)
            BOARD_BRICKS.append(new_brick)

    def row_5(self):
        for position in STARTING_COORDINATES:
            new_brick = Turtle()
            new_brick.penup()
            new_brick.shape("square")
            new_brick.shapesize(stretch_len=3)
            new_brick.color("red")
            new_brick.goto(position, 125)
            BOARD_BRICKS.append(new_brick)

    def row_6(self):
        for position in STARTING_COORDINATES:
            new_brick = Turtle()
            new_brick.penup()
            new_brick.shape("square")
            new_brick.shapesize(stretch_len=3)
            new_brick.color("grey")
            new_brick.goto(position, 150)
            BOARD_BRICKS.append(new_brick)

