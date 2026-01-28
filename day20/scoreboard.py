from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_text.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore_text.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()