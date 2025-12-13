import random
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from screen_style import ScreenStyle
from reward import Reward
from draw_timer import DrawTimer
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
screen_style = ScreenStyle()
scoreboard = Scoreboard()
draw_timer = DrawTimer()
draw_timer.clear()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
random_reward = random.randint(11, 13)
is_reward = False
is_time_bar = False
reward_time = 0
while game_is_on:
    screen.update()
    time.sleep(0.15)
    if is_reward:
        if not is_time_bar:
            draw_timer.time_bar()
            is_time_bar = True
        draw_timer.decrease_time()
        reward_time += 1
    snake.move()
    if snake.head.distance(food) < 10:
        if scoreboard.score % random_reward == 0 and scoreboard.score != 0:
            reward = Reward()
            is_reward = True
        food.hideturtle()
        food = Food()
        scoreboard.refresh_score("food")
        snake.expand()
    if is_reward:
        if reward_time > 60:
            reward.hideturtle()
            reward_time = 0
            is_reward = False
            draw_timer.clear()
            is_time_bar = False
        if snake.head.distance(reward) < 12:
            reward.hideturtle()
            scoreboard.refresh_score("reward")
            reward_time = 0
            is_reward = False
            draw_timer.clear()
            is_time_bar = False
    if snake.head.xcor() > 285 or snake.head.xcor() < -288 or snake.head.ycor() > 254 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()
        # turtle.onscreenclick(Reward.get_mouse_click_coor)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()


