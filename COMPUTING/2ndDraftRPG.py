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

    def NewOrContinue(self, a, window, MC, battle, walls):#detects if the player chose new game or continue
        if self.a == 1:
            self.DrawNew(window, MC, battle, walls)
        elif self.a == 2:
            self.DrawLoad()


    def DrawNew(self, window, MC, battle, walls):
        pygame.draw.rect(window, LBrown, (0,0,X,Y))
        MC.draw(window)
        for wall in walls:
            wall.draw(window)
        pygame.display.update()
        self.Control(window, MC, battle, walls)

    def DrawLoad(self):
        pass #Will get variable values from database from when the player last saved

    def Control(self, window, MC, battle, walls):
        while self.battle == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ScrollUp(MC, walls)
                        if MC.y > (Y//2 - 20):
                            MC.y -= MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle)
                    if event.key == pygame.K_DOWN:
                        self.ScrollDown(MC, walls)
                        if MC.y < (Y//2 + 20):
                            MC.y += MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle)
                    if event.key == pygame.K_LEFT:
                        self.ScrollLeft(MC, walls)
                        if MC.x > (X//2 - 20):
                            MC.x -= MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle)
                    if event.key == pygame.K_RIGHT:
                        self.ScrollRight(MC, walls)
                        if MC.x < (X//2 + 20):
                            MC.x += MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle)
           
            self.ReDraw(window, MC, walls)


    def ScrollUp(self, MC, walls):
        if MC.y <= (Y//2 - 20):
            for wall in walls:
                wall.y += MC.vel

    def ScrollDown(self, MC, walls):
        if MC.y >= (Y//2 + 20):
            for wall in walls:
                wall.y -= MC.vel

    def ScrollLeft(self, MC, walls):
        if MC.x <= (X//2 - 20):
            for wall in walls:
                wall.x += MC.vel

    def ScrollRight(self, MC, walls):
        if MC.x >= (X//2 + 20):
            for wall in walls:
                wall.x -= MC.vel

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
                    
                
        
        
    
            
    def ReDraw(self, window, MC, walls):
        if wall85.y < MC.y:
            pygame.draw.rect(window, LBrown, (0,0,X,Y))
        elif wall85.y >= MC.y:
            pygame.draw.rect(window, red, (0,0,X,Y))
        MC.draw(window)
        for wall in walls:
            wall.draw(window)
        pygame.display.update()
        

    def RandomEncounters(self, battle):
        r = randint(1,30)
        if r == 5:
            self.BattleStart(battle)

    def BattleStart(self, battle):
        print('Show Time!')
        self.battle = True
        
            


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 70


    def draw(self, window):
       pygame.draw.rect(window, black, (self.x, self.y, self.width, self.height))


class fighter(object): #player team stats and positions in battles
    def __init__(self, x, y, width, height, lvl, health, damage, defence, speed, colour):
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

class enemy(object): #enemy stats and positions during battle
    def __init__(self, x, y, width, height, lvl, health, damage, defence, speed, colour):
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
wall91 = wall(0, -4500, 1000, 200, green)

player = fighter(50, 200, 30, 80, 1, 100, 10, 10, 10, black)
steve = fighter(50, 300, 30, 80, 3, 150, 15, 16, 12, green)
akechi = fighter(50, 400, 30, 80, 7, 200, 20, 22, 20, white)
maria = fighter(50, 500, 30, 80, 10, 250, 28, 29, 30, darkRed)

fighters = []

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19,
         wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28,
         wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37,
         wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46,
         wall47, wall48, wall49, wall50, wall51, wall52, wall53, wall54, wall55,
         wall56, wall57, wall58, wall59, wall60, wall61, wall62, wall63, wall64,
         wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72, wall73,
         wall74, wall75, wall76, wall77, wall78, wall79, wall80, wall81, wall82,
         wall83, wall84, wall85, wall86, wall87, wall88, wall89, wall90, wall91]



menu = MainMenu(window, option)
a = menu.MenuLoop(option)
game = Game(a, False)
game.NewOrContinue(a, window, MC, False, walls)
    

