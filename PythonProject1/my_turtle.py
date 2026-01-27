from turtle import Turtle

START_POSITION = (0, -280)

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.player_speed = 10
        self.FINISH_LINE = 280
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)

    def move(self):
        self.setheading(90)
        self.forward(self.player_speed)

    def finish(self):
        self.goto(START_POSITION)

    def left_move(self):
        self.setheading(180)
        self.forward(self.player_speed)
    def right_move(self):
        self.setheading(0)
        self.forward(self.player_speed)
    def back_move(self):
        self.setheading(270)
        self.forward(self.player_speed)

    def speed_up_item(self):
        self.player_speed += 1


