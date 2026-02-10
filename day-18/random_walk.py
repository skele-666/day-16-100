import turtle as t
import random

turtle = t.Turtle()
turtle.hideturtle()
turtle.pensize(10)
turtle.speed("fastest")
t.colormode(255)

def random_walk():
    n = random.randint(500, 1000)

    for _ in range(1, n):
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        turtle.color(colour)
        turtle.forward(30)

        turtle.setheading(random.randrange(0, 271, 90))

        # angle = random.randrange(0, 270, 90)
        # direction = random.randint(1, 2)

        # if direction == 1:
        #     turtle.left(angle)
        # else:
        #     turtle.right(angle)

random_walk()

