import pygame
import sys
from Background import drawDisplay
from ButtonClass import button
from PlayGameNormal import playGameN    #test ver
from PlayGameHard import playGameH
from PlayGameExtreme import playGameE
pygame.init() 
pygame.font.init() 


#Displays the title 'Select Difficulty'#
def displaySelectDifficulty(screen):
    font = pygame.font.SysFont ('Calibri', 60, False, False)               
    selectDiffTitle = font.render ("Select difficulty", True, (255, 255, 255))    
    screen.blit (selectDiffTitle, (415, 100))                                    
    return screen


#Displays the back to menu button#
def backToMenu (screen,pressed):
    #Displaying the back to menu arrow
    arrow = pygame.image.load ("Images\Menu arrow.png").convert_alpha ()       
    arrow = pygame.transform.scale (arrow, (80,50))                             
    backBtn = button (20, 20, arrow, "", 75)                                    
    backBtn.buttonDraw (screen)                                                 

    #Checking if the back to menu arrow has been clicked
    if backBtn.buttonClicked ():                
        pressed = False                                         #If button clicked, pressed = False and returns to menu screen
    return pressed


#Displays the normal, hard and extreme buttons#
def displayButtons (screen):
    buttonColour = pygame.image.load ("Images\Button colour.png").convert_alpha ()     
    buttonColour = pygame.transform.scale (buttonColour, (300,50))                      

    #Creating instances of the class button
    normalDiffBtn = button (450,250,buttonColour,"Normal: 4 lanes",55)                
    hardDiffBtn = button (450,375,buttonColour,"Hard: 5 lanes",70)
    extremeDiffBtn = button (450,500,buttonColour,"Extreme: 6 lanes",50)

    #Draws the buttons onto the pygame screen
    normalDiffBtn.buttonDraw (screen)       
    hardDiffBtn.buttonDraw (screen)
    extremeDiffBtn.buttonDraw (screen)

    #Checks to see if the buttons have been clicked 
    if normalDiffBtn.buttonClicked ():                           
        pressed = True                                                                            
        playGameN (screen, pressed, 0) 
        pressed = False
        return pressed

    if hardDiffBtn.buttonClicked ():
        pressed = True
        playGameH (screen, pressed, 0)
        pressed = False
        return pressed

    if extremeDiffBtn.buttonClicked ():
        pressed = True
        playGameE (screen, pressed, 0)
        pressed = False
        return pressed




#Main Select Difficulty loop#
def selectDifficulty (screen,pressed):
    
    while pressed:  
        pressed1 = True
        while pressed1:
            #Checking to see if players closed window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:           
                    pressed = False             
                    pygame.quit ()
                    sys.exit ()
            
            drawDisplay (screen)
            pressed1 = displayButtons (screen)          #Returns to menu if false is returned from displayButtons
        
            displaySelectDifficulty (screen)
            pressed = backToMenu (screen, pressed)      #Returns to menu if false is returned from backToMenu
            
            pygame.display.flip()                       
        
        if pressed1 == False:
            pressed = False     #Makes it so that the while loop ends even if only pressed1 is false so returns to the menu

    return pressed

