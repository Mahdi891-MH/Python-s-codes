import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Game")
screen.bgpic("road.png")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
is_reach = False
screen.listen()
screen.onkey(player.up, "Up")
counter = 0
while game_is_on:
    is_reach = False
    time.sleep(0.1)
    screen.update()
    if counter % 6 == 0:
        car_manager.generate_car()
    for car in car_manager.cars:
        if car.distance(player) < 23:
            game_is_on = False
            scoreboard.game_over()
    car_manager.move()
    if player.ycor() > 280 and not is_reach:
        scoreboard.refresh_score()
        is_reach = True
        player.goto(0, -280)
        car_manager.speed += 5
    counter += 1

screen.exitonclick()
