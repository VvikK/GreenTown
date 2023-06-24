from pygame import *

WHITE = Color("#FFFFFF")
BLACK = Color("#000000")

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

def itemCreation(itemSurface, grid, house, energies):
    for i in range(31):
        for j in range(31):
            if grid[i][j] == 0:
                continue
            for k in range(4):
                if grid[i][j] == k + 1:
                    itemSurface.blit(energies[k].image_frames, (j * 98 - (i % 2) * 49 + energies[k].placex, i * 28 - 20 + energies[k].placey))
    return itemSurface

def barCreations(buildingbar, statsbar, money, co2, happiness, energies, width, height):
    #buildingbar
    buildingbar.fill(WHITE)
    
    iconback = transform.scale(image.load("images/iconback.png"), (560, 420))
    energy = [0] * 4
    energy[0] = transform.scale(image.load("images/nuclear.png"), (220, 165)).convert_alpha()
    energy[1] = transform.scale(image.load("images/windturbine.png"), (640, 480)).convert_alpha()
    energy[2] = transform.scale(image.load("images/solarpanel.png"), (800, 600)).convert_alpha()
    energy[3] = transform.scale(image.load("images/coalplant.png"), (640, 480)).convert_alpha()

    for i in range(4):
        buildingbar.blit(iconback, (0, i * 110 + 110))   
        buildingbar.blit(energy[i], (0, i * 110 + 110))  

    #statsbar
    m_img = money.image
    c_img = co2.image
    h_img = happiness.image

    #transform images
    moneyimg = transform.scale(image.load(m_img), (75, 75))
    co2img = transform.scale(image.load(c_img), (75, 75))
    happinessimg = transform.scale(image.load(h_img), (60, 60))

    statsbar.fill(WHITE)

    statsbar.blit(moneyimg, (money.xpos, money.ypos))

    hp_status = happiness.set_bar_status()
    statsbar.blit(transform.scale(image.load(hp_status[0]), (hp_status[1], 200)), (happiness.xpos+20, happiness.ypos+5))
    statsbar.blit(transform.scale(image.load(happiness.stbar[0]), (400, 200)), (happiness.xpos+20, happiness.ypos+5))
    statsbar.blit(happinessimg, (happiness.xpos, happiness.ypos))
    
    co2_status = co2.set_bar_status()
    statsbar.blit(transform.scale(image.load(co2_status[0]), (co2_status[1], 200)), (co2.xpos+20, co2.ypos+7))
    statsbar.blit(transform.scale(image.load(co2.stbar[0]), (400, 200)), (co2.xpos+20, co2.ypos+7))
    statsbar.blit(co2img, (co2.xpos, co2.ypos))
    

def drawGame(screen, grid, grass, buildingbar, statsbar, items, houseimg, width, height, xshift, yshift, itemSurface):
    screen.fill(BLACK)
    screen.blit(grass, (xshift, yshift))
    screen.blit(buildingbar, ((width / 5 * 4, 0)))
    screen.blit(statsbar, (0, 0))
    screen.blit(itemSurface, (xshift, yshift))
