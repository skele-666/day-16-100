from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 3
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reached_finish(self):
        # Check if finished level
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
