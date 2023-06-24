from pygame import *

def gridCreation(grid):
    grid[0][25] = 0
    for i in range(1, 51):
        for j in range(51):
            grid[i][j] = grid[i - 1][j]
        if i <= 25:
            if i % 2 == 0:
                grid[i][25 - (i + 1) // 2] = 0
            else:
                grid[i][25 + (i + 1) // 2] = 0
        else:
            if i % 2 == 0:
                grid[i][51 - (i - 1) // 2 - 1] = 1
            else:
                grid[i][(i + 1 - 25) // 2 + 1] = 1
    return grid

def hoverDiamond(grid, x, y):
    for i in range(51):
        for j in range(51):
            if grid[i][j] == 1:
                continue
            top = i * 28
            left = j * 98 - (i % 2) * 49 - 2000
            right = (j + 1) * 98 - (i % 2) * 49 - 2000
            bot = (i + 2) * 28
            midheight = (top + bot) // 2
            midwidth = (left + right) // 2
            if x < left or x > right:
                continue
            if y < top or y > bot:
                continue
            if y < midheight:
                if x >= left + (midheight - y) * 28 / 98 and x <= right - (midheight - y) * 28 / 98:
                    return i, j
            else:
                if x >= left + (y - midheight) * 98 / 28 and x <= right - (y - midheight) * 98 / 28:
                    return i, j
    return -1, -1



