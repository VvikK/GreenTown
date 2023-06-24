from pygame import *

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
                if x >= left + (midheight - y) * 4 // 13 and x <= right - (midheight - y) * 4 // 13:
                    return i, j
            else:
                if x >= left + (y - midheight) * 4 // 13 and x <= right - (y - midheight) * 4 // 13:
                    return i, j
    return -1, -1



