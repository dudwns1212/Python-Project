from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.goto(position, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 24, "normal"))

    def get_score(self):
        self.score += 1
        self.update_score()