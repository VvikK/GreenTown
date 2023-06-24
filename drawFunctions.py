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

def drawGame(screen, grass, width, height):
    screen.blit(grass, (-2000, 0))
    draw.rect(screen, WHITE, (width / 5 * 4, 0, width / 5, height))
