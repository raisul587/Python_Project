from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Minion Pro', 20, 'normal')



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            h_score = int(data.read())
            self.high_score = h_score
        self.ht()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score:{self.score}      High Score:{self.high_score}" , move=False, align=ALIGNMENT, font=FONT)
        
    def plus_score(self):
        self.score+=1
        self.update_score()

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()