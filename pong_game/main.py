from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#instantiation
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
sc=Scoreboard()


screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()

screen.tracer(0)

screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"u")
screen.onkey(l_paddle.down,"d")

game_on=True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce()

    #If l_paddle or right paddle collide
    elif l_paddle.distance(ball)<50 and ball.xcor()<-320:
        ball.bounce_back()

    elif ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.bounce_back()


    #If right player miss the ball
    elif ball.xcor()>350 :
        ball.goto(0,0)
        ball.bounce_back()
        sc.update_lscore()

    elif ball.xcor()<-350:
        ball.goto(0, 0)
        ball.bounce_back()
        sc.update_rscore()
        ball.ball_speed=0.1

screen.exitonclick()
