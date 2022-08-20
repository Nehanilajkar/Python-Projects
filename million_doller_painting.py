from turtle import Turtle,Screen
import random

turtle_obj=Turtle()

l=[(240, 240, 239), (230, 232, 237), (232, 238, 235), (239, 233, 236), (187, 161, 122),
   (14, 25, 57), (67, 94, 134), (145, 87, 55), (139, 158, 184), (139, 73, 94), (68, 15, 6),
   (186, 141, 160), (24, 51, 126), (71, 110, 85), (129, 29, 51), (149, 21, 8), (183, 148, 46),
   (138, 169, 151), (215, 206, 136), (62, 18, 30), (93, 118, 178), (187, 93, 115), (187, 97, 82),
   (14, 34, 29), (97, 146, 129), (222, 174, 188), (33, 84, 64), (162, 208, 183), (180, 186, 211), (91, 145, 154)]

Screen().colormode(255)

turtle_obj.penup()
x,y=-250,-250
turtle_obj.setpos(x,y)

for j in range(10):
    for i in range(10):
        # turtle_obj.pencolor()
        turtle_obj.penup()
        turtle_obj.dot(15,random.choice(l))
        turtle_obj.forward(50)
        turtle_obj.pendown()
        turtle_obj.penup()
    y +=50
    
    turtle_obj.setpos(x,y)
    
turtle_obj.hideturtle()
Screen().exitonclick()
