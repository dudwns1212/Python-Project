from turtle import Turtle

class Sideline(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.color('white')
        self.penup()
        self.goto(400,300)
        self.pendown()
        self.goto(-400, 300)
        self.goto(-400, -300)
        self.goto(400, -300)
        self.goto(400,300)