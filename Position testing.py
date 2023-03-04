#Importing and intialising the pygame library
import pygame
import sys
from blockClass import Block 
pygame.init()    

#Creating the display#
screen = pygame.display.set_mode([1200,800], pygame.RESIZABLE)                
pygame.display.set_caption ("Random Rhythm")       

def displayBackground (screen):
    hardBg = pygame.image.load ("Images\Bg 6 lanes.png")
    hardBg = pygame.transform.scale (hardBg, (1200,800))
    screen.blit (hardBg, (0,0))

    return screen

#Main game loop#
def playGameH (screen, pressed):             

    while pressed:                                

    #Checking to see if players closed window 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                   
                pressed = False            
                pygame.quit ()
                sys.exit ()

        displayBackground (screen)      

        blockImage = pygame.image.load ("Images\Pink block.png")         #if lane = 1 or 4, the pink block image is loaded and scaled
        blockImage = pygame.transform.scale (blockImage, (167,27))   
        new = Block (blockImage, 250,690)
        new.drawBlock (screen)

        
        pygame.display.flip ()
        pos = pygame.mouse.get_pos()  
        print (pos)


pressed = True
playGameH (screen, pressed)