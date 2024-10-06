from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Minion Pro', 20, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"score:{self.score}" , move=False, align=ALIGNMENT, font=FONT)
        
    def plus_score(self):
        self.score+=1
        self.clear()
        self.write(f"score:{self.score}" , move=False, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER...." , move=False, align=ALIGNMENT, font=FONT)