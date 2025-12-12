import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=400)
drawer_turtle = Turtle()
drawer_turtle.speed("fastest")
drawer_turtle.color("red")
drawer_turtle.pensize(3)
drawer_turtle.penup()
drawer_turtle.hideturtle()
drawer_turtle.goto(275, 190)
drawer_turtle.pendown()
drawer_turtle.right(90)
drawer_turtle.forward(372)

user_bed = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "pink", "green", "orange", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-280, y_position[turtle_index])
    turtles.append(new_turtle)

is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 264:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bed == winning_color:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lose! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()