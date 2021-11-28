from turtle import Screen
from set_image import Image
from image_pos import Position
from text_info import Text
from palette import Palette

"""
To set a new image: Go to the 'set_image.py' and the 'palette.py' file
to set a new image for the program to extract the colors for you!! Happy Coding 😄 
"""
screen = Screen()
screen.title("Color Extractor 🎨")
set_image = Image()
image_position = Position()
txt = Text()
colors = Palette()

colors.get_color()
colors.show_palette()
colors.get_rgb()
screen.exitonclick()
