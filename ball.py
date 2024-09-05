import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 2
        self.y = 1
        self.ball_speed = 0.01

    def ball_movement(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x + self.x, current_y + self.y)

    def wall_bounce(self):
        self.y *= -1

    def paddle_bounce(self):
        self.x *= -1
        self.ball_speed *= 0.9

    def out_of_bounds(self):
        self.home()
        self.ball_speed = 0.01


