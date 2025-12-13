from turtle import Turtle


class DrawTimer(Turtle):
    def __init__(self):
        super().__init__()
        self.forward_distance = [81, 8, 81, 9]
        self.time_bar()

    def time_bar(self):
        self.hideturtle()
        self.color("lightgreen")
        self.speed("fastest")
        self.pensize(1)
        self.penup()
        self.goto(200, 280)
        for distance in self.forward_distance:
            self.move(distance)
        self.penup()
        self.time_line()
        self.goto(277, 276)

    def time_line(self):
        self.color("lightgreen")
        self.pensize(5)
        self.goto(202, 276)
        self.pendown()
        self.pensize(5)
        self.forward(75)

    def move(self, forward):
        self.pendown()
        self.forward(forward)
        self.right(90)

    def decrease_time(self):
        self.shape("square")
        self.pensize(6)
        self.color("black")
        self.backward(1.2)
