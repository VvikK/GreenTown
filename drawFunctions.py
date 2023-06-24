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

def barCreations(buildingbar, statsbar, money, co2, happiness):
    #buildingbar
    houseimg = transform.scale(image.load("images/house.png"), (640, 480))
    buildingbar.fill(WHITE)
    
    buildingbar.blit(houseimg, (0, 0))

    #statsbar
    m_img = money.image
    c_img = co2.image
    h_img = happiness.image

    #transform images
    moneyimg = transform.scale(image.load(m_img), (75, 75))
    co2img = transform.scale(image.load(c_img), (75, 75))
    happinessimg = transform.scale(image.load(h_img), (60, 60))

    statsbar.fill(WHITE)
    statsbar.blit(moneyimg, (10, 10))
    statsbar.blit(happinessimg, (510, 10))
    statsbar.blit(co2img, (1010, 10))

def drawGame(screen, grid, grass, buildingbar, statsbar, items, houseimg, width, height):
    screen.blit(grass, (-500, 0))
    screen.blit(buildingbar, ((width / 5 * 4, 0)))
    screen.blit(statsbar, (0, 0))
    
    #for i in range(31):
        #for j in range(31):
            #if items[i][j] == 0:
                #continue
            #if items[i][j] == 1:
            #if grid[i][j] == 0:
                #screen.blit(houseimg, (j * 98 - (i % 2) * 49 - 1000, i * 28 - 20))
