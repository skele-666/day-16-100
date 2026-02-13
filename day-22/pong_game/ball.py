from turtle import Turtle

MOVE_INCREMENT = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # Positive values move right (x) and up (y)
        self.x_move = MOVE_INCREMENT
        self.y_move = MOVE_INCREMENT
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.speed(self.move_speed)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        # Reverse direction of y coordinate to "bounce"
        self.y_move *= -1  # Literally flip it

    def detect_collision(self, l_paddle, r_paddle):
        # Detect collision with wall
        if self.ycor() > 260 or self.ycor() < -260:
            self.bounce_y()

        # Detect collison with paddles
        if (self.distance(r_paddle) < 50 and self.xcor() > 320) or (
                self.distance(l_paddle) < 50 and self.xcor() < -320):
            self.bounce_x()

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    def detect_out_of_bounds(self, scoreboard):
        # Right side
        if self.xcor() > 380:
            scoreboard.l_point()
            self.reset_position()
        elif self.xcor() < -380:
            scoreboard.r_point()
            self.reset_position()
