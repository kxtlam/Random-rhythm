
#User interface background#
def drawDisplay (screen):
    import pygame
    pygame.init()    

    #Setting the background
    bg = pygame.image.load ("Images\Starry background.png")            
    screen.blit (bg, (0,0))                                     

    return screen                            