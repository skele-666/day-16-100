import turtle as t

timmy = t.Turtle()

def etch_a_sketch(turtle, screen):
    def clear():
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    screen.listen()
    screen.onkey(lambda: turtle.forward(10), "w")
    screen.onkey(lambda: turtle.backward(10), "s")
    screen.onkey(lambda: turtle.left(10), "a")
    screen.onkey(lambda: turtle.right(10), "d")
    screen.onkey(clear, "c")


def main():
    screen = t.Screen()
    etch_a_sketch(timmy, screen)
    screen.exitonclick()

if __name__ == "__main__":
    main()