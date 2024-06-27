from turtle import Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high = int(file.read())
        self.ht()
        self.color("white")
        self.penup()
        self.goto(-100, 270)
        self.write(f"Score: {self.score}  ", align="center", font=("TimesNewRoman", 20, "normal"))

    def points(self):
        self.clear()
        self.score += 1
        self.goto(-100, 270)
        self.write(f"Score: {self.score} ", align="center", font=("TimesNewRoman", 20, "normal"))
        self.high_score()

    def high_score(self):
        if self.score > self.high:
            self.high = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high}")
        self.goto(100, 270)
        self.write(f"Highest Score: {self.high} ", align="center", font=("TimesNewRoman", 20, "normal"))

    def refresh(self):
        self.score = 0
        self.clear()
        self.high_score()
        self.goto(-100, 270)
        self.write(f"Score: {self.score} ", align="center", font=("TimesNewRoman", 20, "normal"))


