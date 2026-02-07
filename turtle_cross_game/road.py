from turtle import Turtle

class Road(Turtle):
    def __init__(self, position):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(300, position)
        self.setheading(180)
        for _ in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)