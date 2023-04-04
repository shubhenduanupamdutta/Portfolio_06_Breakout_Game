"""Main module where all others are imported and game action is defined."""
import time
from typing import Final
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Bricks

# Designing Game Window
SCREEN_WIDTH: Final[int] = 500
SCREEN_HEIGHT: Final[int] = 600
BALL_SIZE: Final[int] = 20

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.cv._rootwindow.resizable(False, False)  # fixes the window size
screen.bgcolor("black")
screen.title("Breakout Pro")
screen.tracer(0)

# Designing Game Elements
paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()
bricks = Bricks()

# Starting Functionality for Game

# Moving paddle using keyboard up and down
screen.listen()
screen.onkeypress(fun=paddle.move_right, key="Right")
screen.onkeypress(fun=paddle.move_left, key="Left")
screen.onkeypress(fun=paddle.move_left, key="a")
screen.onkeypress(fun=paddle.move_right, key="d")


def ball_touched_border() -> tuple[bool, str]:
    """
    Checks if ball has collided with top, left or right borders
    :return: Returns True if collided with border, False if not and which border is touched as "top", "right" or "left"
    """
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    top_border_height = SCREEN_HEIGHT // 2
    left_border_at = - SCREEN_WIDTH // 2
    right_border_at = SCREEN_WIDTH // 2
    touched_left_border = ball_x - left_border_at < BALL_SIZE / 2
    touched_right_border = right_border_at - ball_x < BALL_SIZE / 2
    touched_top_border = top_border_height - ball_y < BALL_SIZE / 2
    if touched_top_border:
        return True, "top"
    if touched_right_border:
        return True, "right"
    if touched_left_border:
        return True, "left"
    return False, ""


def ball_touched_paddle():
    """
    Checks if ball has touched paddle
    :return: True if ball has touched paddle, False if not
    """
    paddle_edge_from_center_x = 40
    paddle_edge_from_center_y = 10
    paddle_edge_xcor_min = paddle.xcor() - paddle_edge_from_center_x
    paddle_edge_xcor_max = paddle.xcor() + paddle_edge_from_center_x
    paddle_edge_ycor_max = paddle.ycor() + paddle_edge_from_center_y
    # paddle_edge_ycor_min = paddle.ycor() - paddle_edge_from_center_y
    ball_edge_xcor = ball.xcor()
    ball_edge_ycor = ball.ycor() - BALL_SIZE / 2

    return (ball_edge_ycor < paddle_edge_ycor_max) and (paddle_edge_xcor_min <= ball_edge_xcor <= paddle_edge_xcor_max)


def if_ball_touched_bricks():
    """Checks if ball touches bricks and then hides that brick, increases score and returns"""
    all_bricks = [brick for brick in bricks.bricks if brick.isvisible()]
    x_edge_from_center = 22
    y_edge_from_center = 10
    ball_left_edge = ball.xcor() - BALL_SIZE // 2
    ball_right_edge = ball.xcor() + BALL_SIZE // 2
    ball_top_edge = ball.ycor() + BALL_SIZE // 2
    ball_bottom_edge = ball.ycor() - BALL_SIZE // 2
    for brick in all_bricks:
        brick_left_edge = brick.xcor() - x_edge_from_center
        brick_right_edge = brick.xcor() + x_edge_from_center
        brick_top_edge = brick.ycor() + y_edge_from_center
        brick_bottom_edge = brick.ycor() - y_edge_from_center

        max_diff = 1.2
        # Checking collision with left & right edge
        if brick_bottom_edge <= ball_top_edge and brick_top_edge >= ball_bottom_edge:
            # print("left and right check")
            if (0 < abs(brick_left_edge - ball_right_edge) < max_diff) and \
                    (0 < abs(brick_right_edge - ball_left_edge) < max_diff):
                ball.bounce_x()
                brick.hideturtle()
                scoreboard.brick_broken()
                scoreboard.update_score()
                return

        # Checking collision with top & bottom:
        if brick_left_edge <= ball_right_edge and brick_right_edge >= ball_left_edge:
            # print("top and bottom check")
            if (0 < abs(brick_top_edge - ball_bottom_edge) < max_diff)\
                    or (0 < abs(brick_bottom_edge - ball_top_edge) < max_diff):
                ball.bounce_y()
                brick.hideturtle()
                scoreboard.brick_broken()
                scoreboard.update_score()
                return


game_is_on = True
while game_is_on:
    screen.update()

    # controlling speed of the ball
    time.sleep(ball.movement_speed)
    ball.move()

    if ball_touched_border()[0]:
        if ball_touched_border()[1] == "top":
            ball.bounce_y()
        else:
            ball.bounce_x()

    if ball_touched_paddle():
        ball.bounce_y()
        ball.increase_speed()

    if_ball_touched_bricks()

    if all(list(map(lambda x: not x.isvisible(), bricks.bricks))):
        game_is_on = False
        scoreboard.game_over(True)

    if ball.ycor() + BALL_SIZE < paddle.ycor() - 20:
        game_is_on = False
        scoreboard.game_over(False)


screen.exitonclick()
