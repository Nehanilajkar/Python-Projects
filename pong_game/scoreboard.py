from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score=0
        self.score()

    def score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,move=False,font=("courier",60,"normal"))
        self.goto(100, 200)
        self.write(self.r_score, move=False, font=("courier", 60, "normal"))

    def update_lscore(self):
        self.l_score+=1
        self.score()

    def update_rscore(self):
        self.r_score+=1
        self.score()
