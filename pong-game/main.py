from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    def end_game():
        global game_is_on
        game_is_on = False

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if right paddle misses
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset()

    #Detect if left paddle misses
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset()

    screen.onkey(end_game, "space")
    if not game_is_on:
        scoreboard.game_over()

screen.exitonclick()


