# import colorgram
# colors = colorgram.extract('img.jpg', 25)
# rgb_colors = []
#
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     col = (r, g, b)
#     rgb_colors.append(col)
#
# print(rgb_colors)

colors = [(229, 228, 226), (225, 223, 224), (199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59)]

# 점 그리기
from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
tim.speed("fastest")
screen.colormode(255)

def draw_dot():
    for _ in range(10):
        choice_color = random.choice(colors)
        tim.dot(10, choice_color)
        tim.penup()
        tim.fd(25)
    tim.left(90)
    tim.fd(25)
    tim.right(90)
    tim.setx(0)

for _ in range(10):
    draw_dot()

tim.home()
screen.exitonclick()