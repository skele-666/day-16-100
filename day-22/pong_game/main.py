import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Create screen object
def create_screen():
    screen_obj = Screen()
    screen_obj.setup(800, 600)
    screen_obj.bgcolor("black")
    screen_obj.title("Pong")
    screen_obj.tracer(0)
    return screen_obj


# Draw screen border
def draw_border():
    border_pen = Turtle()
    border_pen.hideturtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.pensize(3)

    border_pen.penup()
    border_pen.goto(-380, -280)
    border_pen.pendown()

    for _ in range(2):
        border_pen.forward(760)  # Bottom and Top sides
        border_pen.left(90)
        border_pen.forward(560)  # Right and Left sides
        border_pen.left(90)

# Draw center line
def draw_center_line():
    line = Turtle()
    line.hideturtle()
    line.speed(0)
    line.color("white")
    line.pensize(2)
    line.penup()

    # Start exactly at the top border (Y=280)
    line.goto(0, 280)
    line.setheading(270)  # Point Down

    # 560 total pixels / 40 (20 down + 20 gap) = 14 segments
    for _ in range(16):
        line.pendown()
        line.forward(18)
        line.penup()
        line.forward(18)


# Setup controls
def setup_controls(screen, paddle, up_key, down_key):
    screen.listen()
    screen.onkey(paddle.up, up_key)
    screen.onkey(paddle.down, down_key)


def pong():
    # Setup
    game_window = create_screen()
    draw_border()
    draw_center_line()
    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0))
    setup_controls(game_window, r_paddle, "Up", "Down")
    setup_controls(game_window, l_paddle, "w", "s")
    ball = Ball()
    scoreboard = Scoreboard()

    # Game loop
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        game_window.update()
        ball.move()
        ball.detect_collision(l_paddle, r_paddle)
        ball.detect_out_of_bounds()

    game_window.exitonclick()


def main():
    pong()


if __name__ == "__main__":
    main()
