import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player=Player()
car=CarManager()
scoreb=Scoreboard()

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

level_speed=0.1
screen.onkey(player.move,"Up")

game_is_on = True
c=0
while game_is_on:
    time.sleep(level_speed)
    screen.update()
    if c%10==0:
        car.generate_cars()
    car.move_cars()
    c+=1
    for i in car.cars_list:
        if i.distance(player)<20:
            scoreb.game_over()
            time.sleep(0.1)
            game_is_on = False
    if player.ycor()==200:
        scoreb.level_up()
        player.restart()
        level_speed*=0.2

screen.exitonclick()
