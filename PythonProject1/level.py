from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.ht()
        self.goto(-200,250)
        self.update_score()

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)
