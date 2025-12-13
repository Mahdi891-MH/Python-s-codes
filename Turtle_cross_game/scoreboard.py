from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 14, "normal")
GAME_OVER_FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("white")
        self.hideturtle()
        self.goto(-330, 270)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.color("#c80047")
        self.penup()
        self.goto(0, 0)
        self.write("Game Over!", False, ALIGNMENT, GAME_OVER_FONT)

