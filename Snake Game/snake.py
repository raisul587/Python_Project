from turtle import Turtle
DISTANCE = 20
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    
    def create_snake(self):
        x=-20
        y=0
        for _ in range (3):
            self.add_body_part((x,y))
            x += 20
    def add_body_part(self,position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        self.snake_body.append(snake)
        snake.goto(position)
    def extend(self):
        tail_position = self.snake_body[-1].position()
        self.add_body_part(tail_position)
    def move(self):
        for snake in range(len(self.snake_body)-1,0,-1):
            newx = self.snake_body[snake-1].xcor()
            newy = self.snake_body[snake-1].ycor()
            self.snake_body[snake].goto(newx,newy)
        self.head.forward(DISTANCE)

    def reset(self):
        for body in self.snake_body:
            body.goto(1000,1000)
        self.snake_body.clear ()
        self.create_snake()
        self.head = self.snake_body[0]
        self.move()

    #intrigrating game with keyboard
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)