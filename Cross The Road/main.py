from  turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Score
import time

player = Player()
car = Car()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Score()

#Setting up the Keyboard button to control player
screen.listen()
screen.onkeypress(player.move,"Up")

#main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    score.init_score()

    #Detect Collision with Cars and Player
    for cars in car.all_cars:
        if player.distance(cars)<28:
            score.game_over()
            game_is_on=False

    #Upgrade level
    if player.ycor()>290:
        player.goto_start()
        car.increase_speed()
        score.next_level()

screen.exitonclick()