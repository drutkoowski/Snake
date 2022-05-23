from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
current_path = os.getcwd()
with open(f"{current_path}\score.txt", mode="r") as file:
    HIGHEST_SCORE = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGHEST_SCORE
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(f"{current_path}\score.txt", mode="w") as f:
                f.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
