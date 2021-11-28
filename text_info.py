from turtle import Turtle

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0, -120)
        self.write("Color Palette from Image", align="center", font=("Arial", 17, "normal"))


