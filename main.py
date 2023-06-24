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

width = 1500
height = 600
screen = display.set_mode((width, height))
clock = time.Clock()

grid = [[1 for i in range(51)] for j in range(51)]

grid[0][25] = 0

for i in range(1, 51):
    for j in range(51):
        grid[i][j] = grid[i - 1][j]
    if i <= 25:
        if i % 2 == 0:
            grid[i][25 - (i + 1) // 2] = 0
        else:
            grid[i][25 + (i + 1) // 2] = 0
    else:
        if i % 2 == 0:
            grid[i][50 - (i - 1) // 2] = 1
        else:
            grid[i][(i + 1 - 25) // 2 + 12] = 1

run = True

#1 is start page, 2 is game
curState = 2

while run:
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            run = False
        if e.type == QUIT:
            run = False
    if curState == 2:
        drawGame(screen, grid)
    display.flip()
    clock.tick(60)
quit()