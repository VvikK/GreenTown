from pygame import *

def drawGame(screen, grid):
    img = transform.scale(image.load("images/borderless_grass.png"), (640, 480))
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 1:
                continue
            screen.blit(img, (j * 98 - (i % 2) * 49, i * 28))

