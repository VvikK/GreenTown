from pygame import *

def drawGame(screen, grid):
    img = transform.scale(image.load("images/borderless_grass.png"), (640, 480))
    for i in range(51):
        for j in range(51):
            if grid[i][j] == 1:
                continue
            screen.blit(img, (j * 104 - (i % 2) * 52 - 2000, i * 32))

