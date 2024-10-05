from turtle import Screen
from draw import Draw
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Famous Pong Arcade Game")
screen.tracer(0)

# Draw center line and boundary
draw = Draw()
draw.draw_line()

# Create paddles for the right and left players
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))

# Set up paddle movement controls - Move paddle when Key is pressed
screen.listen()  # Listen for keyboard input
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Create ball and scoreboard
ball = Ball((0, 0))   # Ball starts at the center of the screen
score = Score()       # Initialize score display

# Main game loop
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()              # Update the screen after each iteration
    ball.move_ball()

    # Detect collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()          # Make the ball bounce when it hits the wall

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()          # Make the ball bounce when it hits a paddle

    # Check if the right paddle misses the ball
    if ball.xcor() > 350:
        ball.reset_position()    # Reset ball to the center
        score.plus_left()        # Left player scores a point

    # Check if the left paddle misses the ball
    if ball.xcor() < -350:
        ball.reset_position()    # Reset ball to the center
        score.plus_right()       # Right player scores a point

# Exit the game when the window is clicked
screen.exitonclick()
