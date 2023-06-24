from pygame import *
from drawFunctions import *
from logicFunctions import *
from buildings import *

init()

WHITE = Color("#FFFFFF")
BLACK = Color("#000000")

#width, height = screen.get_size()
screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()

run = True

num = 51

#grid initialization
grid = [[1 for i in range(num)] for j in range(num)]
grid = gridCreation(grid, num)

#initializing surfaces
grass = Surface((5000, 1000))

#1 is start page, 2 is game
curState = 1

clicked = False
curmouse = "none"

while run:
    x, y = mouse.get_pos()
    k, l = hoverDiamond(grid, x, y)
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            clicked = True
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
    if curState == 1:
        drawStart(screen)
        draw.rect(screen, BLACK, (0, 0, 100, 100))
        if clicked:
            if inbox(x, y, 0, 0, 100, 100):
                grassCreation(grid, grass, num)
                curState = 2
    if curState == 2:
        drawGame(screen, grass, width, height)
    if k != -1:
        #draw.rect(screen, WHITE, Rect(l * 98 - (k % 2) * 49 - 2000 + 49, k * 28 + 14, 10, 10))
        top = (l * 98 - (k % 2) * 49 - 2000 + 49, k * 28)
        left = (l * 98 - (k % 2) * 49 - 2000, k * 28 + 28)
        bot = (l * 98 - (k % 2) * 49 - 2000 + 49, k * 28 + 56)
        right = (l * 98 - (k % 2) * 49 - 2000 + 98, k * 28 + 28)
        draw.polygon(screen, WHITE, (top, left, bot, right))
    display.flip()
    clock.tick(60)
    #delta_time = clock.tick(60)/1000.0
quit()