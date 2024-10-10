from snake import Snake
import time
from turtle import Turtle, Screen
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.listen()
skip_initial_frames = 5
play = True
while play:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        score.plus_score()
        snake.extend()
        food.move_food()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_score()
        snake.reset()

    if skip_initial_frames > 0:
        skip_initial_frames -= 1
    else:
        for body in snake.snake_body[1:]:
            if snake.head.distance(body) < 10:
                score.reset_score()
                snake.reset()


screen.exitonclick()