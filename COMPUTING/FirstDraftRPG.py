import pygame
from random import randint
pygame.init()

X = 1366
Y= 768
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
window = pygame.display.set_mode((X, Y))#making the window
menuBackground = [pygame.image.load('Images/MenuBackground.png').convert_alpha()]
run = True
menu = True
chosen = False
option = 0
play = False

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5


    def draw(self, window):
        print(play)
        if play == True:
            print('fgwhg')
            pygame.draw.rect(window, black, (self.x, self.y, self.width, self.height))
            #draws the main character sprite when the game is being played
        

        
def MainMenu(window):
    #placing all of the text onto the main menu: the 2 options and the title
    global option
    global chosen
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
    keys = pygame.key.get_pressed()
    # if down is pressed, the marker will move to the continue game option
    # if up is pressed, the marker will move to the new game option
    if keys[pygame.K_DOWN] and chosen == False:
        option = 2
    elif keys[pygame.K_UP] and chosen == False:
        option = 1
    
    # if you use the arrow keys, you can move the marker between the 2 options
    if option == 1:
        optionNewGame = pygame.draw.polygon(window, red, ((X//2 - 70, Y//2 - 50), (X//2 - 90, Y//2 - 70), (X//2 - 90, Y//2 - 30)))
        optionContinueGame = pygame.draw.polygon(window, black, ((X//2 - 100, Y//2), (X//2 - 120, Y//2 - 20), (X//2 - 120, Y//2 + 20)))

    elif option == 2:
        optionContinueGame = pygame.draw.polygon(window, red, ((X//2 - 100, Y//2), (X//2 - 120, Y//2 - 20), (X//2 - 120, Y//2 + 20)))
        optionNewGame = pygame.draw.polygon(window, black, ((X//2 - 70, Y//2 - 50), (X//2 - 90, Y//2 - 70), (X//2 - 90, Y//2 - 30)))
    # choosing your option
    if keys[pygame.K_SPACE]:
        chosen = True

    if chosen == True:
        if option == 1:
            New(window)
        elif option == 2:
            Continue()

a = []
a =22
def New(window):
    global play
    play = True
    pygame.draw.rect(window, red,(0, 0, 1366, 768))
    redrawGame()
    




def Continue():
    play = True
    pygame.draw.rect(window, green,(0, 0, 1366, 768))




def redrawMenu():
    window.blit(menuBackground[0], (0,0))#adds the image to the window

def redrawGame():
    MC.draw(window)


MC = player(X//2, Y//2, 30, 80)
# main loop
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            if menu == True:
                redrawMenu()
                a = MainMenu(window)
            else:
                run = False
    pygame.display.update()#redraws the current images to the window
    

pygame.quit()
