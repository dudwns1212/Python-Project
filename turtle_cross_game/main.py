# 길건너기 게임 프로젝트
from turtle import Screen
from my_turtle import MyTurtle
from sideline import Sideline
from road import Road

screen = Screen()
screen.setup(width=600, height=420)
screen.title("turtle cross game")
screen.tracer(0)

# 내 본체
myCharacter = MyTurtle()

# 스크린 범위 확인
sideline = Sideline()

# 도로 선 그리기
position_y = -180
for _ in range(13):
    road = Road(position_y)
    position_y += 30

is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()