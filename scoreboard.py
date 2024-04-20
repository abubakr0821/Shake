from turtle import Turtle, Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def update(self):
        self.write(f"Score {self.score}", align="center")

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", font=("Verdana", 24, "normal"), align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
