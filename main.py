from pygame import *
from drawFunctions import *
from logicFunctions import *

init()

WHITE = Color("#FFFFFF")

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
        self.image_frames = image_frames hii
        self.cap = cap

width = 1500
height = 600
screen = display.set_mode((width, height))
clock = time.Clock()

grid = [[1 for i in range(9)] for j in range(9)]

grid[0][4] = 0

for i in range(1, 9):
    for j in range(9):
        grid[i][j] = grid[i - 1][j]
    if i <= 4:
        if i % 2 == 0:
            grid[i][4 - (i + 1) // 2] = 0
        else:
            grid[i][4 + (i + 1) // 2] = 0
    else:
        if i % 2 == 0:
            grid[i][4 - (i - 1) // 2] = 1
        else:
            grid[i][(i + 1 - 7) // 2 + 4] = 1

run = True

#1 is start page, 2 is game
curState = 2

while run:
    
    x, y = mouse.get_pos()
    #k, l = hoverDiamond(grid, x, y)
    #print(x, y, "yes!")
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            run = False
        if e.type == QUIT:
            run = False
        
    if curState == 2:
        drawGame(screen, grid)
    #if k != -1:
    #draw.rect(screen, WHITE, Rect(l * 98 - (k % 2) * 49 - 2000 + 49, k * 28 + 14, 10, 10))
    draw.rect(screen, WHITE, Rect(x, y, 10, 10))
    display.flip()
    clock.tick(60)
quit()