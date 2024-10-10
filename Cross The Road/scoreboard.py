from turtle import Turtle, Screen
FONT = ("Courier", 24, "bold")
LEVEL = 1

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = LEVEL
        self.penup()
        self.ht()

#initially setting the score position
    def init_score(self):
        self.goto(-280, 280)
        self.write(f"Level: {self.level}",FONT)

    def next_level(self):
        self.level+=1
        self.clear()
        self.init_score()


    def game_over(self):
        self.goto(0,0)
        self.write("G.A.M.E   O.V.E.R",FONT)