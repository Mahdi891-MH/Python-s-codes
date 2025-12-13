import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        new_car = Turtle("square")
        new_car.shape("square")
        new_car.penup()
        y_position = random.randint(-250, 250)
        new_car.color(random.choices(COLORS))
        new_car.goto(400, y_position)
        new_car.left(180)
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

