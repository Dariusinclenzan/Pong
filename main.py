import turtle
from paddle import Paddle
import paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()
r_movement = r_paddle.paddle_movement("Up", "Down")
l_movement = l_paddle.paddle_movement("w", "s")

game_on = True
while game_on:
    screen.update()
    ball.ball_movement()
    time.sleep(ball.ball_speed)


    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.wall_bounce()

    elif ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 450:
        ball.out_of_bounds()
        score.left_score()
        time.sleep(0.5)
    elif ball.xcor() < -450:
        ball.out_of_bounds()
        score.right_score()
        time.sleep(0.5)








screen.exitonclick()