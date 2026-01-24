from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.position_x = 20
        self.position_y = 10
        self.penup()

    def move(self):
        new_x = self.xcor() + self.position_x
        new_y = self.ycor() + self.position_y
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0,0)
        self.position_x *= -1
        self.position_y *= -1

    def touch_bar(self):
        self.position_x *= -1

    def touch_wall(self):
        self.position_y *= -1
