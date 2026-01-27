from turtle import Turtle
import random as rd

ITEM = ["speed_low", "clear", "speed_up"]

class EventItem:
    def __init__(self):
        self.all_item = []

    def create_item(self):
        dice = rd.randint(1,500)
        if dice == 1:
            new_item = Turtle("circle")
            new_item.color("cyan")
            new_x = rd.randint(-280,280)
            new_y = rd.randint(-250,250)
            new_item.penup()
            new_item.goto(new_x,new_y)

            new_item.event_type = rd.choice(ITEM)
            self.all_item.append(new_item)
