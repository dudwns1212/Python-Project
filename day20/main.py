from turtle import Screen, Turtle
from snake import Snake
import time

from snake import Snake

# 초기 설정(스크린 크기, 배경, 타이틀)
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 뱀 움직이기
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()