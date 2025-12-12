import random
import turtle
from turtle import Turtle as t, Screen

timmy = t()
turtle.colormode(255)
timmy.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def draw(gap_size):
    for i in range(360//gap_size+1):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap_size)

draw(1)

screen = Screen()
screen.exitonclick()