import pygame
import sys
from ButtonClass import button
pygame.init()

#Displays  tutorial page when 'tutorial' button in menu is pressed#
def tutorial (screen, pressed):

    while pressed:  #while pressed is true

        #Checking to see if players closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                pressed = False             
                pygame.quit ()
                sys.exit ()

        #Displaying the tutorial image onto screen
        tutorialImage = pygame.image.load ("Images\Tutorial page.png")                 
        tutorialImage = pygame.transform.scale (tutorialImage, (1200,800))      
        screen.blit (tutorialImage, (0,0))                                      

        #Displaying the back to menu arrow
        arrow = pygame.image.load ("Images\Menu arrow.png").convert_alpha ()            
        arrow = pygame.transform.scale (arrow, (80,50))                         
        backBtn = button (20, 20, arrow, "", 75)                                 
        backBtn.buttonDraw (screen)                                              
        
        #Checking if the back to menu arrow has been clicked
        if backBtn.buttonClicked ():
            pressed = False

        pygame.display.flip ()                                                  

    



