import turtle
screen = turtle.Screen()
screen.listen()

class Paddle(turtle.Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(5, 1)
        self.goto(self.x, self.y)

    def paddle_movement(self, up, down):
        def move_up():
            current_pos = self.ycor()
            if current_pos != 240:
                self.sety(current_pos + 30)

        def move_down():
            current_pos = self.ycor()
            if current_pos != -240:
                self.sety(current_pos - 30)

        screen.onkeypress(move_up, up)
        screen.onkeypress(move_down, down)
