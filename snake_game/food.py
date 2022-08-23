from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.new_position()
        self.penup()
        self.shape("circle")
        self.shapesize(0.7)
        self.color("blue")
        self.speed("fastest")


    def new_position(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
