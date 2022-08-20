from turtle import Turtle,Screen
import random
turle_obj=Turtle()
turle_obj.shape("turtle")
turle_obj.pensize(8)
turle_obj.speed(10)
colors=["medium blue","forest green","gold","dark orchid","red","indigo","sienna","cyan","lime"]
def make_shape(sides):
    turle_obj.color(random.choice(colors))
    deg = 360 // sides
    for i in range(sides):
        turle_obj.forward(100)
        turle_obj.right(deg)

for _ in range(3,11):
    make_shape(_)
screen=Screen()
screen.exitonclick()
