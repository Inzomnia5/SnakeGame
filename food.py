from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("green")
        self.speed("fastest")
        self.food_respawn()

    def food_respawn(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)  # 260max Yheight so food doesn't spawn IN scoreboard
        self.goto(random_x, random_y)
