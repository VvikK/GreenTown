from pygame import *

def gridCreation(grid, num):
    grid[0][num//2] = 0
    for i in range(1, num):
        for j in range(num):
            grid[i][j] = grid[i - 1][j]
        if i <= num//2:
            if i % 2 == 0:
                grid[i][num//2 - (i + 1) // 2] = 0
            else:
                grid[i][num//2 + (i + 1) // 2] = 0
        else:
            if i % 2 == 0:
                grid[i][num - (i - 1) // 2 - 1] = 1
            else:
                grid[i][(i + 1 - (num//2)) // 2 + (num+1)%2 + num//4] = 1
                
    return grid

def hoverDiamond(grid, x, y, xshift, yshift):
    for i in range(31):
        for j in range(31):
            if grid[i][j] == 1:
                continue
            top = i * 28 + yshift
            left = j * 98 - (i % 2) * 49 + xshift
            right = (j + 1) * 98 - (i % 2) * 49 + xshift
            bot = (i + 2) * 28 + yshift
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

def inbox(x, y, x1, y1, x2, y2):
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        return True
    return False
