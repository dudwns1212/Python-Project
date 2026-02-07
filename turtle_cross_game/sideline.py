from turtle import Turtle

class Sideline(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color('black')
        self.penup()
        self.goto(300,210)
        self.pendown()
        self.goto(-300, 210)
        self.goto(-300, -210)
        self.goto(300, -210)
        self.goto(300,210)