from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.cars = random.randint(1,4)
        self.generate_cars()
        self.hideturtle()


    def generate_cars(self):
        for i in range(self.cars):
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(random.randint(240,270),random.randint(-200,200))
            self.cars_list.append(new_car)

    def move_cars(self):
        for _ in self.cars_list:
            _.backward(MOVE_INCREMENT)
