from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# Get user colour
def get_colour(screen):
    colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]
    user_colour = screen.textinput("Choose snake colour", "Pick a colour for your snake:").lower()
    while user_colour not in colours:
        if user_colour == "":
            user_colour = "white"
            return user_colour
        user_colour = screen.textinput("Invalid colour", "Try again:")
    return user_colour


# Create screen object
def create_screen():
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    return screen


# Draw screen border
def draw_border():
    border_pen = Turtle()
    border_pen.hideturtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.pensize(3)

    border_pen.penup()
    # Go to the bottom-left corner (slightly inside the 600x600 limit)
    border_pen.goto(-290, -290)
    border_pen.pendown()

    # Draw the square
    for _ in range(4):
        border_pen.forward(580)
        border_pen.left(90)


def setup_controls(snake, screen):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


# Detect collision with food, wall and tail
def check_collisions(snake, food, scoreboard, file_path):
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard(file_path)
        snake.reset()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset_scoreboard(file_path)
            snake.reset()


# Snake game
def snake_game():
    screen = create_screen()
    draw_border()

    snake = Snake(get_colour(screen))
    setup_controls(snake, screen)
    food = Food()
    scoreboard = Scoreboard()

    # Game loop
    game_is_on = True
    while game_is_on:
        screen.update()  # Update here so the snake moves as a whole
        time.sleep(0.1)  # Add pacing to the snake's movements

        snake.move()
        check_collisions(snake, food, scoreboard, "./data.txt")

    screen.exitonclick()


def main():
    snake_game()


if __name__ == "__main__":
    main()
