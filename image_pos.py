from turtle import Turtle, Screen

screen = Screen()
class Position:
    def __init__(self):
        tim_the_turtle = Turtle("smaller")
        tim_the_turtle.penup()
        tim_the_turtle.goto(0, 100)
        screen.update()
