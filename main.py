from pygame import *
from drawFunctions import *
from logicFunctions import *

init()

class Currency(object):
    def __int__ (self, value, name, image_frames, cap):
        self.value = value
        self.name = name
        self.image_frames = image_frames
        self.cap = cap

class Building(object):
    def __int__ (self, value, name, image_frames, cap):
        self.value = value
        self.name = name
        self.image_frames = image_frames
        self.cap = cap


width = 1000
height = 600
screen = display.set_mode((width, height))
clock = time.Clock()

run = True

#1 is start page, 2 is game
curState = 1

while run:
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            run = False
    if curState == 1:
        draw
    display.flip()
    clock.tick(60)