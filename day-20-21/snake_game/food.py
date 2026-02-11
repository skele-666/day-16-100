from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)  # Make the food 10 x 10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))
