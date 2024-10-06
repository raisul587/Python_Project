from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.move_food()
    def move_food(self):
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        self.goto(x,y)