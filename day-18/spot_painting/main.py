import colorgram, turtle as t, random

# I got ChatGPT to help..........

# Create colour array
rgb_colours = []
colours = colorgram.extract('image.jpg', 30)
for colour in colours:
    rgb_colours.append((colour.rgb.r, colour.rgb.g, colour.rgb.b))


def spot_painting():
    # Turtle
    turtle = t.Turtle()
    turtle.hideturtle()
    t.colormode(255)
    turtle.penup()

    # Starting position
    start_x = 220
    start_y = -250

    # Draw spot painting
    for row in range(10):
        print(row)
        # Move up to next row
        turtle.goto(start_x, start_y + (row * 50))
        # Row starts as 0 so this works
        for col in range(10):
            # Draw dot
            turtle.dot(20, random.choice(rgb_colours))
            # Move left to next dot
            turtle.backward(50)


spot_painting()
t.Screen().exitonclick()
