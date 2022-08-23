from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.pencolor("orange")
        self.update_score()

    def update_score(self):
        self.score +=1
        self.clear()
        self.write(arg="Score: " + str(self.score), move=False, align='center', font=('Arial', 15, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=False, align='center', font=('Arial', 25, 'bold'))
