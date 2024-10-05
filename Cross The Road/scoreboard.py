from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.ht()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}",FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("G.A.M.E   O.V.E.R",FONT)