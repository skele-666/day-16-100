import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def create_screen():
    screen_obj = Screen()
    screen_obj.setup(width=600, height=600)
    screen_obj.tracer(0)
    return screen_obj


def draw_border():
    border_pen = Turtle()
    border_pen.hideturtle()
    border_pen.speed(0)
    border_pen.pensize(3)

    border_pen.penup()
    border_pen.goto(-280, -280)
    border_pen.pendown()

    # Draw a square (all sides are 560)
    for _ in range(4):
        border_pen.forward(560)
        border_pen.left(90)


# Setup controls
def setup_controls(screen, player):
    screen.listen()
    screen.onkey(player.up, "Up")


def check_collision(car_manager, player):
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            return True
    return False


def turtle_game():
    screen = create_screen()
    draw_border()

    player = Player()
    setup_controls(screen, player)

    car_manager = CarManager()
    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with car
        if check_collision(car_manager, player):
            game_is_on = False
            scoreboard.game_over()

        # Detect successful crossing
        if player.reached_finish():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

    screen.exitonclick()


def main():
    turtle_game()


if __name__ == "__main__":
    main()
