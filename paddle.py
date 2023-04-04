"""Defines the class of Paddle, inherits from turtle"""
from turtle import Turtle


class Paddle(Turtle):
    """Paddle class made up on Turtle class"""
    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.shape("square")
        self.color("#EEEEEE")
        self.shapesize(stretch_wid=1.0, stretch_len=3.0)
        self.penup()
        self.goto(position)

    def move_left(self):
        """Function to move the paddle left"""
        self.goto(self.xcor() - 20, self.ycor())

    def move_right(self):
        """Function to move the paddle right"""
        self.goto(self.xcor() + 20, self.ycor())
