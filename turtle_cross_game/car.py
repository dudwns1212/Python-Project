from turtle import Turtle

class Car(Turtle):
    def __init__(self, postion):
        super().__init__()
        self.shape("car")
        self.penup()
        self.goto()
