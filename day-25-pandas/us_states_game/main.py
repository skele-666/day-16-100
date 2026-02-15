import turtle, pandas


def create_screen(image):
    screen = turtle.Screen()
    screen.title("U.S States Game")
    screen.addshape(image)
    turtle.shape(image)
    return screen


# List of states to learn
def generate_csv(guessed_states, all_states):
    missing_states = []
    for state in all_states:
        if state not in guessed_states:
            missing_states.append(state)

    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")


def us_states_game():
    image = "blank_states_img.gif"
    screen = create_screen(image)
    data = pandas.read_csv("./50_states.csv")
    all_states = data.state.to_list()

    guessed_states = []
    while len(guessed_states) < 50:
        answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                        f"{len(guessed_states)}/50 States Correct\nWhat's another state's name?").title()

        if answer_state == "Exit":
            generate_csv(guessed_states, all_states)
            break

        while answer_state in guessed_states:
            answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                            f"{len(guessed_states)}/50 States Correct\nYou already guessed that!").title()

        if answer_state in all_states:
            guessed_states.append(answer_state)
            print(guessed_states)
            t = turtle.Turtle()
            t.color("black")
            t.hideturtle()
            t.penup()

            current_state_row = data[data.state == answer_state]
            t.goto(current_state_row.x.item(), current_state_row.y.item())
            t.write(answer_state)


def main():
    us_states_game()


if __name__ == "__main__":
    main()
