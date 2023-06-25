from pygame import *
from drawFunctions import *
from logicFunctions import *
from buildings import *
from currency import *

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
itemgrid = [[0 for i in range(num)] for j in range(num)]

#initializing surfaces
grass = Surface((5000, 1000))
itemSurface = Surface((5000, 1000)).convert_alpha()
itemSurface.fill((0, 0, 0, 0))
buildingbar = Surface((width / 5, height))
statsbar = Surface((width-width/5-10, height/15))

#initializing images

#initializing buildings
#value, name, img, cap
house = Building(100, "house", transform.scale(image.load("images/house.png"), (640, 480)).convert_alpha(), 0, 0, 0, 0, 0, 1, 1)
nuclear = Building(100, "nuclear", transform.scale(image.load("images/nuclear.png"), (640, 480)).convert_alpha(), 0, -50, -200, 25, -175, 2, 2)
windturbine = Building(100, "windturbine", transform.scale(image.load("images/windturbine.png"), (640, 480)).convert_alpha(), 0, -25, -75, 15, -30, 1, 1)
solarpanel = Building(100, "solarpanel", transform.scale(image.load("images/solarpanel.png"), (640, 480)).convert_alpha(), 0, -25, -25, 25, 15, 1, 1)
coalplant = Building(100, "coalplant", transform.scale(image.load("images/coalplant.png"), (640, 480)).convert_alpha(), 0, -10, -75, 25, -40, 2, 1)

energies = [nuclear, windturbine, solarpanel, coalplant]

#statbar intiialization
statbar = ["images/statbar.png", "images/redbar.png", "images/yellowbar.png", "images/greenbar.png", "images/brownbar.png"]

#initializing currency
money = Currency(0, "money", "images/money.png", 500, statbar, 10, 10)
happiness = Currency(500, "happiness", "images/happiness.png", 500, statbar, 510, 10)
co2 = Currency(500, "CO2", "images/CO2.png", 500, statbar, 1010, 10)

#1 is start page, 2 is game
curState = 1

clicked = False
curmouse = "none"

xshift, yshift = (0, 0)

while run:
    x, y = mouse.get_pos()
    k, l = hoverDiamond(grid, x, y, xshift, yshift)
    if x > width / 5 * 4:
        k = -1
    clicked = False
    #getting events
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            clicked = True
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
    #adjusting x and y shift based on scrolling
    curkeys = key.get_pressed()
    if curkeys[K_LEFT]:
        xshift += 10
    if curkeys[K_RIGHT]:
        xshift -= 10
    if curkeys[K_UP]:
        yshift += 10
    if curkeys[K_DOWN]:
        yshift -= 10
    if curState == 1:
        drawStart(screen)
        draw.rect(screen, BLACK, (0, 0, 100, 100))
        if clicked:
            if inbox(x, y, 0, 0, 100, 100):
                grass = grassCreation(grid, grass, num)
                barCreations(buildingbar, statsbar, money, co2, happiness, energies, width, height)
                curState = 2
    if curState == 2:
        drawGame(screen, grid, grass, buildingbar, statsbar, itemgrid, house.image_frames, width, height, xshift, yshift, itemSurface)
        if clicked:
            for i in range(4):
                if inbox(x, y, width // 5 * 4, i * 110 + 110, width, i * 110 + 220):
                    curmouse = energies[i].name
                    break
            if inbox(x, y, width // 5 * 4, 0, width, height) and curmouse == "house":
                curmouse = "none"
        for i in range(4):
            if curmouse == energies[i].name:
                screen.blit(energies[i].image_frames, (x + energies[i].mousex, y + energies[i].mousey))
                alist = diamondspan(k, l, energies[i].w, energies[i].h)
                shadow = Surface((5000, 1000)).convert_alpha()
                shadow.fill((0, 0, 0, 0))
                canplace = True
                for i1 in range(len(alist)):
                    k1, l1 = alist[i1]
                    top = (l1 * 98 - (k1 % 2) * 49 + 49 + xshift, k1 * 28 + yshift)
                    left = (l1 * 98 - (k1 % 2) * 49 + xshift, k1 * 28 + 28 + yshift)
                    bot = (l1 * 98 - (k1 % 2) * 49 + 49 + xshift, k1 * 28 + 56 + yshift)
                    right = (l1 * 98 - (k1 % 2) * 49 + 98 + xshift, k1 * 28 + 28 + yshift)
                    draw.polygon(shadow, (255,160,122, 50), (top, left, bot, right))
                    if itemgrid[k1][l1] != 0:
                        canplace = False
                screen.blit(shadow, (0, 0))
                if clicked and k != -1 and canplace:
                    for i1 in range(len(alist)):
                        tmpk, tmpl = alist[i1]
                        itemgrid[tmpk][tmpl] = -1
                    itemgrid[k][l] = i + 1
                    itemSurface = itemCreation(itemSurface, itemgrid, house.image_frames, energies)
    display.flip()
    clock.tick(60)
quit()