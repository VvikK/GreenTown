from pygame import *
from drawFunctions import *
from logicFunctions import *
from buildings import *

init()

WHITE = Color("#FFFFFF")

width = 1500
height = 600
screen = display.set_mode((width, height))
clock = time.Clock()

run = True

#grid initialization
grid = [[1 for i in range(51)] for j in range(51)]
grid = gridCreation(grid)

#initializing surfaces
grass = Surface((5000, 1000))
grassCreation(grid, grass)

#1 is start page, 2 is game
curState = 2

while run:
    
    x, y = mouse.get_pos()
    k, l = hoverDiamond(grid, x, y)
    #print(x, y, "yes!")
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            run = False
        if e.type == QUIT:
            run = False
        
    if curState == 2:
        drawGame(screen, grass)
    if k != -1:
        draw.rect(screen, WHITE, Rect(l * 98 - (k % 2) * 49 - 2000 + 49, k * 28 + 14, 10, 10))
        #draw.rect(screen, WHITE, Rect(x, y, 10, 10))
    display.flip()
    clock.tick(60)
    #delta_time = clock.tick(60)/1000.0
quit()