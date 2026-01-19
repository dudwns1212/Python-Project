from turtle import Turtle, Screen

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forwards)

# screen.exitonclick()

# 에치어스케치 앱 만들기
# def w_forwards():
#     tim.forward(10)
#
# def s_forwards():
#     tim.backward(10)
#
# def a_counter_clockwise():
#     tim.left(10)
#
# def d_clockwise():
#     tim.right(10)
#
# def c_clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkeypress(w_forwards, "w")
# screen.onkeypress(s_forwards, "s")
# screen.onkeypress(a_counter_clockwise, "a")
# screen.onkeypress(d_clockwise, "d")
# screen.onkey(c_clear_drawing, "c")

# 터틀 레이싱 게임 프로젝트
is_race_on = False
import random
all_turtles = []

colors = ["red","orange","yellow","green","blue","purple"]

screen = Screen()
screen.setup(width=500, height=400) # screen의 크기를 지정
user_bet = screen.textinput(title="Make you bet", prompt="Witch turtle will win the race? Enter a color: ")
y_positions = [-100, -60, -20, 20, 60, 100]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    # 임의의 숫자 가져오기
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            if user_bet == winner:
                print(f"You correct! winner is {winner}")
            else:
                print(f"You lose! winner is {winner}")
            break
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()