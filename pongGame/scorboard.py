from turtle import Turtle

class Scorboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scorboard()

    def update_scorboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 50, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 50, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scorboard()

    def r_point(self):
        self.r_score += 1
        self.update_scorboard()