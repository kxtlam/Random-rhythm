#Importing and intialising all libraries
import pygame
import sys
import random
from pygame.constants import K_c        
from pygame.constants import K_v
from pygame.constants import K_n
from pygame.constants import K_m
from blockClass import Block 
from Gameover import gameover
pygame.init()    
pygame.font.init()


#Displays 4 lane background
def displayBackground (screen):
    normalBg = pygame.image.load ("Images\Bg 4 lanes.png")              
    normalBg = pygame.transform.scale (normalBg, (1200,800))           
    screen.blit (normalBg, (0,0))                                       
    return screen

#Generating a random lane number
def generateRandLane ():
    lane = random.randint (1,4)                                 #Generates a random number between 1 and 4 (each one represents the lane number)
    if lane == 1:
        pos = (268,0)                                           #Then it sets the correct position and block image for the block that would belong in that lane

    elif lane == 2:
        pos = (436,0)

    elif lane == 3:
        pos = (604,0)

    elif lane == 4:
        pos = (773,0)                                                 
    
    return pos                              

#Loading and scaling the block image according to the lane (x position)
def getImage (x):
    if x == 268 or x == 773:
        blockImage = pygame.image.load ("Images\Pink block.png")         #if lane = 1 or 4, the pink block image is loaded and scaled
        blockImage = pygame.transform.scale (blockImage, (167,27))    
    
    elif x == 436 or x == 604:
        blockImage = pygame.image.load ("Images\Blue block.png")         #if lane = 2 or 3, the blue block image is loaded and scaled
        blockImage = pygame.transform.scale (blockImage, (167,27))

    return blockImage      
     


#Main game loop#
def playGameN (screen, pressed,score):               #Passes the arguments screen and pressed (to make sure button stays pressed)
    while pressed:                                  

        displayBackground (screen)                          
        pygame.display.flip ()                           
        font = pygame.font.Font ("Saira-Light.ttf", 34)     

        #Checking to see if players closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           
                pressed = False                 
                pygame.quit ()
                sys.exit ()                     


        #Generating the random positions for all the blocks and storing it into list allBlockPos
        allBlockPos = [ ]                           
        yCount = 0
        for i in range (350):                            
            pos = generateRandLane ()            #Generates a random lane and stores the coordinates in pos
            
            if 0 <= i <= 20:
                yCount = yCount - 250               #Takes away yCount from current block y pos 
            elif 20 < i <= 40:                      #This creates a distance between each block created
                yCount = yCount - 200               #The distance between blocks decreases for the later blocks
            elif 40 < i <= 60:
                yCount = yCount - 150
            elif 60 < i <= 70:
                yCount = yCount - 100
            elif 70 < i <= 350:
                yCount = yCount - 50

            x = pos [0]                           
            y = pos [1] + yCount                  
            tempList = [x, y]                      
            allBlockPos.append (tempList)          
            i += 1                            



        #----Drawing all blocks----#
        stepX = 0                               
        stepY = 0                               
        allBlocks = []                         
        for n in range (350):                        #Creates 350 blocks
            x = allBlockPos [stepX][0]              
            y = allBlockPos [stepY][1]         
            blockImg = getImage (x)                                  
            block = Block(blockImg, x, y)      
            allBlocks.append (block)            
            block.drawBlock (screen)             
            n +=1
            stepX += 1         
            stepY += 1
        pygame.display.flip ()

        #----Making all the blocks fall----#
        lives = 3
        score = 0
        combo = 0
        highestCombo = 0

        while allBlockPos [349][1] < 800:                #While the y coordinate of the last block is still on screen (i.e. until all blocks have fallen),
            while lives > 0:   

                displayBackground (screen)            #Resets the pygame surface so that the new block positions can be displayed

                #Makes all blocks y value increase by 10 (i.e fall by 10)
                for a in range (350):                
                    block = allBlocks [a]          
                    if  0 <= a <= 140:                              
                        if (20 < a <= 40) and (block.y >= -100):     
                            block.y = block.y + 15
                        elif (40 < a <= 60) and (block.y >= -100):     
                            block.y = block.y + 20
                        elif (60 < a <= 350) and (block.y >= -100):
                            block.y = block.y + 25
                        else:
                            block.y = block.y + 10        
                    block = Block (blockImg, x, y)          
                    block = allBlocks [a]                   
                    
                    a+= 1         
                    
                #Drawing all the blocks' new position onto the display
                for b in range (350):
                    block = allBlocks [b]                           
                    block = Block (block.image,block.x,block.y)    
                    block.drawBlock (screen)                        

                    #Detecting if the correct keyboard key was pressed    
                    if 660 <= block.y <= 685:                       #If the block has reached the bar at the bottom (i.e. between y=660 and y=690)
                        for event in pygame.event.get ():
                            keyPressed = pygame.key.get_pressed ()  
                            if event.type == pygame.KEYDOWN:        #If a key was pressed...
                        
                                if block.x == 268:                  #If the block is in the first lane
                                    if keyPressed [K_c]:            #Check if the c key has been pressed
                                        score = score + 1           
                                        combo = combo + 1           

                                    elif keyPressed != [K_c]:       #If a key other than c was pressed
                                        lives = lives - 1           #Lose a life
                                        if combo > highestCombo:    #If the current combo is higher than the highest combo reached this game
                                            highestCombo = combo    #Store combo has new highest combo

                                if block.x == 436:                  #Etc.  (repeat with other lanes but with different keys)
                                    if keyPressed [K_v]:
                                        score = score + 1
                                        combo = combo + 1

                                    elif keyPressed != [K_v]:
                                        lives = lives - 1
                                        if combo > highestCombo:
                                            highestCombo = combo 
                                        combo = 0 
                                                                    
                                if block.x == 604:
                                    if keyPressed [K_n]:
                                        score = score + 1
                                        combo = combo + 1

                                    elif keyPressed != [K_n]:
                                        lives = lives - 1
                                        if combo > highestCombo:
                                            highestCombo = combo 
                                        combo = 0

                                if block.x == 773:
                                    if keyPressed [K_m]:
                                        score = score + 1
                                        combo = combo + 1

                                    elif keyPressed != [K_m]:
                                        lives = lives - 1
                                        if combo > highestCombo:
                                            highestCombo = combo 
                                        combo = 0

                    b += 1                                                             
        
                #Replacing block image with transparent image when reaches the bar
                for d in range (350):                                                     
                    block = allBlocks [d]                                                   
                    if block.y > 690:                                                       
                        block.image = pygame.image.load ("Images\Transparent block.png")    
                        block = Block (block.image,block.x,block.y)                         
                        block.drawBlock (screen)                                            
                    d += 1                                                                  

                #Displaying lives UI
                if lives == 3:                                                              
                    lives3 = pygame.image.load ("Images\Lives three.png")                  
                    screen.blit (lives3, (-150,-190))                                       
                elif lives == 2:
                    lives2 = pygame.image.load ("Images\Lives two.png")                   
                    screen.blit (lives2, (-150,-190))
                elif lives == 1:
                    lives1 = pygame.image.load ("Images\Lives one.png")
                    screen.blit (lives1, (-150,-190))


                #Displaying scores
                displayScoreText = font.render ("Score:", True, (255,255,255))
                displayScore = font.render (str(score), True, (255,255,255))                     
                screen.blit (displayScore, (1100, 100))                                          
                screen.blit (displayScoreText, (990, 100))                                        

                #Displaying combos
                displayComboText = font.render ("Combo: ", True, (255,255,255))
                displayCombo = font.render (str(combo), True, (255,255,255))                     
                screen.blit (displayCombo, (1110, 200))                                           
                screen.blit (displayComboText, (980, 200))                                        

                pygame.display.flip ()                  


            #Displays zero lives with a mini delay before moving onto game over screen
            lives0 = pygame.image.load ("Images\Lives zero.png")
            screen.blit (lives0, (-150,-190))
            pygame.display.flip ()
            pygame.time.delay (2000)            #Adds a 2 second delay after losing all lives


            allBlockPos [349][1] = 900                   #Breaks the other while loop to end the game            
        
        pressed = False       

    #Creating a new whileloop for the game over screen
    displayGameOver = True
    difficulty = "normal"
    while displayGameOver == True:
        gameover (screen,score,highestCombo, displayGameOver, difficulty)                 
        displayGameOver = False
    
    pressed = False
    return pressed

       




 





       

        
        


 

              
