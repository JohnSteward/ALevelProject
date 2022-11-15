import pygame
from random import randint
pygame.init()

coinage = 5000
X = 1366
Y= 768
red = (255,0,0)
darkRed = (60,0,0)
black = (0,0,0)
green = (0,255,0)
DGreen = (0,100,0)
white = (255,255,255)
brown = (65,43,21)
LBrown = (181,101,29)
pink = (255,110,199)
DBlue = (25,25,112)
LBlue = (65,105,225)
purple = (148,0,211)
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

    def NewOrContinue(self, a, window, MC, battle, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList, charList):#detects if the player chose new game or continue
        if self.a == 1:
            self.DrawNew(window, MC, battle, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList)
        elif self.a == 2:
            self.DrawLoad(window, MC, walls, battle, fighters, keyItems, NPCList, bossList, expReduction, charList)


    def DrawNew(self, window, MC, battle, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList):
        pygame.draw.rect(window, LBrown, (0,0,X,Y))
        MC.draw(window)
        for wall in walls:
            wall.draw(window)
        Hodir.draw(window)
        Shark.draw(window)
        Akechi.draw(window)
        LMaria.draw(window)
        Ludwig.draw(window)
        Kos.draw(window)
        Kira.draw(window)
        
        steven.draw(window)
        simon.draw(window)

        scroll.draw(window)
        
        pygame.display.update()
        self.Control(window, MC, battle, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList, charList)
    # Function to load the game from the last save
    def DrawLoad(self, window, MC, walls, battle, fighters, keyItems, NPCList, bossList, expReduction, charList):
        saveFile = open('saveFile.txt', 'r')
        keyItems = saveFile.readline()
        if 'relic' in keyItems:
            walls.remove(wall137)
        for wall in walls:
            wall.x = int(saveFile.readline())
        for wall in walls:
            wall.y = int(saveFile.readline())
        for NPC in NPCList:
            NPC.x = int(saveFile.readline())
        for NPC in NPCList:
            NPC.y = int(saveFile.readline())
        for NPC in NPCList:
            NPC.done = bool(saveFile.readline())
        for boss in bossList:
            boss.x = int(saveFile.readline())
        for boss in bossList:
            boss.y = int(saveFile.readline())
        for boss in bossList:
            boss.beaten = bool(saveFile.readline())
        charList = saveFile.readline()
        if 'player' in charList and player not in fighters:
            fighters.append(player)
            print('player added')
        if 'steve' in charList and steve not in fighters:
            fighters.append(steve)
            print('steve added')
        if 'akechi' in charList and akechi not in fighters:
            fighters.append(akechi)
            print('akechi added')
        if 'maria' in charList and maria not in fighters:
            fighters.append(maria)
            print('maria added')
        print(len(fighters))
        for fighter in fighters:
            fighter.lvl = int(saveFile.readline())
        for fighter in fighters:
            fighter.health = int(saveFile.readline())
        for fighter in fighters:
            fighter.damage = int(saveFile.readline())
        for fighter in fighters:
            fighter.defence = int(saveFile.readline())
        for fighter in fighters:
            fighter.speed = int(saveFile.readline())
        for fighter in fighters:
            fighter.exp = int(saveFile.readline())
        saveFile.close()
        self.ReDraw(window, MC, walls, battle)
        self.Control(window, MC, battle, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList, charList)
            


    def Control(self, window, MC, battle, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList, charList):
        while self.battle == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ScrollUp(MC, walls)
                        if MC.y > (Y//2 - 20):
                            MC.y -= MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle, window, fighters, enemies, MC, walls, expReduction)
                        Hodir.encounter(battle, window, fighters, enemies, MC, walls, Hodir.beaten, keyItems)
                        Shark.encounter(battle, window, fighters, enemies, MC, walls, Shark.beaten, keyItems)
                        Akechi.encounter(battle, window, fighters, enemies, MC, walls, Akechi.beaten, keyItems)
                        LMaria.encounter(battle, window, fighters, enemies, MC, walls, LMaria.beaten, keyItems)
                        Ludwig.encounter(battle, window, fighters, enemies, MC, walls, Ludwig.beaten, keyItems)
                        Kos.encounter(battle, window, fighters, enemies, MC, walls, Kos.beaten, keyItems)
                        Kira.encounter(battle, window, fighters, enemies, MC, walls, Kira.beaten, keyItems)
                    if event.key == pygame.K_DOWN:
                        self.ScrollDown(MC, walls)
                        if MC.y < (Y//2 + 20):
                            MC.y += MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle, window, fighters, enemies, MC, walls, expReduction)
                        Hodir.encounter(battle, window, fighters, enemies, MC, walls, Hodir.beaten, keyItems)
                        Shark.encounter(battle, window, fighters, enemies, MC, walls, Shark.beaten, keyItems)
                        Akechi.encounter(battle, window, fighters, enemies, MC, walls, Akechi.beaten, keyItems)
                        LMaria.encounter(battle, window, fighters, enemies, MC, walls, LMaria.beaten, keyItems)
                        Ludwig.encounter(battle, window, fighters, enemies, MC, walls, Ludwig.beaten, keyItems)
                        Kos.encounter(battle, window, fighters, enemies, MC, walls, Kos.beaten, keyItems)
                        Kira.encounter(battle, window, fighters, enemies, MC, walls, Kira.beaten, keyItems)
                    if event.key == pygame.K_LEFT:
                        self.ScrollLeft(MC, walls)
                        if MC.x > (X//2 - 20):
                            MC.x -= MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle, window, fighters, enemies, MC, walls, expReduction)
                        Hodir.encounter(battle, window, fighters, enemies, MC, walls, Hodir.beaten, keyItems)
                        Shark.encounter(battle, window, fighters, enemies, MC, walls, Shark.beaten, keyItems)
                        Akechi.encounter(battle, window, fighters, enemies, MC, walls, Akechi.beaten, keyItems)
                        LMaria.encounter(battle, window, fighters, enemies, MC, walls, LMaria.beaten, keyItems)
                        Ludwig.encounter(battle, window, fighters, enemies, MC, walls, Ludwig.beaten, keyItems)
                        Kos.encounter(battle, window, fighters, enemies, MC, walls, Kos.beaten, keyItems)
                        Kira.encounter(battle, window, fighters, enemies, MC, walls, Kira.beaten, keyItems)
                    if event.key == pygame.K_RIGHT:
                        self.ScrollRight(MC, walls)
                        if MC.x < (X//2 + 20):
                            MC.x += MC.vel
                        self.collision(MC, walls)
                        self.RandomEncounters(battle, window, fighters, enemies, MC, walls, expReduction)
                        Hodir.encounter(battle, window, fighters, enemies, MC, walls, Hodir.beaten, keyItems)
                        Shark.encounter(battle, window, fighters, enemies, MC, walls, Shark.beaten, keyItems)
                        Akechi.encounter(battle, window, fighters, enemies, MC, walls, Akechi.beaten, keyItems)
                        LMaria.encounter(battle, window, fighters, enemies, MC, walls, LMaria.beaten, keyItems)
                        Ludwig.encounter(battle, window, fighters, enemies, MC, walls, Ludwig.beaten, keyItems)
                        Kos.encounter(battle, window, fighters, enemies, MC, walls, Kos.beaten, keyItems)
                        Kira.encounter(battle, window, fighters, enemies, MC, walls, Kira.beaten, keyItems)
                    if event.key == pygame.K_SPACE:
                        self.slots(MC, wall105, keyItems)
                        steven.Encounter(MC, keyItems)
                        simon.Encounter(MC, keyItems)
                        scroll.pickUp(MC, keyItems)
                        if (steven.done == True) and (steve not in fighters):
                            fighters.append(steve)
                            if steven.viscinity == True:
                                print('Baldur has decided to join your cause')
                    if event.key == pygame.K_s:
                        self.saveGame(walls, NPCList, bossList, keyItems, fighters, charList)

                        
                    if Kira.beaten == True and Cthulhu.beaten == False:
                        enemies.append(Cthulhu)
                        for i in range(30):
                            Cthulhu.y += 10
                            self.ReDraw(window, MC, walls, battle)
                        Cthulhu.finalBossTrigger(keyItems, fighters, Cthulhu.beaten)
                        if Cthulhu.beaten == True:
                            print('You have saved this world from this abomination. The inhabitants will be eternally grateful.')
                            print(' ')
                            print('The End')
                            pygame.quit()
                        else:
                            print('Explore more to unlock other endings')
                            pygame.quit()
                        

            for character in charaList:
                if character == 'player':
                    if player not in fighters:
                        if player.health < 0:
                            player.health = 1
                        fighters.append(player)
                        
                if character == 'steve':
                    if (steven.done == True) and (steve not in fighters):
                        if steve.health < 0:
                            steve.health = 1
                        fighters.append(steve)
                        charList += 'steve'
                
                if character == 'akechi':
                    if (Akechi.beaten == True) and (akechi not in fighters):
                        if akechi.health < 0:
                            akechi.health = 1
                        fighters.append(akechi)
                        charList += 'akechi'
                if character == 'maria':
                    if (LMaria.beaten == True) and (maria not in fighters):
                        if maria.health < 0:
                            maria.health = 1
                        fighters.append(maria)
                        charList += 'maria'
                
                

            if ('relic' in keyItems) and (wall137 in walls):
                walls.remove(wall137)
                
            self.ReDraw(window, MC, walls, battle)


    def saveGame(self, walls, NPCList, bossList, keyItems, fighters, charList):
        saveFile = open('saveFile.txt', 'w')
        saveFile.write(str(keyItems))
        saveFile.write('\n')
        for wall in walls:
            saveFile.write(str(wall.x))
            saveFile.write('\n')
        for wall in walls:
            saveFile.write(str(wall.y))
            saveFile.write('\n')
        for NPC in NPCList:
            saveFile.write(str(NPC.x))
            saveFile.write('\n')
        for NPC in NPCList:
            saveFile.write(str(NPC.y))
            saveFile.write('\n')
        for NPC in NPCList:
            saveFile.write(str(NPC.done))
            saveFile.write('\n')
        for boss in bossList:
            saveFile.write(str(boss.x))
            saveFile.write('\n')
        for boss in bossList:
            saveFile.write(str(boss.y))
            saveFile.write('\n')
        for boss in bossList:
            saveFile.write(str(boss.beaten))
            saveFile.write('\n')
        saveFile.write(str(charList))
        saveFile.write('\n')
        for fighter in fighters:
            saveFile.write(str(fighter.lvl))
            saveFile.write('\n')
        for fighter in fighters:
            saveFile.write(str(fighter.health))
            saveFile.write('\n')
        for fighter in fighters:
            saveFile.write(str(fighter.damage))
            saveFile.write('\n')
        for fighter in fighters:
            saveFile.write(str(fighter.defence))
            saveFile.write('\n')
        for fighter in fighters:
            saveFile.write(str(fighter.speed))
            saveFile.write('\n')
        for fighter in fighters:
            saveFile.write(str(fighter.exp))
            saveFile.write('\n')
        saveFile.close()
            
        print('Saved')


    def ScrollUp(self, MC, walls):
        if MC.y <= (Y//2 - 20):
            for wall in walls:
                wall.y += MC.vel
            Hodir.y += MC.vel
            Shark.y += MC.vel
            Akechi.y += MC.vel
            LMaria.y += MC.vel
            Ludwig.y += MC.vel
            Kos.y += MC.vel
            Kira.y += MC.vel
            Cthulhu.y += MC.vel
            steven.y += MC.vel
            simon.y += MC.vel
            scroll.y += MC.vel

    def ScrollDown(self, MC, walls):
        if MC.y >= (Y//2 + 20):
            for wall in walls:
                wall.y -= MC.vel
            Hodir.y -= MC.vel
            Shark.y -= MC.vel
            Akechi.y -= MC.vel
            LMaria.y -= MC.vel
            Ludwig.y -= MC.vel
            Kos.y -= MC.vel
            Kira.y -= MC.vel
            Cthulhu.y -= MC.vel
            steven.y -= MC.vel
            simon.y -= MC.vel
            scroll.y -= MC.vel

    def ScrollLeft(self, MC, walls):
        if MC.x <= (X//2 - 20):
            for wall in walls:
                wall.x += MC.vel
            Hodir.x += MC.vel
            Shark.x += MC.vel
            Akechi.x += MC.vel
            LMaria.x += MC.vel
            Ludwig.x += MC.vel
            Kos.x += MC.vel
            Kira.x += MC.vel
            Cthulhu.x += MC.vel
            steven.x += MC.vel
            simon.x += MC.vel
            scroll.x += MC.vel

    def ScrollRight(self, MC, walls):
        if MC.x >= (X//2 + 20):
            for wall in walls:
                wall.x -= MC.vel
            Hodir.x -= MC.vel
            Shark.x -= MC.vel
            Akechi.x -= MC.vel
            LMaria.x -= MC.vel
            Ludwig.x -= MC.vel
            Kos.x -= MC.vel
            Kira.x -= MC.vel
            Cthulhu.x -= MC.vel
            steven.x -= MC.vel
            simon.x -= MC.vel
            scroll.x -= MC.vel

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
            if ((MC.x + MC.width) >= wall.x) and (MC.x <= wall.x):
                if (MC.y + MC.height) > wall.y and (MC.y < (wall.y + wall.height)):
                    MC.x -= ((MC.x + MC.width) - wall.x)

            #if you approach a wall from the right
            if (MC.x <= (wall.x + wall.width)) and ((MC.x + MC.width) >= (wall.x + wall.width)):
                if (MC.y + MC.height) > wall.y and (MC.y < (wall.y + wall.height)):
                    MC.x += ((wall.x + wall.width) - MC.x)
                    
                
        
    def slots(self, MC, wall105, keyItems):
        global coinage
        if coinage >= 20:
            if MC.x + MC.width == wall105.x:
                if MC.y >= wall105.y and (MC.y + MC.height) <= (wall105.y + wall105.height):
                    coinage -= 20
                    print('you have', coinage, 'coins left')
                    a = randint(1,3)
                    print(a)
                    b = randint(1,3)
                    print(b)
                    c = randint(1,3)
                    print(c)
                    if a == b and b == c:
                        coinage += 150
                        if 'relic' not in keyItems:
                            print('you have gained 150 coins and a mysterious relic')
                            keyItems.append('relic')
                        else:
                            print('You have gained 150 coins')
        elif coinage < 20:
            print('You do not have enough coins')
    
            
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
            if MC.y < wall133.y:
                pygame.draw.rect(window, DGreen, (0,0,X,Y))
            MC.draw(window)
            for wall in walls:
                wall.draw(window)
            if Hodir.beaten == False:
                Hodir.draw(window)
            if Shark.beaten == False:
                Shark.draw(window)
            if Akechi.beaten == False:
                Akechi.draw(window)
            if LMaria.beaten == False:
                LMaria.draw(window)
            if Ludwig.beaten == False:
                Ludwig.draw(window)
            if Kos.beaten == False:
                Kos.draw(window)
            if Kira.beaten == False:
                Kira.draw(window)
            if Cthulhu.beaten == False:
                Cthulhu.draw(window)

            if scroll.picked == False:
                scroll.draw(window)
                
            steven.draw(window)
            simon.draw(window)
            pygame.display.update()
        

    def RandomEncounters(self, battle, window, fighters, enemies, MC, walls, expReduction):
        r = randint(1,30)
        if r == 5:
            n = randint(1,3)
            print(n, 'enemies have appeared')
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
        drop = n
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
                                    damageGiven =  round(40 + (fighter.damage // enemies[attacked - 1].defence))
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
                                                    fighter.damage += randint(3,5)
                                                    fighter.defence += randint(3,5)
                                                    fighter.speed += randint(3,5)
                                                    fighter.maxHealth += randint(30,40)
                                                    fighter.lvl += lvl
                                                for enemy in expReduction:
                                                    enemy.exp *= 0.85**lvlUp
                                            
                                        enemies.remove(enemies[attacked - 1])
                                        n -= 1
                                        self.BattleReDraw(window, fighters, enemies, battle)
                                        if n == 0:
                                            self.itemDrop(drop, itemList, battleItems)
                                            self.battle = False
                                            self.Control(window, MC, battle, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList, charList)
                                    #print damage given to the screen
                                    attacked = 0
                                elif event.key == pygame.K_s:
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
                                    damageGiven = round(40 + (fighter.damage // enemies[attacked - 1].defence))
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
                                                    fighter.damage += randint(3,5)
                                                    fighter.defence += randint(3,5)
                                                    fighter.speed += randint(3,5)
                                                    fighter.maxHealth += randint(10,14)
                                                    fighter.lvl += lvl
                                                for enemy in expReduction:
                                                    enemy.exp *= 0.9**lvlUp
                                                    enemy.exp = round(enemy.exp)
                                                    
                                        enemies.remove(enemies[attacked - 1])
                                        n -= 1
                                        self.BattleReDraw(window, fighters, enemies, battle)
                                        if n == 0:
                                            self.itemDrop(drop, itemList, battleItems)
                                            self.battle = False
                                            self.Control(window, MC, battle, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList, charList)
                                    attacked = 0

                                elif event.key == pygame.K_m:
                                    itemUse = 0
                                    for item in battleItems:
                                        print(item.listValue)
                                        fighterChoose = 0
                                    while itemUse == 0:
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_1 and len(battleItems) >= 1:
                                                    itemUse = 1
                                                elif event.key == pygame.K_2 and len(battleItems) >= 2:
                                                    itemUse = 2
                                                elif event.key == pygame.K_3 and len(battleItems) >= 3:
                                                    itemUse = 3
                                                elif event.key == pygame.K_4 and len(battleItems) >= 4:
                                                    itemUse = 4
                                                elif event.key == pygame.K_5 and len(battleItems) >= 5:
                                                    itemUse = 5
                                                elif event.key == pygame.K_6 and len(battleItems) >= 6:
                                                    itemUse = 6
                                                elif event.key == pygame.K_7 and len(battleItems) >= 7:
                                                    itemUse = 7
                                    print('Choose fighter to use the item on')
                                    while fighterChoose == 0:
                                        for event in pygame.event.get():
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_1:
                                                    fighterChoose = 1
                                                    print('chosen fighter 1')
                                                elif event.key == pygame.K_2 and len(fighters) >= 2:
                                                    fighterChoose = 2
                                                    print('chosen fighter 2')
                                                elif event.key == pygame.K_3 and len(fighters) >= 3:
                                                    fighterChoose = 3
                                                    print('chosen fighter 3')
                                                elif event.key == pygame.K_4 and len(fighters) >= 4:
                                                    fighterChoose = 4
                                                    print('chosen fighter 4')
                                    if battleItems[itemUse - 1].listValue == 'Potion':
                                        if fighters[fighterChoose - 1].maxHealth - fighters[fighterChoose - 1].health >= 100:
                                            fighters[fighterChoose - 1].health += 100
                                        else:
                                            fighters[fighterChoose - 1].health += (fighters[fighterChoose - 1].maxHealth - fighters[fighterChoose - 1].health)
                                    elif battleItems[itemUse - 1].listValue == 'atkUp':
                                        fighters[fighterChoose - 1].damage += 5
                                    elif battleItems[itemUse - 1].listValue == 'defUp':
                                        fighters[fighterChoose - 1].defence += 5
                                    battleItems.remove(battleItems[itemUse - 1])
                                    moved = True
                                            
                    playerTurn = False
            else:
                eMoved = False
                while eMoved == False:
                    if enemies != []:
                        for enemy in enemies:
                            temp = 123123
                            while temp == 123123:
                                for fighter in fighters:
                                    if fighter.health <= round(10 + (enemy.damage // fighter.defence)):
                                        temp = 1
                                        damageTaken = round(10 + (enemy.damage // fighter.defence))
                                        fighter.health -= damageTaken
                                        print('Taken',damageTaken)
                                        eMoved = True
                                        if fighter.health < 0:
                                            print('fighter has died')
                                            fighters.remove(fighter)
                                            self.BattleReDraw(window, fighters, enemies, battle)
                                if temp == 123123:
                                    opp = randint(0, len(fighters))
                                    temp = 1
                                    if opp < len(fighters):
                                        damageTaken = round(10 + (enemy.damage // fighter.defence))
                                        fighters[opp].health -= damageTaken
                                        print('Taken',damageTaken)
                                    else:
                                        enemy.damage += 5
                                        print('enemy attack has increased')
                                    i = 0
                                    for fighter in fighters:
                                        i += 1
                                        print('fighter', i, 'has', fighter.health, 'health left')
                                    eMoved = True                                            
                playerTurn = True
        
    def itemDrop(self, drop, itemList, battleItems):
        global coinage
        for i in range(drop):
            chance = randint(1,3)
            if chance == 1:
                x = randint(1,3)
                if len(battleItems) <= 7:
                    battleItems.append(itemList[x - 1])
                    print('received ', itemList[x - 1].listValue)
                else:
                    print('Item inventory is full')
            coinage += 50
            

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 30


    def draw(self, window):
       pygame.draw.rect(window, black, (self.x, self.y, self.width, self.height))


class fighter(object): #player team stats and positions in battles
    def __init__(self, x, y, width, height, lvl, health, maxHealth, damage, defence, speed, exp, colour, control):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lvl = lvl
        self.health = health
        self.maxHealth = maxHealth
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
    def __init__(self, x, y, width, height, colour, health, maxHealth, damage, defence, speed, dialogue, exp, beaten, drop):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.health = health
        self.maxHealth = maxHealth
        self.damage = damage
        self.defence = defence
        self.speed = speed
        self.dialogue = dialogue
        self.exp = exp
        self.beaten = beaten
        self.drop = drop
        
    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))
    # Triggers the boss battle when the player is close
    def encounter(self, battle, window, fighters, enemies, MC, walls, beaten, keyItems):
        if ((MC.y - (self.y + self.height) < 50 and MC.y - (self.y + self.height) > 0 and ((MC.x + MC.width > self.x) and (MC.x) < (self.x + self.height)) and self.beaten == False)) or ((self.y -(MC.y + MC.height) < 50 and (self.y - (MC.y + MC.height)) > 0 and ((MC.x + MC.width > self.x) and (MC.x) < (self.x + self.height)) and self.beaten == False)):
            print(self.dialogue)
            cont = False
            while cont == False:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.x = 1000
                            self.y = 300
                            enemies.append(self)
                            self.bossFightDraw(window, fighters, enemies, beaten, keyItems)
                            cont = True

    def bossFightDraw(self, window, fighters, enemies, beaten, keyItems):
        pygame.draw.rect(window, pink, (0,0,X,Y))
        for fighter in fighters:
            fighter.draw(window)
            
        for enemy in enemies:
            enemy.draw(window)
        pygame.display.update()
        self.bossFightControl(fighters, enemies, beaten, keyItems)

    def bossFightReDraw(self, window, fighters, enemies, beaten):
        pygame.draw.rect(window, pink, (0,0,X,Y))
        for fighter in fighters:
            fighter.draw(window)
            
        for enemy in enemies:
            enemy.draw(window)
        pygame.display.update()

    #Criteria for different endings
    def finalBossTrigger(self, keyItems, fighters, beaten):
        for i in keyItems:
            print(i)
        print(len(fighters))
        if (('Left eye' in keyItems) or ('Right eye' in keyItems)) and ('relic' not in keyItems):
            print('YOU CAN SEE ME, YET YOU CANNOT DEFEAT ME. HAHA! THIS WILL MAKE IT ALL THE MORE FUN AS I DESTROY THIS WORLD WITH YOU IN IT')
            print(' ')
            print('Since you had no way of defeating this immortal monster, it was able to destroy this world with no opposition')
        elif (('Left eye' in keyItems) or ('Right eye' in keyItems)) and ('relic' in keyItems) and (len(fighters) < 4):
            print('THE RELIC HAS REJECTED YOU! YOUR EFFORTS IN SAVING THIS WORLD ARE FUTILE')
            print(' ')
            print('Since the relic rejected your body as its vessel, you did not have the power do defeat the monster, and you were destroyed along with the world')
        elif ('Right eye' in keyItems) and ('Left eye' in keyItems) and ('relic' in keyItems) and (len(fighters) == 4):
            print('THE RELIC HAS ACCEPTED YOU AS ITS VESSEL. NO MATTER, I WILL JUST DESTROY YOU MYSELF')
            self.bossFightControl(fighters, enemies, beaten, keyItems)
        else:
            print('IT LOOKS AS THOUGH YOU CANNOT EVEN SEE ME. YOU HAVE FAILED, JUST AS HODIR DID BEFORE YOU. PERISH, LOWLEY INSECT!')
            print('You did not have the necessary items to fight the monster, so it was able to destroy this world with you in it.')

    def bossFightControl(self, fighters, enemies, beaten, keyItems):
        attacked = 0
        n = 1
        while self.beaten == False:
            if fighters[0].speed > enemies[0].speed:
                playerTurn = True
            else:
                playerTurn = False
            while fighters != [] and enemies != []:
                if playerTurn == True:
                    for fighter in fighters:
                        if self.beaten == False:
                            print(fighter.control)
                            moved = False
                            while moved == False:
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_a:
                                            #Chooses enemy to attack
                                            valid = False
                                            while valid == False:
                                                if n > 1:
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
                                            damageGiven =  round(40 + (fighter.damage // enemies[attacked - 1].defence))
                                            enemies[attacked - 1].health -= damageGiven
                                            moved = True
                                            print('Given',damageGiven, 'to the boss')
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
                                                            fighter.damage += randint(3,5)
                                                            fighter.defence += randint(3,5)
                                                            fighter.speed += randint(3,5)
                                                            fighter.maxHealth += randint(30,40)
                                                            fighter.lvl += lvl
                                                        for enemy in expReduction:
                                                            enemy.exp *= 0.85**lvlUp
                                                    
                                                enemies.remove(enemies[attacked - 1])
                                                n -= 1
                                                if n == 0:
                                                    self.beaten = True
                                            #print damage given to the screen
                                            attacked = 0
                                        if event.key == pygame.K_s:
                                            valid = False
                                            while valid == False:
                                                if n > 1:
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
                                            damageGiven = round(40 + (fighter.damage // enemies[attacked - 1].defence))
                                            enemies[attacked - 1].health -= damageGiven
                                            moved = True
                                            print('Given',damageGiven, 'to the boss')
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
                                                            fighter.damage += randint(3,5)
                                                            fighter.defence += randint(3,5)
                                                            fighter.speed += randint(3,5)
                                                            fighter.maxHealth += randint(30,40)
                                                            fighter.lvl += lvl
                                                        for enemy in expReduction:
                                                            enemy.exp *= 0.85**lvlUp
                                                            enemy.exp = round(enemy.exp)
                                                            
                                                enemies.remove(enemies[attacked - 1])
                                                n -= 1
                                                if n == 0:
                                                    self.beaten = True
                                            attacked = 0

                                        if event.key == pygame.K_m:
                                            itemUse = 0
                                            for item in battleItems:
                                                print(item.listValue)
                                                fighterChoose = 0
                                            while itemUse == 0:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.KEYDOWN:
                                                        if event.key == pygame.K_1 and len(battleItems) >= 1:
                                                            itemUse = 1
                                                        elif event.key == pygame.K_2 and len(battleItems) >= 2:
                                                            itemUse = 2
                                                        elif event.key == pygame.K_3 and len(battleItems) >= 3:
                                                            itemUse = 3
                                                        elif event.key == pygame.K_4 and len(battleItems) >= 4:
                                                            itemUse = 4
                                                        elif event.key == pygame.K_5 and len(battleItems) >= 5:
                                                            itemUse = 5
                                                        elif event.key == pygame.K_6 and len(battleItems) >= 6:
                                                            itemUse = 6
                                                        elif event.key == pygame.K_7 and len(battleItems) >= 7:
                                                            itemUse = 7
                                            print('Choose fighter to use the item on')
                                            while fighterChoose == 0:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.KEYDOWN:
                                                        if event.key == pygame.K_1:
                                                            fighterChoose = 1
                                                            print('chosen fighter 1')
                                                        elif event.key == pygame.K_2 and len(fighters) >= 2:
                                                            fighterChoose = 2
                                                            print('chosen fighter 2')
                                                        elif event.key == pygame.K_3 and len(fighters) >= 3:
                                                            fighterChoose = 3
                                                            print('chosen fighter 3')
                                                        elif event.key == pygame.K_4 and len(fighters) >= 4:
                                                            fighterChoose = 4
                                                            print('chosen fighter 4')
                                            if battleItems[itemUse - 1].listValue == 'Potion':
                                                if fighters[fighterChoose - 1].maxHealth - fighters[fighterChoose - 1].health >= 100:
                                                    fighters[fighterChoose - 1].health += 100
                                                else:
                                                    fighters[fighterChoose - 1].health += (fighters[fighterChoose - 1].maxHealth - fighters[fighterChoose - 1].health)
                                            elif battleItems[itemUse - 1].listValue == 'atkUp':
                                                fighters[fighterChoose - 1].damage += 3
                                            elif battleItems[itemUse - 1].listValue == 'defUp':
                                                fighters[fighterChoose - 1].defence += 3
                                            battleItems.remove(battleItems[itemUse - 1])
                                            moved = True
                                                
                        playerTurn = False
                else:
                    #Enemy turn
                    eMoved = False
                    while eMoved == False:
                        if enemies != []:
                            for enemy in enemies:
                                temp = 123123
                                while temp == 123123:
                                    for fighter in fighters:
                                        if fighter.health <= round(10 + (enemy.damage // fighter.defence)):
                                            temp = 1
                                            damageTaken = round(10 + (enemy.damage // fighter.defence))
                                            fighter.health -= damageTaken
                                            print('Taken',damageTaken)
                                            if fighter.health < 0:
                                                print('fighter has died')
                                                eMoved = True
                                                fighters.remove(fighter)
                                                self.bossFightReDraw(window, fighters, enemies, beaten)
                                    if temp == 123123:
                                        opp = randint(0, len(fighters))
                                        temp = 1
                                        if opp < len(fighters):
                                            damageTaken = round(10 + (enemy.damage // fighter.defence))
                                            fighters[opp].health -= damageTaken
                                            print('Taken',damageTaken)
                                        else:
                                            buff = randint(1,3)
                                            #The boss can buff instead of attack
                                            if buff == 1:
                                                self.damage += 3
                                                print('boss attack power has increased')
                                            elif buff == 2:
                                                self.defence += 3
                                                print('boss defence has increased')
                                            else:
                                                self.health += 30
                                                print('boss has healed 30 health')
                                        print('boss has', self.health, 'health left')
                                        i = 0
                                        for fighter in fighters:
                                            i += 1
                                            print('fighter', i, 'has', fighter.health, 'left')
                                        eMoved = True
                    playerTurn = True
        print('The boss has been defeated')
        keyItems.append(self.drop)

class NPC(object):
    def __init__(self, x, y, width, height, colour, dialogueA, dialogueB, request, reward, done, coins, viscinity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.dialogueA = dialogueA
        self.dialogueB = dialogueB
        self.request = request
        self.reward = reward
        self.done = done
        self.coins = coins
        self.viscinity = viscinity

    def draw(self, window):
        pygame.draw.rect(window, self.colour, (self.x, self.y, self.width, self.height))
        
    def Encounter(self, MC, keyItems):
        global coinage
        if ((self.x - (MC.x + MC.width)) < 50) and ((self.x - (MC.x + MC.width)) > 0) and ((MC.y < (self.y + self.height)) and ((MC.y + MC.height) > self.y)):
            self.viscinity = True
            if self.done == False:
                print(self.dialogueA)
            if self.request in keyItems and self.done == False:
                print(self.dialogueB)
                keyItems.append(self.reward)
                coinage += self.coins
                self.done = True
        else:
            self.viscinity = False
            
            
class overworldItem(object):
    def __init__(self, x, y, width, height, listValue, picked):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.listValue = listValue
        self.picked = picked
        
    def draw(self, window):
        pygame.draw.rect(window, DBlue, (self.x, self.y, self.width, self.height))

    def pickUp(self, MC, keyItems):
        if (self.x > MC.x) and ((self.x + self.width) < (MC.x + MC.width)):
            if (self.y > MC.y) and ((self.y + self.height) < (MC.y + MC.height)):
                self.picked = True
                keyItems.append(self.listValue)
                print('Picked up', self.listValue)
                
            
        
class battleItem(object):
    def __init__(self, function, listValue):
        self.function = function
        self.listValue = listValue

        
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
wall103 = wall(0, -5150, 200, 100, black)
wall104 = wall(1000, -5150, 200, 100, black)
wall105 = wall(1000, -5710, 100, 300, brown)#slot machine
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

scroll = overworldItem(200, -1000, 10, 10, 'scroll', False)

keyItems = ['Left eye', 'Right eye']
battleItems = []


player = fighter(300, 200, 30, 80, 1, 10000, 10000, 15, 1, 12, 0, black, 'A: attack, S: ice spell, M:  item menu')
steve = fighter(300, 300, 30, 80, 3, 10000, 10000, 19, 3, 12, 0, DBlue, 'A: attack, S: electricity spell, M: item menu')
akechi = fighter(300, 400, 30, 80, 7, 10000, 10000, 25, 6, 20, 0, white, 'A: attack, S: blessed spell, M: item menu')
maria = fighter(300, 500, 30, 80, 10, 10000, 10000, 29, 9, 30, 0, darkRed, 'A: attack, S: fire spell, M: item menu')

boi1 = enemy(1000, 200, 30, 80, 1, 100, 100, 11, 1, randint(9,12), 30, green)
boi2 = enemy(1000, 400, 30, 80, 1, 100, 100, 11, 1, randint(9,12), 30, green)
boi3 = enemy(1000, 600, 30, 80, 1, 100, 100, 11, 1, randint(9,12), 30, green)

potion = battleItem('Heal 100', 'Potion')
atkUp = battleItem('Damage Increase', 'atkUp')
defUp = battleItem('Defence increase', 'defUp')

steven = NPC(2400, -1500, 50, 100, DBlue, 'If you want to know some of what is happening within this twisted world, you will want to fetch me the scroll from the town square. You will be rewarded', 'Glaive Master Hodir is a man who has been cursed for all eternity to test those who come through here. Those who can best him, in his eyes, may be able to succeed where he could not.', 'scroll', 'Right eye', False, 100, False)
simon = NPC(wall184.x + 30, wall184.y - 100, 50, 100, red, 'Interested in nightmares, eh? There is a terrible secret in this one. If you fetch me the Rakuyo from that well over there, maybe I will help you to understand.', 'This fishing hamlet is a peaceful, prosperous fishing village. There is a secret hidden deep within this village. They say the great one, named Kos, resides near the ocean on the very edge of this Hamlet. The people of this village, in exchange for bountiful fishing harvests and immortality, they routinely offer human sacrifices to Kos, and throw away their humanity to become hideous fish beasts', 'Rakuyo', 'Left eye', False, 100, False)

itemList = [potion, atkUp, defUp]
NPCList = [steven, simon]
fighters = [player, steve]
enemies = []
expReduction = [boi1, boi2, boi3]

Hodir = boss((X//2 - 115), -4300, 70, 120, darkRed, 600, 600, 15, 3, 16, 'Hand it over. That thing. Your Dark Sock', 150, False, '')
Shark = boss(wall198.x + 330, wall200.y - 150, 70, 120, DBlue, 1000, 1000, 30, 3, 20, 'REEEEEEEEEE', 150, False, 'Rakuyo')
Akechi = boss(wall125.x + 130, wall127.y - 150, 50, 120, darkRed, 1000, 1000, 25, 2, 21, 'AHAHAHAHA YOU WILL DIE HERE TODAY', 200, False, '')
LMaria = boss(wall172.x - 130, wall172.y + 250, 70, 120, darkRed, 1300, 1300, 27, 3, 40, 'A corpse should be left well alone. Only an honest death can cure you now', 230, False, '')
Ludwig = boss(wall155.x + 250, wall150.y - 120, 70, 120, DBlue, 1200, 1200, 25, 3, 36, 'Help us please. Here he comes. An unsightly beast', 200, False, '')
Kos = boss(wall190.x + 150, wall191.y - 400, 70, 120, DBlue, 2000, 2000, 40, 4, 45, '...', 350, False, '')
Kira = boss(wall133.x + 170, wall133.y - 220, 70, 120, purple, 2500, 2500, 40, 4, 40, 'My name is Yoshikage Kira. Oh you know the rest. I shant lose to you scum.', 300, False, '')
Cthulhu = boss(wall133.x - 50, wall133.y - 400, 150, 200, pink, 1, 1, 1, 1, 1, 'YOU WILL DIE BEFORE ME, AND I WILL USE YOUR CORPSE AS A PUPPET, JUST LIKE WITH YOSHIKAGE KIRA. GOODBYE INSECT', 1000, False, '')

bossList = [Hodir, Shark, Akechi, LMaria, Ludwig, Kos, Kira, Cthulhu]

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

charList = 'playersteve'
charaList = ['player', 'steve', 'akechi', 'maria']

menu = MainMenu(window, option)
a = menu.MenuLoop(option)
game = Game(a, False)
game.NewOrContinue(a, window, MC, False, walls, fighters, enemies, expReduction, keyItems, NPCList, bossList, charList)
    

