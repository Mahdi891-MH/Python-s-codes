import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color("lightblue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):

        random_x = random.randint(-275, 274)
        random_y = random.randint(-274, 248)
        self.goto(random_x, random_y)



