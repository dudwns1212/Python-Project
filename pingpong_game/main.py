from turtle import Screen
from player_bar import Bar
from ball import Ball
import time
from sideline import Sideline
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pingpong-game")
screen.tracer(0)

sideline = Sideline()

bar1 = Bar()
bar1.create_bar1()

bar2 = Bar()
bar2.create_bar2()

screen.listen()
screen.onkeypress(bar1.up_bar, "w")
screen.onkeypress(bar1.down_bar, "s")
screen.onkeypress(bar2.up_bar, "Up")
screen.onkeypress(bar2.down_bar, "Down")

ball = Ball()

left_scoreboard = Scoreboard(-100)
right_scoreboard = Scoreboard(100)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # 벽에 부딫혔을 때
    if ball.xcor() > 385:
        left_scoreboard.get_score()
        ball.reset()
    elif ball.xcor() < -385:
        right_scoreboard.get_score()
        ball.reset()

    # 바에 부딫혔을 때
    if (ball.distance(bar1) < 54 and ball.xcor() < -360)  or (ball.distance(bar2) < 54 and ball.xcor() > 360) :
        ball.touch_bar()

    # 위 또는 아래 벽에 부딪쳤을 때
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.touch_wall()

screen.exitonclick()