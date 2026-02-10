from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [80, 50, 20, -10, -40, -70]

def get_user_bet():
    bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour:").lower()
    while bet not in colours:
        bet = screen.textinput("Make your bet", "Try again:")
    return bet

user_bet = get_user_bet()

# Create turtle racers
turtles = []
for i in range(6):
    turtle = Turtle("turtle")
    turtle.color(colours[i])
    turtle.penup()
    turtle.goto(-230, y_pos[i])
    turtles.append(turtle)

# Each instance of turtle will have different state

# Run race
is_race_on = True
while is_race_on:
    # Generate random speed for each turtle and move turtle
    for turtle in turtles:
        # Check if turtle won
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            # Check if user bet correctly
            if winning_colour == user_bet:
                print(f"You won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You lost. The {winning_colour} turtle is the winner!")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
