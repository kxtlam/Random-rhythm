import pygame
pygame.init()

class Block(pygame.sprite.Sprite):
    def __init__ (self,image,x, y):                
        pygame.sprite.Sprite.__init__(self)
        super ().__init__()
        self.x = x
        self.y = y
        self.image = image

    #Draws block onto pygame surface at position self.x, self.y
    def drawBlock (self, screen): 
        pos = (self.x, self.y)
        screen.blit (self.image, pos)     
        return screen


  




        
        
        
    


