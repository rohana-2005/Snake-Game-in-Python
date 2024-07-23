from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))


    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier", 15, "normal"))
        self.goto(0, -50)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))
