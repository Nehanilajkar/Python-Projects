from turtle import Turtle
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.score=0
        self.penup()
        self.goto(-270, 250)
        self.write(f"Level: {self.score}" , move=False, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over",move=False,font=FONT)

    def level_up(self):
        self.clear()
        self.score+=1
        self.write(f"Level: {self.score}",move=False,font=FONT)

