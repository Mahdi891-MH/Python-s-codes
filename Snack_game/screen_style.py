from turtle import Turtle


class ScreenStyle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("lightgreen")
        self.speed("fastest")
        self.pensize(3)
        self.penup()
        self.goto(-290, -282)
        self.pendown()
        self.move(573)
        self.move(538)
        self.move(576)
        self.forward(538)

    def move(self, forward):
        self.forward(forward)
        self.left(90)