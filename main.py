"""Main module where all others are imported and game action is defined."""

from typing import Final
from turtle import Screen
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH: Final[int] = 500
SCREEN_HEIGHT: Final[int] = 600
BALL_SIZE: Final[int] = 20

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout Pro")
screen.tracer(0)

paddle = Paddle((0, -260))
ball = Ball()
screen.update()

screen.exitonclick()