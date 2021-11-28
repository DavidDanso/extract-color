import turtle
import colorgram
from random import choice

screen = turtle.Screen()
turtle.colormode(255)
NUM = 10
DOT_SIZE = 65
class Palette:
    def __init__(self):
        self.colors = colorgram.extract('./images/img_1.gif', NUM)
        self.rgb_colors = []

    def get_color(self):
        for color in self.colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            new_color = (r, g, b)
            self.rgb_colors.append(new_color)

    def show_palette(self):
        timmy_the_turtle = turtle.Turtle()
        timmy_the_turtle.speed("fastest")
        timmy_the_turtle.penup()
        timmy_the_turtle.hideturtle()
        timmy_the_turtle.setheading(225)
        timmy_the_turtle.forward(300)
        timmy_the_turtle.setheading(0)
        number_of_dots = NUM
        for dots_count in range(1, number_of_dots + 1):
            timmy_the_turtle.dot(DOT_SIZE, choice(self.rgb_colors))
            timmy_the_turtle.forward(50)



    def get_rgb(self):
        txt_response = screen.textinput(title="Do you want to see the [rgb colors]?",
                                        prompt="The program displays '10' random colors from "
                                               "the image. Type 'Yes' for RGB COLORS "
                                               " or 'No' to end the program.").title()

        if txt_response == "Yes":
            turtle.clearscreen()
            turtle.hideturtle()
            screen.title("Click Screen to exit Program❌")
            screen.bgcolor("blue")
            turtle.color("white")
            turtle.write("The RGB COLORS has been saved into the 'rgb_color.txt' file.",
                         align='center', font=('Arial', 18, 'normal'))

            for rgb in self.rgb_colors:
                with open("rgb_colors.txt", mode="a") as colors:
                    colors.write(f"\n{str(rgb)}")

        else:
            turtle.clearscreen()
            turtle.hideturtle()
            screen.title("End Program!!❌")
            turtle.write("Click Screen to exit Program",
                         align='center', font=('Arial', 20, 'normal'))