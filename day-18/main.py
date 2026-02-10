from turtle import Turtle, Screen
from random import choice
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkSeaGreen4")
timmy.turtlesize(3)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Draw shapes
def draw_shape(sides):
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(360 / sides)

for n in range(3, 11):
    timmy.color(choice(colours))
    draw_shape(n)

# Move timmy
timmy.penup()
timmy.goto(-200, 0)
timmy.pendown()
timmy.right(90)

# Draw dashed line
for _ in range (15):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
