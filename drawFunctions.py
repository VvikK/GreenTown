from pygame import *
import random

WHITE = Color("#FFFFFF")
BLACK = Color("#000000")
RED = Color("#880808")

def drawStart(screen, start, instructions, highscore, background, width, height):
    screen.blit(background, (0, 0))
    title = transform.scale(image.load("images/starttitle.png"), (1600, 1200))
    screen.blit(title, (width // 2 - 800, -100))
    screen.blit(start, (width//2 - 150, height // 3 + 100))
    screen.blit(instructions, (width//2 - 350, height // 2 + 100))
    screen.blit(highscore, (width//2 - 350, height // 3 * 2 + 100))

def grassCreation(grid, grass, num):
    img = transform.scale(image.load("images/borderless_grass.png"), (640, 480))
    for i in range(num):
        for j in range(num):
            if grid[i][j] == 1:
                continue
            grass.blit(img, (j * 98 - (i % 2) * 49, i * 28))
    return grass

def itemCreation(itemSurface, grid, house, energies):
    itemSurface.fill((0, 0, 0, 0))
    for i in range(31):
        for j in range(31):
            if grid[i][j] == 0:
                continue
            for k in range(7):
                if grid[i][j] == k + 1:
                    itemSurface.blit(energies[k].image_frames, (j * 98 - (i % 2) * 49 + energies[k].placex, i * 28 - 20 + energies[k].placey))
    return itemSurface, grid

def roadCreation(roadSurface, grid):
    roadSurface.fill((0, 0, 0, 0))
    for i in range(11, 27):
        grid[i][(i - 11) // 2 + 10] = -2
    for i in range(3, 19):
        grid[i][(i - 3) // 2 + 14] = -2
    for i in range(6, 22):
        grid[i][(16 - (i - 10)//2)] = -3
    grid[9][17] = -4
    grid[17][13] = -4
    for i in range(31):
        for j in range(31):
            if grid[i][j] == -2:
                roadSurface.blit(transform.scale(image.load("images/road2.png"), (1000, 750)), (j * 98 - (i % 2) * 49 - 28, i * 28 - 20 - 20))
            if grid[i][j] == -3:
                roadSurface.blit(transform.scale(image.load("images/road1.png"), (1000, 750)), (j * 98 - (i % 2) * 49 - 28, i * 28 - 20 - 20))
            if grid[i][j] == -4:
                roadSurface.blit(transform.scale(image.load("images/roadcross.png"), (1000, 750)), (j * 98 - (i % 2) * 49 - 28, i * 28 - 20 - 20))

def busGeneration(busSurface, grid):
    busSurface.fill((0, 0, 0, 0))
    grid = [[0 for i in range(31)] for j in range(31)]
    car = transform.scale(image.load("images/car.png"), (640, 480))
    car2 = transform.scale(image.load("images/car2.png"), (640, 480))
    for i in range(11, 27):
        r = random.randint(1, 3)
        j = (i - 11) // 2 + 10
        if (i == 9 and j == 17) or (i == 17 and j == 13):
            continue
        if r == 1:
            busSurface.blit(car2, (j * 98 - (i % 2) * 49, i * 28 - 20))
    for i in range(3, 19):
        r = random.randint(1, 3)
        j = (i - 3) // 2 + 14
        if (i == 9 and j == 17) or (i == 17 and j == 13):
            continue
        if r == 1:
            busSurface.blit(car2, (j * 98 - (i % 2) * 49, i * 28 - 20))
    for i in range(6, 22):
        r = random.randint(1, 3)
        j = (16 - (i - 10)//2)
        if (i == 9 and j == 17) or (i == 17 and j == 13):
            continue
        if r == 1:
            busSurface.blit(car, (j * 98 - (i % 2) * 49, i * 28 - 20))

def upgradeCreation(upgradeSurface, grid, upgrades):
    upgradeSurface.fill((0, 0, 0, 0))
    for i in range(31):
        for j in range(31):
            if grid[i][j] == 0:
                continue
            for k in range(3):
                if grid[i][j] == k + 1:
                    upgradeSurface.blit(upgrades[k].image_frames, (j * 98 - (i % 2) * 49 + upgrades[k].placex, i * 28 - 20 + upgrades[k].placey))


def barCreations(screen, buildingbar, upgradebar, statsbar, money, co2, happiness, energies, width, height):
    #buildingbar
    buildingbar.fill(WHITE)
    
    iconback = transform.scale(image.load("images/iconback.png"), (560, 420))
    energy = [0] * 7
    energy[0] = transform.scale(image.load("images/nuclear.png"), (220, 165)).convert_alpha()
    energy[1] = transform.scale(image.load("images/windturbine.png"), (640, 480)).convert_alpha()
    energy[2] = transform.scale(image.load("images/solarpanel.png"), (800, 600)).convert_alpha()
    energy[3] = transform.scale(image.load("images/coalplant.png"), (640, 480)).convert_alpha()
    energy[4] = transform.scale(image.load("images/house.png"), (640, 480)).convert_alpha()
    energy[5] = transform.scale(image.load("images/shop.png"), (400, 300)).convert_alpha()
    energy[6] = transform.scale(image.load("images/tree.png"), (640, 480)).convert_alpha()
    f = font.SysFont(None, 32)
    for i in range(7):
        buildingbar.blit(iconback, (0, i * 110 + 110))   
        buildingbar.blit(energy[i], (0, i * 110 + 110))
        txtname = f.render(energies[i].name.upper(), True, BLACK)
        buildingbar.blit(txtname, (width / 5 // 3, i * 110 + 110 + 15))
        txtvalue = f.render(str(energies[i].value), True, BLACK)
        buildingbar.blit(txtvalue, (width // 5 - 60, i * 110 + 110 + 30))
    draw.rect(buildingbar, RED, (0, 7 * 110 + 110, 350, 100))

    #upgradebar
    upgradebar.fill(WHITE)
    upgrade = [0]*4
    upgrade[0] = transform.scale(image.load("images/greenroof.png"), (1200, 800)).convert_alpha()
    upgrade[1] = transform.scale(image.load("images/solarpanelroof.png"), (1200, 800)).convert_alpha()
    upgrade[2] = transform.scale(image.load("images/insulation.png"), (800, 600)).convert_alpha()
    upgrade[3] = transform.scale(image.load("images/electricbus.png"), (640, 480)).convert_alpha()

    for i in range(4):
        upgradebar.blit(iconback, (0, i * 110 + 110))   
        upgradebar.blit(upgrade[i], (0, i * 110 + 110))
    

def drawGame(screen, grid, grass, buildingbar, upgradebar, curbar, statsbar, items, houseimg, width, height, xshift, yshift, itemSurface, upgradeSurface, busSurface, roadSurface):
    screen.fill(BLACK)
    screen.blit(grass, (xshift, yshift))
    screen.blit(roadSurface, (xshift, yshift))
    screen.blit(busSurface, (xshift, yshift))
    screen.blit(itemSurface, (xshift, yshift))
    screen.blit(upgradeSurface, (xshift, yshift))
    if curbar == "building":
        screen.blit(buildingbar, ((width / 5 * 4, 0)))
    if curbar == "upgrade":
        screen.blit(upgradebar, ((width / 5 * 4, 0)))
    screen.blit(statsbar, (0, 0))
    buildingslabel = transform.scale(image.load("images/buildingslabel.png"), (220, 165)).convert_alpha()
    upgradeslabel = transform.scale(image.load("images/upgradeslabel.png"), (220, 165)).convert_alpha()
    screen.blit(buildingslabel, (width / 5 * 4 - 50, 100))
    screen.blit(upgradeslabel, (width / 5 * 4 - 50, 250))