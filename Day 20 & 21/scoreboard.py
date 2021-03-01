from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()