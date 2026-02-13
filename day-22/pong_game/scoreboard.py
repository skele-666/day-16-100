from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 80, "normal")
SCORE_LEFT_POS = (-100, 150)
SCORE_RIGHT_POS = (100, 150)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_LEFT_POS)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(SCORE_RIGHT_POS)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
