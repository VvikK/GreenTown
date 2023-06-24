from pygame import *
from drawFunctions import *
from logicFunctions import *
from buildings import *

init()

WHITE = Color("#FFFFFF")
BLACK = Color("#000000")

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()

run = True

num = 31

#grid initialization
grid = [[1 for i in range(num)] for j in range(num)]
grid = gridCreation(grid, num)
itemplotgrid = [[0 for i in range(num)] for j in range(num)]

#initializing surfaces
grass = Surface((5000, 1000))
buildingbar = Surface((width / 5, height))

#initializing images
houseimg = transform.scale(image.load("images/house.png"), (640, 480))
house2img = houseimg.copy().convert_alpha()

#1 is start page, 2 is game
curState = 1

clicked = False
curmouse = "none"

while run:
    x, y = mouse.get_pos()
    k, l = hoverDiamond(grid, x, y)
    clicked = False
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
                barCreations(buildingbar)
                curState = 2
    if curState == 2:
        drawGame(screen, grid, grass, buildingbar, itemplotgrid, house2img, width, height)
        if k != -1:
            top = (l * 98 - (k % 2) * 49 - 1000 + 49, k * 28)
            left = (l * 98 - (k % 2) * 49 - 1000, k * 28 + 28)
            bot = (l * 98 - (k % 2) * 49 - 1000 + 49, k * 28 + 56)
            right = (l * 98 - (k % 2) * 49 - 1000 + 98, k * 28 + 28)
            draw.polygon(screen, WHITE, (top, left, bot, right))
        if clicked:
            if inbox(x, y, width // 5 * 4, 0, width, height) and curmouse == "none":
                curmouse = "house"
            elif inbox(x, y, width // 5 * 4, 0, width, height) and curmouse == "house":
                curmouse = "none"
        if curmouse == "house":
            screen.blit(houseimg, (x - 35, y - 60))
            if clicked:
                itemplotgrid[k][l] = 1
        
    display.flip()
    clock.tick(60)
    #delta_time = clock.tick(60)/1000.0
quit()