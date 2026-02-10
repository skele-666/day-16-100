import turtle as t
import random
import math

from random import choice
turtle = t.Turtle()
turtle.hideturtle()
turtle.pensize(1)
turtle.speed("fastest")
t.colormode(255)

def draw_spirograph(gap_size):
    for i in range(int(360 / gap_size)):
        (x, y) = turtle.position()
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.color(colour)
        turtle.circle(90)

        turtle.setheading(turtle.heading() + gap_size)

draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()