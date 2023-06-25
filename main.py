from pygame import *
from drawFunctions import *
from logicFunctions import *
from buildings import *
from currency import *

init()

WHITE = Color("#FFFFFF")
BLACK = Color("#000000")

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()

run = True

num = 31

#grid initialization
grid = [[1 for i in range(num)] for j in range(num)]
grid = gridCreation(grid, num)
itemgrid = [[0 for i in range(num)] for j in range(num)]
upgradegrid = [[0 for i in range(num)] for j in range(num)]
busgrid = [[0 for i in range(num)] for j in range(num)] 

itemgrid[18][9] = 5
itemgrid[4][15] = 5
itemgrid[6][16] = 5
itemgrid[12][19] = 5
itemgrid[14][20] = 5
itemgrid[14][12] = 5
itemgrid[18][14] = 5
itemgrid[20][15] = 5
itemgrid[15][17] = 4
itemgrid[14][17] = -1
itemgrid[18][18] = 4
itemgrid[17][19] = -1
itemgrid[9][13] = 4
itemgrid[8][13] = -1
itemgrid[22][12] = 4
itemgrid[21][13] = -1

#initializing surfaces
grass = Surface((5000, 1000))
itemSurface = Surface((5000, 1000)).convert_alpha()
itemSurface.fill((0, 0, 0, 0))
upgradeSurface = Surface((5000, 1000)).convert_alpha()
upgradeSurface.fill((0, 0, 0, 0))
busSurface = Surface((5000, 1000)).convert_alpha()
busSurface.fill((0, 0, 0, 0)) 
roadSurface = Surface((5000, 1000)).convert_alpha()
roadSurface.fill((0, 0, 0, 0)) 
buildingbar = Surface((width / 5, height)).convert_alpha()
upgradebar = Surface((width / 5, height))
statsbar = Surface((width-width/5-10, height/15))

#initializing images

#initializing buildings
#value, name, img, cap
house = Building(5, 10, 100, 10, "house", transform.scale(image.load("images/house.png"), (640, 480)).convert_alpha(), 0, -25, -50, 0, 0, 1, 1)
nuclear = Building(100, -50, 0, 50, "nuclear", transform.scale(image.load("images/nuclear.png"), (640, 480)).convert_alpha(), 0, -50, -200, 25, -175, 2, 2)
windturbine = Building(40, -20, 10, 20, "windturbine", transform.scale(image.load("images/windturbine.png"), (640, 480)).convert_alpha(), 0, -25, -75, 15, -30, 1, 1)
solarpanel = Building(1, -10, 10, 0, "solarpanel", transform.scale(image.load("images/solarpanel.png"), (640, 480)).convert_alpha(), 0, -25, -25, 25, 15, 1, 1)
coalplant = Building(10, 50, -20, 50, "coalplant", transform.scale(image.load("images/coalplant.png"), (640, 480)).convert_alpha(), 0, -10, -75, 25, -40, 2, 1)
tree = Building(0, -5, 5, 0, "tree", transform.scale(image.load("images/tree.png"), (640, 480)).convert_alpha(), 0, -35, -75, 15, -20, 1, 1)
shop = Building(5, 0, 50, 10, "shop", transform.scale(image.load("images/shop.png"), (640, 480)).convert_alpha(), 0, -25, -90, 0, -50, 1, 2)

greenroof = Building(5, -5, 10, 0, "greenroof", transform.scale(image.load("images/greenroof.png"), (640, 480)).convert_alpha(), 0, -25, -10, 0, 0, 1, 1)
solarroof = Building(5, -10, 5, 0, "solarroof", transform.scale(image.load("images/solarpanelroof.png"), (640, 480)).convert_alpha(), 0, -25, -10, 0, 0, 1, 1)
insulation = Building(10, -10, 15, 0, "insulation", transform.scale(image.load("images/insulation.png"), (640, 480)).convert_alpha(), 0, -25, -50, 0, 0, 1, 1)

energies = [nuclear, windturbine, solarpanel, coalplant, house, shop, tree]
upgrades = [greenroof, solarroof, insulation]

#statbar intiialization
statbar = ["images/statbar.png", "images/redbar.png", "images/yellowbar.png", "images/greenbar.png", "images/brownbar.png"]

#initializing currency
money = Currency(500, "money", "images/money.png", 0, statbar, 10, 10)
happiness = Currency(100, "happiness", "images/happiness.png", 500, statbar, 510, 10)
co2 = Currency(350, "CO2", "images/CO2.png", 500, statbar, 1010, 10)

#1 is start page, 2 is game
curState = 1

clicked = False
curmouse = "none"
curbar = "building"
years = 0
max_years = 5

xshift, yshift = (0, 0)

while run:
    x, y = mouse.get_pos()
    k, l = hoverDiamond(grid, x, y, xshift, yshift)
    if clicked:
        print(k, l)
    if x > width / 5 * 4:
        k = -1
    clicked = False
    #getting events
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            clicked = True
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
    #adjusting x and y shift based on scrolling
    curkeys = key.get_pressed()
    if curkeys[K_LEFT]:
        xshift += 10
    if curkeys[K_RIGHT]:
        xshift -= 10
    if curkeys[K_UP]:
        yshift += 10
    if curkeys[K_DOWN]:
        yshift -= 10
    if curState == 1:
        #start pages
        background = transform.scale(image.load("images/startbackground.png"), (width, width / 4 * 3))
        start = transform.scale(image.load("images/startbutton.png"), (1600, 1200))
        instructions = transform.scale(image.load("images/instructionsbutton.png"), (1600, 1200))
        highscore = transform.scale(image.load("images/highscorebutton.png"), (1600, 1200))
        if inbox(x, y, width//2 - 150, height // 3 + 100, width//2 - 150 + 300, height // 3 + 100 + 120):
            start = transform.scale(image.load("images/startclick.png"), (1600, 1200))
            if clicked:
                #when the start button is clicked
                screen.fill(WHITE)
                loading = transform.scale(image.load("images/loading.png"), (1600, 1200))
                screen.blit(loading, (width // 2 - 500, height // 2 - 150))
                display.flip()
                grass = grassCreation(grid, grass, num)
                barCreations(screen, buildingbar, upgradebar, statsbar, money, co2, happiness, energies, upgrades, width, height)
                itemSurface, itemgrid = itemCreation(itemSurface, itemgrid, house, energies)
                roadCreation(roadSurface, itemgrid)
                busGeneration(busSurface, busgrid)
                curState = 2
        if inbox(x, y, width//2 - 350, height // 2 + 100, width//2 - 350 + 650, height // 2 + 100 + 120):
            instructions = transform.scale(image.load("images/instructionsclick.png"), (1600, 1200))
        if inbox(x, y, width//2 - 350, height // 3 * 2 + 100, width//2 - 350 + 650, height // 3 * 2 + 100 + 120):
            highscore = transform.scale(image.load("images/highscoreclick.png"), (1600, 1200))
        if clicked:
            print(x, y)
        drawStart(screen, start, instructions, highscore, background, width, height)
    if curState == 2:
        drawGame(screen, grid, grass, buildingbar, upgradebar, curbar, statsbar, itemgrid, house.image_frames, width, height, xshift, yshift, itemSurface, upgradeSurface, busSurface, roadSurface)
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
        f = font.SysFont(None, 32)
        moneytxt = f.render(str(money.value), True, BLACK)
        statsbar.blit(moneytxt, (75, 20))
        yeartxt = f.render(str("Year " + str(years)), True, BLACK)
        draw.rect(buildingbar, WHITE, (0, 0, 160, 100))
        draw.rect(upgradebar, WHITE, (0, 0, 160, 100))
        buildingbar.blit(yeartxt, (75, 20))
        upgradebar.blit(yeartxt, (75, 20))
        #years
        if clicked and inbox(x, y, 1720, 20, 1753, 50):
            years += 1
            money.value += money.cap
            busGeneration(busSurface, busgrid)
            if years > 20:
                curState = 3
        if clicked:
            #checking to see which things are clicked
            for i in range(7):
                if inbox(x, y, width // 5 * 4, i * 110 + 110, width, i * 110 + 220) and curbar == "building":
                    if curmouse == energies[i].name:
                        curmouse = "none"
                    else:
                        curmouse = energies[i].name
                    break
            if inbox(x, y, width // 5 * 4, 7 * 110 + 110, width, 7 * 110 + 220) and curbar == "building":
                if curmouse == "remove":
                    curmouse = "none"
                else:
                    curmouse = "remove"
            for i in range(3):
                if inbox(x, y, width // 5 * 4, i * 110 + 110, width, i * 110 + 220) and curbar == "upgrade":
                    if curmouse == upgrades[i].name:
                        curmouse = "none"
                    else:
                        curmouse = upgrades[i].name
                    break
            #checking to see if swap the input thing
            if inbox(x, y, width // 5 * 4 - 50, 100, width // 5 * 4, 200):
                curbar = "building"
                curmouse = "none"
            elif inbox(x, y, width // 5 * 4 - 50, 250, width // 5 * 4, 350):
                curbar = "upgrade"
                curmouse = "none"
        #buying buildings
        for i in range(7):
            if curmouse == energies[i].name:
                screen.blit(energies[i].image_frames, (x + energies[i].mousex, y + energies[i].mousey))
                if k == -1:
                    break
                alist = diamondspan(k, l, energies[i].w, energies[i].h)
                shadow = Surface((5000, 1000)).convert_alpha()
                shadow.fill((0, 0, 0, 0))
                canplace = True
                for i1 in range(len(alist)):
                    k1, l1 = alist[i1]
                    if itemgrid[k1][l1] != 0 or grid[k1][l1] == 1:
                        canplace = False
                if money.value < energies[i].value:
                    canplace = False
                for i1 in range(len(alist)):
                    k1, l1 = alist[i1]
                    top = (l1 * 98 - (k1 % 2) * 49 + 49 + xshift, k1 * 28 + yshift)
                    left = (l1 * 98 - (k1 % 2) * 49 + xshift, k1 * 28 + 28 + yshift)
                    bot = (l1 * 98 - (k1 % 2) * 49 + 49 + xshift, k1 * 28 + 56 + yshift)
                    right = (l1 * 98 - (k1 % 2) * 49 + 98 + xshift, k1 * 28 + 28 + yshift)
                    if canplace:
                        draw.polygon(shadow, (255, 255, 255, 100), (top, left, bot, right))
                    else:
                        draw.polygon(shadow, (255, 160, 122, 100), (top, left, bot, right))
                screen.blit(shadow, (0, 0))
                #checking to see if you can place
                if clicked and k != -1 and canplace:
                    for i1 in range(len(alist)):
                        tmpk, tmpl = alist[i1]
                        itemgrid[tmpk][tmpl] = -1
                    itemgrid[k][l] = i + 1
                    itemSurface, itemgrid = itemCreation(itemSurface, itemgrid, house.image_frames, energies)
                    #changing variables
                    money.value -= energies[i].value
                    if (co2.value + energies[i].co2_contribution >=0):
                        co2.value += energies[i].co2_contribution
                    elif (co2.value + energies[i].co2_contribution <= 0 & co2.value >=0):
                        co2.value = 0
                    if (co2.value + energies[i].co2_contribution >= co2.cap):
                        co2.value = co2.cap 

                    if (happiness.value + energies[i].happiness_contribution >=0):
                        happiness.value += energies[i].happiness_contribution
                    elif (happiness.value + energies[i].happiness_contribution <= 0 & co2.value >=0):
                        happiness.value = 0
                    if (happiness.value + energies[i].happiness_contribution >= happiness.cap):
                        happiness.value = happiness.cap 
                    money.cap += energies[i].money_contribution
        #buying upgrades
        for i in range(3):
            if curmouse == upgrades[i].name:
                screen.blit(upgrades[i].image_frames, (x + upgrades[i].mousex, y + upgrades[i].mousey))
                if k == -1:
                    break
                alist = diamondspan(k, l, upgrades[i].w, upgrades[i].h)
                shadow = Surface((5000, 1000)).convert_alpha()
                shadow.fill((0, 0, 0, 0))
                canplace = True
                for i1 in range(len(alist)):
                    k1, l1 = alist[i1]
                    if itemgrid[k1][l1] != 5 or grid[k1][l1] == 1:
                        canplace = False
                if money.value < upgrades[i].value:
                    canplace = False
                for i1 in range(len(alist)):
                    k1, l1 = alist[i1]
                    top = (l1 * 98 - (k1 % 2) * 49 + 49 + xshift, k1 * 28 + yshift)
                    left = (l1 * 98 - (k1 % 2) * 49 + xshift, k1 * 28 + 28 + yshift)
                    bot = (l1 * 98 - (k1 % 2) * 49 + 49 + xshift, k1 * 28 + 56 + yshift)
                    right = (l1 * 98 - (k1 % 2) * 49 + 98 + xshift, k1 * 28 + 28 + yshift)
                    if canplace:
                        draw.polygon(shadow, (255, 255, 255, 100), (top, left, bot, right))
                    else:
                        draw.polygon(shadow, (255, 160, 122, 100), (top, left, bot, right))
                screen.blit(shadow, (0, 0))
                #checking to see if you can place
                if clicked and k != -1 and itemgrid[k][l] == 5 and canplace:
                    for i1 in range(len(alist)):
                        tmpk, tmpl = alist[i1]
                        upgradegrid[tmpk][tmpl] = -1
                    upgradegrid[k][l] = i + 1
                    upgradeCreation(upgradeSurface, upgradegrid, upgrades)
                    money.value -= upgrades[i].value
                    if (co2.value + upgrades[i].co2_contribution >=0):
                        co2.value += upgrades[i].co2_contribution
                    elif (co2.value + upgrades[i].co2_contribution <= 0 & co2.value >=0):
                        co2.value = 0
                    if (co2.value + upgrades[i].co2_contribution >= co2.cap):
                        co2.value = co2.cap
                    if (happiness.value + upgrades[i].happiness_contribution >=0):
                        happiness.value += upgrades[i].happiness_contribution
                    elif (happiness.value + upgrades[i].happiness_contribution <= 0 & co2.value >=0):
                        happiness.value = 0
                    if (happiness.value + upgrades[i].happiness_contribution >= happiness.cap):
                        happiness.value = upgrades[i].cap 
                    money.cap += upgrades[i].money_contribution
        if curmouse == "remove":
            removemouse = transform.scale(image.load("images/removemouse.png"), (400, 300))
            screen.blit(removemouse, (x - 30, y - 30))
            if k != -1:
                shadow = Surface((5000, 1000)).convert_alpha()
                shadow.fill((0, 0, 0, 0))
                if itemgrid[k][l] > 0:
                    alist = diamondspan(k, l, energies[itemgrid[k][l] - 1].w, energies[itemgrid[k][l] - 1].h)
                    for i1 in range(len(alist)):
                        k1, l1 = alist[i1]
                        top = (l1 * 98 - (k1 % 2) * 49 + 49 + xshift, k1 * 28 + yshift)
                        left = (l1 * 98 - (k1 % 2) * 49 + xshift, k1 * 28 + 28 + yshift)
                        bot = (l1 * 98 - (k1 % 2) * 49 + 49 + xshift, k1 * 28 + 56 + yshift)
                        right = (l1 * 98 - (k1 % 2) * 49 + 98 + xshift, k1 * 28 + 28 + yshift)
                        draw.polygon(shadow, (255, 160, 122, 100), (top, left, bot, right))
                else:
                    top = (l * 98 - (k % 2) * 49 + 49 + xshift, k * 28 + yshift)
                    left = (l * 98 - (k % 2) * 49 + xshift, k * 28 + 28 + yshift)
                    bot = (l * 98 - (k % 2) * 49 + 49 + xshift, k * 28 + 56 + yshift)
                    right = (l * 98 - (k % 2) * 49 + 98 + xshift, k * 28 + 28 + yshift)
                    draw.polygon(shadow, (255, 255, 255, 100), (top, left, bot, right))
                screen.blit(shadow, (0, 0))
                if clicked and k != -1 and itemgrid[k][l] > 0:
                    for i1 in range(len(alist)):
                        k1, l1 = alist[i1]
                        itemgrid[k1][l1] = 0
                        upgradegrid[k1][l1] = 0
                    itemSurface, itemgrid = itemCreation(itemSurface, itemgrid, house.image_frames, energies)
                    upgradeCreation(upgradeSurface, upgradegrid, upgrades)
    if curState == 3:
        screen.fill(WHITE)
        completescreen = transform.scale(image.load("images/gamecomplete.png"), (1200, 900))
        screen.blit(completescreen, (width // 2 - 500, height // 4 - 150))
        f = font.SysFont(None, 100)
        moneyscore = f.render(str(money.value), True, BLACK)
        happinessscore = f.render(str(happiness.value), True, BLACK)
        co2score = f.render(str(co2.value), True, BLACK)
        moneyimg = transform.scale(image.load("images/moneyscore.png"), (1200, 900))
        happyimg = transform.scale(image.load("images/happinessscore.png"), (1200, 900))
        coimg = transform.scale(image.load("images/co2score.png"), (1200, 900))
        screen.blit(moneyimg, (width//4 - 300, height//3))
        screen.blit(happyimg, (width//4 - 300, height//2))
        screen.blit(coimg, (width//4 - 300, height//3*2))
        screen.blit(moneyscore, (width//4*3, height//3 + 50))
        screen.blit(happinessscore, (width//4*3, height//2 + 50))
        screen.blit(co2score, (width//4*3, height//3*2 + 50))
        
    #if (clicked):
        #print(x, y)
    display.flip()
    clock.tick(60)
quit()