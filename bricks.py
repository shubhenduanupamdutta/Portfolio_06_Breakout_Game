from turtle import Turtle
from typing import Final

SCREEN_WIDTH: Final[int] = 500
SCREEN_HEIGHT: Final[int] = 600
BRICKS_PER_ROW: Final[int] = 10
ROWS_OF_BRICKS: Final[int] = 5


class Bricks:
    """
    Takes in BRICKS_PER_ROW & ROWS_OF_BRICKS and creates and sets up (BRICKS_PER_ROW * ROW_OF_BRICKS) number of bricks
    """

    def __init__(self, rows=ROWS_OF_BRICKS, per_row=BRICKS_PER_ROW):
        self.rows = rows
        self.per_row = per_row
        self.bricks: list[Turtle] = [Turtle() for _ in range(rows * per_row)]
        self.pen_up()
        self.set_shape()
        self.set_position()
        self.set_color()

    def pen_up(self):
        for brick in self.bricks:
            brick.penup()

    def set_color(self):
        x_coordinates = [t.xcor() for t in self.bricks]
        x_unique = []
        for x in x_coordinates:
            if x not in x_unique:
                x_unique.append(x)
        colors = ["AntiqueWhite", "aquamarine", "bisque", "blue", "brown", "burlywood", "CadetBlue",
                  "chartreuse", "coral", "DarkMagenta"]
        color_map = {x: colors[i] for i, x in enumerate(x_unique)}
        for brick in self.bricks:
            brick.color(color_map[brick.xcor()])

    def set_shape(self):
        width_stretch = 2.2
        for brick in self.bricks:
            brick.shape("square")
            brick.shapesize(stretch_wid=1.0, stretch_len=width_stretch)

    def set_position(self):
        positions = []
        scoreboard_height = 50
        row_height = 25
        brick_len = 25
        x_min, x_max = - int((SCREEN_WIDTH - brick_len) / 2) + 7, int((SCREEN_WIDTH - brick_len) / 2)
        y_min, y_max = SCREEN_HEIGHT // 2 - scoreboard_height - self.rows * row_height, SCREEN_HEIGHT // 2 - scoreboard_height
        for x in range(x_min, x_max, SCREEN_WIDTH // self.per_row):
            for y in range(y_min, y_max, row_height):
                positions.append((x, y))
        for i, brick in enumerate(self.bricks):
            brick.goto(positions[i])


