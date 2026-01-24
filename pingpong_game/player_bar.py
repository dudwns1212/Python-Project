from turtle import Turtle

class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.resizemode("user")
        self.turtlesize(5,1,1)
        self.penup()

    def create_bar1(self):
        self.goto(-380,0)

    def create_bar2(self):
        self.goto(380,0)

    def up_bar(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_bar(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)