import pygame
pygame.init()                           
pygame.font.init()  

#Button class#
class button ():

    #Initialising all button attributes
    def __init__(self, x, y, image, text, extraSpace):  

        self.image = image
        self.width = image.get_width ()
        self.height = image.get_height ()
        self.x = x    
        self.y = y      
        self.text = text
        self.extraSpace = extraSpace


    #Draws the button on screen 
    def buttonDraw (self, screen):

        font = pygame.font.Font ("Saira-Light.ttf", 26)                          
        buttonText = font.render (self.text, True, (0,0,0))                      
        screen.blit (self.image, (self.x, self.y))                               
        screen.blit (buttonText, (self.x + self.extraSpace, self.y+4))           


    #Checks to see if the button has been clicked 
    def buttonClicked (self):
        
        progress = False   
        pos = pygame.mouse.get_pos()                                            
        buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)       

        if buttonRect.collidepoint (pos):                                       #If mouse position matches button position
            if pygame.mouse.get_pressed()[0] == 1:                             
                progress = True

        return progress     #If progress = true, it will trigger the condition in the menu module

    
  


