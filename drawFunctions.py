from pygame import *

WHITE = Color("#FFFFFF")

def drawStart(screen):
    screen.fill(WHITE)

def grassCreation(grid, grass, num):
    img = transform.scale(image.load("images/borderless_grass.png"), (640, 480))
    for i in range(num):
        for j in range(num):
            if grid[i][j] == 1:
                continue
            grass.blit(img, (j * 98 - (i % 2) * 49, i * 28))
    return grass

def barCreations(buildingbar):
    houseimg = transform.scale(image.load("images/house.png"), (640, 480))
    buildingbar.fill(WHITE)
    buildingbar.blit(houseimg, (0, 0))

def drawGame(screen, grass, buildingbar, width, height):
    screen.blit(grass, (-2000, 0))
    screen.blit(buildingbar, ((width / 5 * 4, 0)))
