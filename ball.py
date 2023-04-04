from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_step: int = 2
        self.y_step: int = 2
        self.movement_speed: float = 0.02

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step *= -1

    def increase_speed(self):
        self.movement_speed *= 0.95

    def bounce_x(self):
        self.x_step *= -1

    def reset(self):
        self.home()
        self.bounce_x()
        self.movement_speed = 0.1
