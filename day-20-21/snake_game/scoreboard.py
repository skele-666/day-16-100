from turtle import Turtle
import os.path

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # High score stuff
        # Create hs file if doesnt exist
        file_path = "./data.txt"

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("0")

        with open(file_path, "r") as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

        self.color("white")

        # Position text
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self, score_file):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(score_file, "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
