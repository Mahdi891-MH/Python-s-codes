from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 13, "bold")
GAME_OVER_FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 268)
        self.record()
        self.refresh_score("food")

    def record(self):
        with open("High_score.txt") as file:
            self.high_score = file.read()
            return self.high_score

    def refresh_score(self, food_reward):
        self.clear()
        self.color("lightgreen")
        if food_reward == "food":
            self.score += 1
        elif food_reward == "reward":
            self.score += 3
        self.write(f"Score: {self.score}     High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def set_record(self):
        if self.score > int(self.high_score):
            with open("./High_score.txt", mode="w") as file:
                file.write(f"{self.score}")

    def game_over(self):
        self.set_record()
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over!", False, ALIGNMENT, GAME_OVER_FONT)


