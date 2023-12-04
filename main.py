from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
import time

game_on = True

screen = Screen()
screen.bgcolor("navy")
screen.setup(width=600, height=600)
screen.title("My Arkanoid Game")
screen.tracer(0)

paddle = Paddle()
bricks = Bricks()
ball = Ball()

bricks.row_1()
bricks.row_2()
bricks.row_3()
bricks.row_4()
bricks.row_5()
bricks.row_6()

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)




screen.exitonclick()