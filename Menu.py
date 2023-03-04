import pygame
import sys
from Background import drawDisplay      
from ButtonClass import button             
from Tutorial import tutorial
from Controls import controls
from SelectDifficulty import selectDifficulty
from PlayerStats import playerStatsMain
pygame.init()                           
pygame.font.init()                      


#Displays the title 'Menu'#
def displayMenuText (screen):
    font = pygame.font.SysFont ('Calibri', 60, False, False)    
    menuTitle = font.render ("Menu", True, (255, 255, 255))    
    screen.blit (menuTitle, (531, 100))                         
    return screen


#Creates instances of the class Button and displays them#
def displayButtons (screen):
    buttonColour = pygame.image.load ("Images\Button colour.png").convert_alpha ()    
    buttonColour = pygame.transform.scale (buttonColour, (300,50))             

    #Creates instances of the class button
    singleplayerBtn = button(450, 200, buttonColour, "Singleplayer", 75)            
    multiplayerBtn = button(450, 300, buttonColour, "Multiplayer", 81)
    playerStatsBtn = button(450, 400, buttonColour, "Player stats", 78)
    controlsBtn = button(450, 500, buttonColour, "Controls", 100)
    tutorialBtn = button(450, 600, buttonColour, "Tutorial", 105)
        
    #Displays all the buttons on screen
    singleplayerBtn.buttonDraw(screen)
    multiplayerBtn.buttonDraw(screen)
    playerStatsBtn.buttonDraw(screen)
    controlsBtn.buttonDraw(screen)
    tutorialBtn.buttonDraw(screen)
        
    #Checks if buttons have been clicked -> If clicked, progresses to respective display
    if singleplayerBtn.buttonClicked ():
        pressed = True
        selectDifficulty (screen,pressed)       
        return pressed

    if multiplayerBtn.buttonClicked ():
        print ("multiplayer Clicked")
            
    if playerStatsBtn.buttonClicked ():
        pressed = True
        playerStatsMain (screen,pressed)

    if controlsBtn.buttonClicked ():                    
        pressed = True
        controls (screen, pressed)              

    if tutorialBtn.buttonClicked ():
        pressed = True
        tutorial (screen, pressed)              

    


##---Main menu loop---##
def menu (screen):
    run = True
    while run:

        #Checking to see if the user closed the window 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                  
                run = False

        #Creating the UI
        drawDisplay (screen)                           
        displayMenuText (screen)                              
        displayButtons (screen)                               
       
        pygame.display.flip()                           

    pygame.quit()            
    sys.exit ()




