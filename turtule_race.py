from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=600,height=400)
directions=[-145,-85,-30,30,85,145]

colors=["yellow","red","blue","green","orange","purple"]
turtles=[]
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-280,y=directions[i])
    new_turtle.color(colors[i])
    turtles.append(new_turtle)

user_guess = screen.textinput("User input", "What do you think which turtle will win?")
if user_guess:
    set_race=True

while set_race:
    for _ in range(0,6):
        if turtles[_].xcor()>270:
            winner=turtles[_].pencolor()
            if winner==user_guess:
                print(f"You got it 😊! Winner is {user_guess} .")
                set_race = False
            else:
                print(f"You are wrong 🙁 ! winner is {winner}.")
                set_race = False
        turtles[_].forward(random.randint(0, 10))
Screen().exitonclick()
