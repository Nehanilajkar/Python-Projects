from turtle import Turtle
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.snake_head=self.turtles[0]

    def create_snake(self):
        for i in range(3):
            self.extend_snake()
            self.turtles[i].goto(i * 20, 0)

    def move(self):
        for _ in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[_ - 1].xcor()
            y = self.turtles[_ - 1].ycor()
            self.turtles[_].goto(x, y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() !=DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def extend_snake(self):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color("white")
        self.turtles.append(new_turtle)


