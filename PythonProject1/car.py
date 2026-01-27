from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","indigo","purple"]
INCREASE_SPEED = 5

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        dice = random.randint(1,6)
        if dice == 1:
            new_car = Turtle("square")
            new_car.resizemode("user")
            new_car.shapesize(1,2,1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.penup()
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += INCREASE_SPEED

    def speed_low_item(self):
        self.car_speed /= 2

    def clear_item(self):
        for car in self.all_cars:
            car.ht()
        self.all_cars.clear()