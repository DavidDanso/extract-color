from tkinter import PhotoImage
from turtle import Screen, Shape

screen = Screen()
class Image:
    def __init__(self):
        # substitute 'subsample' for 'zoom' if you want to go smaller:
        image = "./images/img_1.gif"
        smaller = PhotoImage(file=image).subsample(2, 2)
        screen.addshape("smaller", Shape("image", smaller))
        screen.tracer(0)

