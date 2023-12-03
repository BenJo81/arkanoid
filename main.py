from turtle import Turtle, Screen
from paddle import Paddle
import time

game_on = True

screen = Screen()
screen.bgcolor("blue")
screen.setup(width=600, height=600)
screen.title("My Arkanoid Game")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)




screen.exitonclick()