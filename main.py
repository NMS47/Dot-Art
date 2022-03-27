import turtle

import colorgram
from turtle import Turtle, Screen
import random

#
# colors = colorgram.extract('elchanta.jpg', 20)
#
# color_list = []
# num_of_color = 0
#
# for num in range(20):
#
#     colorete = colors[num_of_color]
#     color_list.append((colorete.rgb[0], colorete.rgb[1], colorete.rgb[2]))
#     num_of_color += 1
#
# print(color_list)

rgb_colors = [(196, 161, 17), (52, 97, 154), (159, 47, 58), (136, 34, 57), (30, 61, 48), (22, 35, 62), (23, 50, 117),
              (225, 75, 41), (39, 127, 61), (203, 120, 173), (232, 170, 203), (215, 147, 65), (37, 76, 54),
              (191, 79, 41), (148, 189, 203), (51, 42, 40)]
turtle.colormode(255)
gus = Turtle()
my_screen = Screen()

gus.speed(1)
gus.penup()
gus.setposition(-200.0 , -200.0)

for _ in range(5):
    direc = "right"
    if direc == "right":
        for _ in range(9):
            gus.dot(20, random.choice(rgb_colors))
            gus.forward(40.0)
            gus.dot(20, random.choice(rgb_colors))
        gus.left(90)
        gus.forward(40.0)
        gus.left(90)
        direc = "left"
    if direc == "left":
        for _ in range(9):
            gus.dot(20, random.choice(rgb_colors))
            gus.forward(40.0)
            gus.dot(20, random.choice(rgb_colors))
        gus.right(90)
        gus.forward(40.0)
        gus.right(90)
        direc = "right"





my_screen.exitonclick()