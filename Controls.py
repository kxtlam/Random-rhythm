import pygame
import sys
from ButtonClass import button
pygame.init()

#Displays controls page when 'controls' button in menu is pressed#
def controls (screen, pressed):

    while pressed:  

        #Checking to see if players closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #when the x button on the window is clicked                
                pressed = False             #pressed is set to false, so the while loop ends
                pygame.quit ()
                sys.exit ()

        #Displaying the controls image onto screen
        controlsImage = pygame.image.load ("Images\Controls page.png")                  
        controlsImage = pygame.transform.scale (controlsImage, (1200,800))      
        screen.blit (controlsImage, (0,0))                                       

        #Displaying the back to menu arrow
        arrow = pygame.image.load ("Images\Menu arrow.png").convert_alpha ()            
        arrow = pygame.transform.scale (arrow, (80,50))                         
        backBtn = button (20, 20, arrow, "", 75)                                
        backBtn.buttonDraw (screen)                                             
        
        #Checking if the back to menu arrow has been clicked
        if backBtn.buttonClicked ():
            pressed = False                                 

        pygame.display.flip ()                                                   
