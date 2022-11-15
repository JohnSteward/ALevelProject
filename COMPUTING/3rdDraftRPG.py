import pygame
from random import randint
pygame.init()

X = 1366
Y= 768
red = (255,0,0)
darkRed = (60,0,0)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)
brown = (65,43,21)
LBrown = (181,101,29)
pink = (255,110,199)
DBlue = (25,25,112)
LBlue = (65,105,225)
option = 0
window = pygame.display.set_mode((X, Y))
background = pygame.image.load('Images/MenuBackground.png').convert_alpha()


class MainMenu(object):
    def __init__(self, window, option):
        self.background = background
        self.arrow = option
        self.window = window
        self.draw(window)
        

    def draw(self, window):
        window.blit(background, (0,0))# draws the background and all text for the menu
        fontNewGame = pygame.font.Font('freesansbold.ttf', 24)#gets the font and size of the text
        fontTitle = pygame.font.Font('freesansbold.ttf', 50)
        fontContinueGame = pygame.font.Font('freesansbold.ttf', 24)
        newGameText = fontNewGame.render('New Game', True, red, black)
        continueGameText = fontContinueGame.render('Continue Game', True, red, black)
        titleText = fontTitle.render('*Insert Title Here*', True, red, black)
        textRect = newGameText.get_rect()
        textRect1 = continueGameText.get_rect()
        textRect2 = titleText.get_rect()
        textRect.center = (X//2, Y//2 - 50)
        textRect1.center = (X//2, Y//2)
        textRect2.center = (X//2, 200)
        window.blit(newGameText, textRect)
        window.blit(continueGameText, textRect1)
        window.blit(titleText, textRect2)
        pygame.display.update()
        
    def ChangeArrow(self, option):# changes the option on the main menu
        if option == 0:
            option = 1
            return option
        elif option == 1:
            option = 2
            return option
        elif option == 2:
            option = 1
            return option

    def MenuLoop(self, option):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                        chose = self.ChangeArrow(option)#Making a variable to represent
                        if chose == 1:                  #the option returned from the function
                            option = 1
                            optionNewGame = pygame.draw.polygon(window, red, ((X//2 - 70, Y//2 - 50), (X//2 - 90, Y//2 - 70), (X//2 - 90, Y//2 - 30)))
                            optionContinueGame = pygame.draw.polygon(window, black, ((X//2 - 100, Y//2), (X//2 - 120, Y//2 - 20), (X//2 - 120, Y//2 + 20)))
                            #draws the arrow over the option 
                        elif chose == 2:
                            option = 2
                            optionContinueGame = pygame.draw.polygon(window, red, ((X//2 - 100, Y//2), (X//2 - 120, Y//2 - 20), (X//2 - 120, Y//2 + 20)))
                            optionNewGame = pygame.draw.polygon(window, black, ((X//2 - 70, Y//2 - 50), (X//2 - 90, Y//2 - 70), (X//2 - 90, Y//2 - 30)))

                        pygame.display.update()
                    elif event.key == pygame.K_SPACE:
                        return option
                        

class Game(object):
    def __init__(self, a, battle):
        self.a = a
        self.battle = battle

    def NewOrContinue(self, a, window, MC, battle, walls, fighters, enemies, expReduction):#detects if the player chose new game or continue
        if self.a == 1:
            self.DrawNew(window, MC, battle, walls, fighters, enemies, expReduction)
        elif self.a == 2:
            self.DrawLoad()


    def DrawNew(self, window, MC, battle, walls, fighters, enemies, expReduction):
        pygame.draw.rect(window, LBrown, (0,0,X,Y))
        MC.draw(window)
        for wall in walls:
            wall.draw(window)
        Hodir.draw(window)
        pygame.display.update()
        self.Control(window, MC, battle, walls, fighters, enemies, expReduction)

    def DrawLoad(self):
        pass #Will get variable values from database from when the player last saved

    def Control(self, window, MC, battle, walls, fighters, enemies, expReduction):
        while self.battle == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ScrollUp(MC, walls)
                        if MC.y > (Y//2 - 20):
                            MC.y -= MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle, window, fighters, enemies, MC, walls, expReduction)
                    if event.key == pygame.K_DOWN:
                        self.ScrollDown(MC, walls)
                        if MC.y < (Y//2 + 20):
                            MC.y += MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle, window, fighters, enemies, MC, walls, expReduction)
                    if event.key == pygame.K_LEFT:
                        self.ScrollLeft(MC, walls)
                        if MC.x > (X//2 - 20):
                            MC.x -= MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle, window, fighters, enemies, MC, walls, expReduction)
                    if event.key == pygame.K_RIGHT:
                        self.ScrollRight(MC, walls)
                        if MC.x < (X//2 + 20):
                            MC.x += MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle, window, fighters, enemies, MC, walls, expReduction)
           
            self.ReDraw(window, MC, walls, battle)


    def ScrollUp(self, MC, walls):
        if MC.y <= (Y//2 - 20):
            for wall in walls:
                wall.y += MC.vel
            Hodir.y += MC.vel

    def ScrollDown(self, MC, walls):
        if MC.y >= (Y//2 + 20):
            for wall in walls:
                wall.y -= MC.vel
            Hodir.y -= MC.vel

    def ScrollLeft(self, MC, walls):
        if MC.x <= (X//2 - 20):
            for wall in walls:
                wall.x += MC.vel
            Hodir.x += MC.vel

    def ScrollRight(self, MC, walls):
        if MC.x >= (X//2 + 20):
            for wall in walls:
                wall.x -= MC.vel
            Hodir.x -= MC.vel

    def collision(self, MC, walls):
        for wall in walls:
            #if you approach a wall from above
            if ((MC.y + MC.height) > wall.y) and (MC.y < wall.y):
                if (MC.x >= wall.x) and ((MC.x + MC.width) < (wall.x + wall.width)):
                    MC.y -= ((MC.y + MC.height) - wall.y)
            #if you approach a wall from below
            if (MC.y < (wall.y + wall.height)) and ((MC.y + MC.height)) > (wall.y + wall.height):
                if (MC.x > wall.x) and ((MC.x + MC.width) < (wall.x + wall.width)):
                    MC.y += ((wall.y + wall.height) - MC.y)

            #if you approach a wall from the left
            if ((MC.x + MC.width) > wall.x) and (MC.x < wall.x):
                if (MC.y + MC.height) > wall.y and (MC.y < (wall.y + wall.height)):
                    MC.x -= ((MC.x + MC.width) - wall.x)

            #if you approach a wall from the right
            if (MC.x < (wall.x + wall.width)) and ((MC.x + MC.width) > (wall.x + wall.width)):
                if (MC.y + MC.height) > wall.y and (MC.y < (wall.y + wall.height)):
                    MC.x += ((wall.x + wall.width) - MC.x)
                    
                
        
        
    
            
    def ReDraw(self, window, MC, walls, battle):
        if self.battle == False:
            if wall85.y < MC.y and MC.x < wall147.x:
                pygame.draw.rect(window, LBrown, (0,0,X,Y))
            elif wall85.y >= MC.y and MC.x < wall147.x:
                pygame.draw.rect(window, red, (0,0,X,Y))
            elif MC.x >= wall147.x and MC.y < wall180.y:
                pygame.draw.rect(window, brown, (0,0,X,Y))
            elif MC.x >= wall147.x and MC.y >= wall180.y:
                pygame.draw.rect(window, LBlue, (0,0,X,Y))
            MC.draw(window)
            for wall in walls:
                wall.draw(window)
            Hodir.draw(window)
            pygame.display.update()
        

    def RandomEncounters(self, battle, window, fighters, enemies, MC, walls, expReduction):
        r = randint(1,30)
        if r == 5:
            n = randint(1,3)
            print(n)
            if n == 1:
                enemies.append(boi1)
            elif n == 2:
                enemies.append(boi1)
                enemies.append(boi2)
            else:
                enemies.append(boi1)
                enemies.append(boi2)
                enemies.append(boi3)
            self.BattleStart(battle, window, fighters, enemies, MC, walls, n, expReduction)

    def BattleStart(self, battle, window, fighters, enemies, MC, walls, n, expReduction):
        print('Show Time!')
        self.battle = True
        self.BattleDraw(window, fighters, enemies, battle, MC, walls, n, expReduction)
        
    def BattleDraw(self, window, fighters, enemies, battle, MC, walls, n, expReduction):
        if self.battle == True:
            pygame.draw.rect(window, pink, (0,0,X,Y))
            for fighter in fighters:
                fighter.draw(window)
                #append enemy list with random numbers here
            for enemy in enemies:
                enemy.draw(window)
            pygame.display.update()
            self.BattleControl(window, fighters, enemies, MC, walls, battle, n, expReduction)

    def BattleReDraw(self, window, fighters, enemies, battle):
        if self.battle == True:
            pygame.draw.rect(window, pink, (0,0,X,Y))
            for fighter in fighters:
                fighter.draw(window)
            for enemy in enemies:
                enemy.draw(window)
            pygame.display.update()

    def BattleControl(self, window, fighters, enemies, MC, walls, battle, n, expReduction):
        attacked = 0
        for i in range(n):
            enemies[n - 1].health = enemies[n - 1].maxHealth
            print(enemies[n - 1].health)
            
        #decides whether characters or enemies go first
        if fighters[0].speed > enemies[0].speed:
            playerTurn = True
        else:
            playerTurn = False
        while fighters != [] and enemies != []:
            if playerTurn == True:
                for fighter in fighters:
                    print(fighter.control)
                    moved = False
                    while moved == False:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_a:
                                    #Chooses enemy to attack
                                    valid = False
                                    while valid == False:
                                        if n != 1:
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN: 
                                                   if event.key == pygame.K_1:
                                                       attacked = 1
                                                   elif event.key == pygame.K_2:
                                                        attacked = 2
                                                   elif event.key == pygame.K_3:
                                                        attacked = 3
                                                if n == 2 and (attacked == 1 or attacked == 2):
                                                    valid = True
                                                elif n == 3 and(attacked == 1 or attacked == 2 or attacked == 3):
                                                    valid = True
                                        else:
                                            attacked = 1
                                            valid = True
                                        
                                    
                                    #put animation here
                                    damageGiven =  round(40 + (fighter.damage*(1 - enemies[attacked - 1].defence)))
                                    enemies[attacked - 1].health -= damageGiven
                                    moved = True
                                    print('Given',damageGiven, 'to enemy', attacked)
                                    if enemies[attacked - 1].health <= 0:
                                        for fighter in fighters:
                                            initialLvl = round(fighter.exp//100)
                                            fighter.exp += enemies[attacked - 1].exp
                                            lvl = round(fighter.exp//100)
                                            if lvl > initialLvl:
                                                lvlUp = lvl - initialLvl
                                                print(lvlUp)
                                                lvlUp = int(lvlUp)
                                                for i in range(lvlUp):
                                                    print('level up for', fighter)
                                                    fighter.damage += randint(1,4)
                                                    fighter.defence += randint(1,4)
                                                    fighter.speed += randint(1,4)
                                                    fighter.health += randint(10,14)
                                                    fighter.lvl += lvl
                                                for enemy in expReduction:
                                                    enemy.exp *= 0.85**lvlUp
                                            
                                        enemies.remove(enemies[attacked - 1])
                                        n -= 1
                                        self.BattleReDraw(window, fighters, enemies, battle)
                                        if n == 0:
                                            self.battle = False
                                            self.Control(window, MC, battle, walls, fighters, enemies, expReduction)
                                    #print damage given to the screen
                                    attacked = 0
                                if event.key == pygame.K_s:
                                    valid = False
                                    while valid == False:
                                        if n != 1:
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN: 
                                                   if event.key == pygame.K_1:
                                                       attacked = 1
                                                   elif event.key == pygame.K_2:
                                                        attacked = 2
                                                   elif event.key == pygame.K_3:
                                                        attacked = 3
                                                if n == 2 and (attacked == 1 or attacked == 2):
                                                    valid = True
                                                elif n == 3 and(attacked == 1 or attacked == 2 or attacked == 3):
                                                    valid = True

                                        else:
                                            attacked = 1
                                            valid = True                                    
                                    damageGiven = round(40 + (fighter.damage*(1 - enemies[attacked - 1].defence)))
                                    enemies[attacked - 1].health -= damageGiven
                                    moved = True
                                    print('Given',damageGiven, 'to enemy', attacked)
                                    if enemies[attacked - 1].health <= 0:
                                        for fighter in fighters:
                                            initialLvl = round(fighter.exp//100)
                                            fighter.exp += enemies[attacked - 1].exp
                                            lvl = round(fighter.exp//100)
                                            if lvl > initialLvl:
                                                lvlUp = round(lvl - initialLvl)
                                                lvlUp = int(lvlUp)
                                                print(lvlUp)
                                                for i in range(lvlUp):
                                                    print('level up for', fighter)
                                                    fighter.damage += randint(1,4)
                                                    fighter.defence += randint(1,4)
                                                    fighter.speed += randint(1,4)
                                                    fighter.health += randint(10,14)
                                                    fighter.lvl += lvl
                                                for enemy in expReduction:
                                                    enemy.exp *= 0.9**lvlUp
                                                    enemy.exp = round(enemy.exp)
                                                    
                                        enemies.remove(enemies[attacked - 1])
                                        n -= 1
                                        self.BattleReDraw(window, fighters, enemies, battle)
                                        if n == 0:
                                            self.battle = False
                                            self.Control(window, MC, battle, walls, fighters, enemies)
                                    attacked = 0
                    playerTurn = False
            else:#Enemy turn
                eMoved = False
                while eMoved == False:
                    if enemies != []:
                        for enemy in enemies:
                            temp = 123123
                            for fighter in fighters:
                                while temp == 123123:
                                    if fighter.health <= round(10 + (enemy.damage // fighter.defence)):
                                        temp = 1
                                        damageTaken = round(10 + (enemy.damage // fighter.defence))
                                        fighter.health -= damageTaken
                                        print('Taken',damageTaken)
                                        eMoved = True
                                        fighters.remove(fighter)
                                        playerTurn = True
                                    else:
                                        opp = randint(0, (len(fighters) - 1))
                                        temp = 1
                                        damageTaken = round(10 + (enemy.damage // fighter.defence))
                                        fighters[opp].health -= damageTaken
                                        print('Taken',damageTaken)
                                        eMoved = True
                                        playerTurn = True                                            
            
        


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 100


    def draw(self, window):
       pygame.draw.rect(window, black, (self.x, self.y, self.width, self.height))


class fighter(object): #player team stats and positions in battles
    def __init__(self, x, y, width, height, lvl, health, damage, defence, speed, exp, colour, control):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lvl = lvl
        self.health = health
        self.damage = damage
        self.defence = defence
        self.speed = speed
        self.colour = colour
        self.control = control
        self.exp = exp

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

class enemy(object): #enemy stats and positions during battle
    def __init__(self, x, y, width, height, lvl, maxHealth, health, damage, defence, speed, exp, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lvl = lvl
        self.maxHealth = maxHealth
        self.health = health
        self.damage = damage
        self.defence = defence
        self.speed = speed
        self.colour = colour
        self.exp = exp

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

class boss(object):
    def __init__(self, x, y, width, height, colour, health, damage, defence, speed, dialogue, exp, beaten):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.health = health
        self.damage = damage
        self.defence = defence
        self.speed = speed
        self.dialogue = dialogue
        self.exp = exp
        self.beaten = beaten
        
    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))

        
class wall(object):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))



MC = player(X//2, 500, 30, 80)
#walls for first area
wall1 = wall(0, 600, 1366, 100, brown)
wall2 = wall(0, 0, 200, 768, brown)
wall3 = wall(1166, 0, 200, 768, brown)
wall4 = wall(150, 200, 375, 150, brown)
wall5 = wall(850, 200, 350, 150, brown)
wall6 = wall((X//2 - 350), -250, (X//2 + 25), 300, brown)
wall7 = wall(0, -450, 200, 300, brown)
wall8 = wall(1166, -450, 200, 300, brown)
wall9 = wall(0, -550, 525, 100, brown)
wall10 = wall(850, -550, 516, 100, brown)
wall11 = wall(1360, 150, 500, 150, brown)
wall12 = wall(1860, -400, 100, 700, brown)
wall13 = wall(1710, -500, 250, 100, brown)
wall14 = wall(1250, -500, 300, 100, brown)
wall15 = wall(1450, -1250, 100, 750, brown)
wall16 = wall(1710, -1250, 100, 750, brown)
wall17 = wall(1710, -1250, 350, 100, brown)
wall18 = wall(1200, -1250, 250, 100, brown)
wall19 = wall(1200, -1400, 100, 150, brown)
wall20 = wall(1960, -1350, 100, 100, brown)
wall21 = wall(2010, -1350, 150, 100, brown)
wall22 = wall(2160, -1350, 100, 150, brown)
wall23 = wall(2160, -1300, 300, 100, brown)
wall24 = wall(2460, -1700, 100, 500, brown)
wall25 = wall(2160, -1700, 300, 100, brown)
wall26 = wall(2160, -1700, 100, 150, brown)
wall27 = wall(1960, -1650, 200, 100, brown)
wall28 = wall(1960, -1700, 100, 100, brown)
wall29 = wall(1200, -1700, 770, 100, brown)
wall30 = wall(1200, -1700, 100, 200, brown)
wall31 = wall(-500, -350, 500, 100, brown)
wall32 = wall(-500, 100, 500, 100, brown)
wall33 = wall(-500, -350, 100, 200, brown)
wall34 = wall(-500, 0, 100, 200, brown)
wall35 = wall(-550, -250, 100, 100, brown)
wall36 = wall(-550, 0, 100, 100, brown)
wall37 = wall(-650, -350, 100, 200, brown)
wall38 = wall(-650, 0, 100, 200, brown)
wall39 = wall(-950, 100, 400, 100, brown)
wall40 = wall(-950, -350, 400, 100, brown)
wall41 = wall(-1000, -350, 100, 550, brown)
wall42 = wall(0, -1700, 100, 1250, brown)
wall43 = wall(0, -1700, 500, 100, brown)
wall44 = wall(700, -1700, 500, 100, brown)
wall45 = wall(400, -1800, 100, 200, brown)
wall46 = wall(700, -1800, 100, 200, brown)
wall47 = wall(300, -1900, 200, 100, brown)
wall48 = wall(700, -1900, 200, 100, brown)
wall49 = wall(800, -2000, 100, 200, brown)
wall50 = wall(300, -2000, 100, 200, brown)
wall51 = wall(200, -2000, 200, 100, brown)
wall52 = wall(800, -2000, 200, 100, brown)
wall53 = wall(800, -2200, 200, 100, brown)
wall54 = wall(200, -2200, 200, 100, brown)
wall55 = wall(300, -2300, 100, 200, brown)
wall56 = wall(800, -2300, 100, 200, brown)
wall57 = wall(300, -2300, 200, 100, brown)
wall58 = wall(700, -2300, 200, 100, brown)
wall59 = wall(400, -2400, 100, 200, brown)
wall60 = wall(700, -2400, 100, 200, brown)
wall61 = wall(1000, -2300, 100, 200, brown)
wall62 = wall(1000, -2000, 100, 200, brown)
wall63 = wall(1000, -2300, 200, 100, brown)
wall64 = wall(1000, -1900, 500, 100, brown)
wall65 = wall(1400, -2300, 100, 400, brown)
wall66 = wall(1300, -2300, 200, 100, brown)
wall67 = wall(1100, -2600, 100, 300, brown)
wall68 = wall(1300, -2800, 100, 500, brown)
wall69 = wall(1000, -2700, 200, 100, brown)
wall70 = wall(1000, -2900, 400, 100, brown)
wall71 = wall(100, -2000, 100, 200, brown)
wall72 = wall(100, -2300, 100, 200, brown)
wall73 = wall(0, -2300, 200, 100, brown)
wall74 = wall(-300, -1900, 500, 100, brown)
wall75 = wall(-300, -2300, 100, 400, brown)
wall76 = wall(-300, -2300, 200, 100, brown)
wall77 = wall(-200, -2800, 100, 500, brown)
wall78 = wall(0, -2600, 100, 300, brown)
wall79 = wall(0, -2700, 200, 100, brown)
wall80 = wall(-200, -2900, 400, 100, brown)
wall81 = wall(200, -3000, 100, 200, brown)
wall82 = wall(900, -3000, 100, 200, brown)
wall83 = wall(200, -3000, 300, 100, brown)
wall84 = wall(700, -3000, 300, 100, brown)
wall85 = wall(400, -4000, 100, 1000, brown)
wall86 = wall(700, -4000, 100, 1000, brown)
wall87 = wall(200, -2700, 100, 300, brown)
wall88 = wall(200, -2500, 300, 100, brown)
wall89 = wall(700, -2500, 300, 100, brown)
wall90 = wall(900, -2700, 100, 200, brown)
#walls for second area
wall91 = wall(200, -4100, 300, 100, green)
wall92 = wall(700, -4100, 300, 100, green)
wall93 = wall(200, -4500, 100, 400, green)
wall94 = wall(900, -4500, 100, 400, green)
wall95 = wall(200, -4500, 300, 100, green)
wall96 = wall(700, -4500, 300, 100, green)
wall97 = wall(400, -4800, 100, 300, green)
wall98 = wall(700, -4800, 100, 300, green)
wall99 = wall(-200, -4900, 700, 100, green)
wall100 = wall(700, -4900, 700, 100, green)
wall101 = wall(-200, -5500, 100, 700, green)
wall102 = wall(1300, -5600, 100, 800, green)
wall103 = wall(0, -5150, 200, 100, black)#walls with black are slot machines
wall104 = wall(1000, -5150, 200, 100, black)
wall105 = wall(1000, -5710, 100, 300, black)
wall106 = wall(0, -5710, 100, 300, black)
wall107 = wall(-400, -5500, 300, 100, green)
wall108 = wall(-500, -5500, 100, 300, green)
wall109 = wall(-900, -5300, 500, 100, green)
wall110 = wall(-1000, -6000, 100, 800, green)
wall111 = wall(-1000, -6000, 500, 100, green)
wall112 = wall(-500, -6000, 100, 300, green)
wall113 = wall(-500, -5800, 400, 100, green)
wall114 = wall(-200, -6600, 100, 900, green)
wall115 = wall(-200, -6600, 700, 100, green)
wall116 = wall(700, -6600, 700, 100, green)
wall117 = wall(1300, -6600, 100, 100, green)
wall118 = wall(1300, -5900, 400, 100, green)
wall119 = wall(1300, -5600, 400, 100, green)
wall120 = wall(1600, -5600, 100, 300, green)
wall121 = wall(1600, -6100, 100, 300, green)
wall122 = wall(1600, -6100, 500, 100, green)
wall123 = wall(1600, -5400, 500, 100, green)
wall124 = wall(2100, -6100, 100, 800, green)
wall125 = wall(400, -6900, 100, 400, green)
wall126 = wall(700, -6900, 100, 400, green)
wall127 = wall(0, -6900, 500, 100, green)
wall128 = wall(700, -6900, 500, 100, green)
wall129 = wall(1100, -7500, 100, 700, green)
wall130 = wall(0, -7500, 100, 700, green)
wall131 = wall(0, -7500, 500, 100, green)
wall132 = wall(700, -7500, 500, 100, green)
wall133 = wall(400, -8300, 100, 900, green)
wall134 = wall(700, -8300, 100, 900, green)
wall135 = wall(0, -6400, 300, 100, black)
wall136 = wall(900, -6400, 300, 100, black)
wall137 = wall(1300, -6500, 100, 200, pink)#gateway to optional area
wall138 = wall(1300, -6300, 500, 100, green)
wall139 = wall(1300, -6500, 300, 100, green)
wall140 = wall(1800, -6600, 100, 400, green)
wall141 = wall(1500, -6900, 100, 500, green)
wall142 = wall(1800, -6600, 200, 100, green)
wall143 = wall(1500, -6900, 500, 100, green)
wall144 = wall(2000, -7000, 100, 200, green)
wall145 = wall(2000, -6600, 100, 200, green)
wall146 = wall(2000, -7100, 500, 100, green)
wall147 = wall(2000, -6400, 500, 100, green)
wall148 = wall(2500, -7100, 100, 300, red)
wall149 = wall(2500, -6600, 100, 300, red)
wall150 = wall(2500, -6600, 300, 100, red)
wall151 = wall(2500, -6900, 300, 100, red)
wall152 = wall(2800, -7300, 100, 500, red)
wall153 = wall(2800, -6600, 100, 500, red)
wall154 = wall(2800, -7300, 700, 100, red)
wall155 = wall(2800, -6200, 700, 100, red)
wall156 = wall(3400, -7300, 100, 500, red)
wall157 = wall(3400, -6600, 100, 500, red)
wall158 = wall(3400, -6900, 300, 100, red)
wall159 = wall(3400, -6600, 300, 100, red)
wall160 = wall(3700, -7500, 100, 700, red)
wall161 = wall(3700, -7500, 500, 100, red)
wall162 = wall(4100, -7800, 100, 300, red)
wall163 = wall(3900, -7800, 200, 100, red)
wall164 = wall(3900, -8100, 100, 300, red)
wall165 = wall(3900, -8200, 600, 100, red)
wall166 = wall(4500, -8200, 100, 400, red)
wall167 = wall(4400, -7800, 200, 100, red)
wall168 = wall(4400, -7800, 100, 600, red)
wall169 = wall(4000, -7200, 500, 100, red)
wall170 = wall(4000, -7200, 100, 1400, red)
wall171 = wall(3700, -6600, 100, 800, red)
wall172 = wall(4000, -5800, 200, 100, red)
wall173 = wall(3600, -5800, 200, 100, red)
wall174 = wall(3500, -5800, 100, 400, red)
wall175 = wall(4200, -5800, 100, 400, red)
wall176 = wall(4000, -5400, 300, 100, red)
wall177 = wall(3500, -5400, 300, 100, red)
wall178 = wall(3700, -5400, 100, 400, red)
wall179 = wall(4000, -5400, 100, 400, red)
wall180 = wall(3300, -5000, 500, 100, DBlue)
wall181 = wall(4000, -5000, 500, 100, DBlue)
wall182 = wall(3300, -5000, 100, 600, DBlue)
wall183 = wall(3300, -4400, 1200, 100, DBlue)
wall184 = wall(3700, -4600, 400, 100, black)#huts
wall185 = wall(4400, -5000, 100, 200, DBlue)
wall186 = wall(4400, -4500, 100, 200, DBlue)
wall187 = wall(4400, -4800, 600, 100, DBlue)
wall188 = wall(4400, -4500, 600, 100, DBlue)
wall189 = wall(4900, -4500, 100, 400, DBlue)
wall190 = wall(4900, -5200, 100, 400, DBlue)
wall191 = wall(4400, -5200, 500, 100, DBlue)
wall192 = wall(4400, -6200, 100, 1000, DBlue)
wall193 = wall(5600, -6200, 100, 1000, DBlue)
wall194 = wall(5200, -5200, 500, 100, DBlue)
wall195 = wall(5200, -5200, 100, 1100, DBlue)
wall196 = wall(4700, -4100, 300, 100, DBlue)
wall197 = wall(5200, -4100, 300, 100, DBlue)
wall198 = wall(4700, -4100, 100, 400, DBlue)
wall199 = wall(5400, -4100, 100, 400, DBlue)
wall200 = wall(4700, -3700, 800, 100, DBlue)

inventory = []

player = fighter(300, 200, 30, 80, 1, 3000, 10, 1, 12, 0, black, 'A: attack, S: ice spell, M: menu')
steve = fighter(300, 300, 30, 80, 3, 150, 15, 3, 12, 0, DBlue, 'A: attack, S: electricity spell, M: menu')
akechi = fighter(300, 400, 30, 80, 7, 200, 20, 6, 20, 0, white, 'A: attack, S: blessed spell, M: menu')
maria = fighter(300, 500, 30, 80, 10, 250, 28, 9, 30, 0, darkRed, 'A: attack, S: fire spell, M: menu')

boi1 = enemy(1000, 200, 30, 80, 1, 100, 100, 11, 0.08, randint(9,12), 30, green)
boi2 = enemy(1000, 400, 30, 80, 1, 100, 100, 11, 0.08, randint(9,12), 30, green)
boi3 = enemy(1000, 600, 30, 80, 1, 100, 100, 11, 0.08, randint(9,12), 30, green)

fighters = [player]
enemies = []
expReduction = [boi1, boi2, boi3]

Hodir = boss((X//2 - 115), -4300, 70, 120, DBlue, 600, 15, 0.6, 16, ' ', 150, False)

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19,
         wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28,
         wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37,
         wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46,
         wall47, wall48, wall49, wall50, wall51, wall52, wall53, wall54, wall55,
         wall56, wall57, wall58, wall59, wall60, wall61, wall62, wall63, wall64,
         wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72, wall73,
         wall74, wall75, wall76, wall77, wall78, wall79, wall80, wall81, wall82,
         wall83, wall84, wall85, wall86, wall87, wall88, wall89, wall90, wall91,
         wall92, wall93, wall94, wall95, wall96, wall97, wall98, wall99, wall100,
         wall101, wall102, wall103, wall104, wall105, wall106, wall107, wall108,
         wall109, wall110, wall111, wall112, wall113, wall114, wall115, wall116,
         wall117, wall118, wall119, wall120, wall121, wall122, wall123, wall124,
         wall125, wall126, wall127, wall128, wall129, wall130, wall131, wall132,
         wall133, wall134, wall135, wall136, wall137, wall138, wall139, wall140,
         wall141,wall142, wall143, wall144, wall145, wall146, wall147, wall148,
         wall149, wall150, wall151, wall152, wall153, wall154, wall155, wall156,
         wall157, wall158, wall159, wall160, wall161, wall162, wall163, wall164,
         wall165, wall166, wall167, wall168, wall169, wall170, wall171, wall172,
         wall173, wall174, wall175, wall176, wall177, wall178, wall179, wall180,
         wall181, wall182, wall183, wall184, wall185, wall186, wall187, wall188,
         wall189, wall190, wall191, wall192, wall193, wall194, wall195, wall196,
         wall197, wall198, wall199, wall200]



menu = MainMenu(window, option)
a = menu.MenuLoop(option)
game = Game(a, False)
game.NewOrContinue(a, window, MC, False, walls, fighters, enemies, expReduction)
    

