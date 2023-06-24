from pygame import *

def grassCreation(grid, grass):
    img = transform.scale(image.load("images/borderless_grass.png"), (640, 480))
    for i in range(51):
        for j in range(51):
            if grid[i][j] == 1:
                continue
            grass.blit(img, (j * 98 - (i % 2) * 49, i * 28))
    return grass

def drawGame(screen, grass):
    screen.blit(grass, (-2000, 0))
