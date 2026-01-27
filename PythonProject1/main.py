# 길건너기 게임 프로젝트
from turtle import Screen
from my_turtle import MyTurtle
from car import Car
from level import Score
from event import EventItem
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("turtle cross game")
screen.tracer(0)

# 내 본체
player = MyTurtle()

# 이벤트 리스너 등록
screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.left_move, "Left")
screen.onkeypress(player.right_move, "Right")
screen.onkeypress(player.back_move, "Down")

# 차 만들기
car = Car()

# 점수 객체
score = Score()

# 아이템
item = EventItem()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.drive()

    item.create_item()

    # 부딪치다
    for car_x in car.all_cars:
        if car_x.distance(player) < 20:
            score.game_over()
            is_game_on = False

    for it in item.all_item:
        if it.distance(player) < 15:
            if it.event_type == "speed_up":
                player.speed_up_item()
            elif it.event_type == "speed_low":
                car.speed_low_item()
            else:
                car.clear_item()
            it.ht()
            item.all_item.remove(it)

    if player.ycor() > player.FINISH_LINE:
        player.finish()
        car.speed_up()
        score.update_score()





screen.exitonclick()