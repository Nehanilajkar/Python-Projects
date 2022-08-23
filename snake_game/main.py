from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_obj=Snake()
food=Food()
scoreb=Scoreboard()

screen.listen()

screen.onkey(snake_obj.up,"Up")
screen.onkey(snake_obj.down,"Down")
screen.onkey(snake_obj.left,"Left")
screen.onkey(snake_obj.right,"Right")

play='on'
while play=='on':
    screen.update()
    sleep(0.1)
    snake_obj.move()
    #Detect snake touch the food
    if snake_obj.snake_head.distance(food) < 15:
        food.new_position()
        snake_obj.extend_snake()
        scoreb.update_score()

    #Detect wall collision
    if snake_obj.snake_head.xcor()>280 or snake_obj.snake_head.xcor() <-280 or snake_obj.snake_head.ycor() > 280 or snake_obj.snake_head.ycor() <-280:
        scoreb.game_over()
        play='off'
