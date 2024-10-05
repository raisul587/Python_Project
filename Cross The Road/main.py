from  turtle import Screen
from player import Player
from car_manager import Car
import time

player = Player()
car = Car()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
screen.onkeypress(player.move,"Up")
game_is_on = True
while game_is_on:ff
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
screen.exitonclick()