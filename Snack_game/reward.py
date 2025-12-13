from turtle import Turtle
import random


class Reward(Turtle):
    def __init__(self):
        super().__init__()
        self.color("lightgreen")
        self.shape("circle")
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.penup()
        self.speed("fastest")
        random_x = random.randint(-275, 274)
        random_y = random.randint(-274, 248)
        self.goto(random_x, random_y)

    # def get_mouse_click_coor(x, y):
    #     print(x)
    #     print(y)