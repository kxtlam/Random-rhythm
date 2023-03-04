import pygame
import sys
from Background import drawDisplay
from ButtonClass import button
from datetime import datetime
import Database
pygame.init()
pygame.font.init ()

def gameover (screen, score, highestCombo,displayGameOver,difficulty):
    while displayGameOver:
        #Checking to see if players closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                    
                pygame.quit ()
                sys.exit ()                    

        drawDisplay (screen)       

        #Displaying "Game Over"
        gameoverText = pygame.image.load ("Images\Gameover image.png")
        screen.blit (gameoverText, (0,0))

        #Displaying "Score:" and "Highest Combo:"
        gameoverText = pygame.image.load ("Images\gameover text.png")
        screen.blit (gameoverText, (0,0))

        font = pygame.font.Font ("Saira-Light.ttf", 90)     

        #Displaying score and highest combo number
        displayScore = font.render (str(score), True, (255,203,217))                      #Renders the font onto pygame surface with the score number in pink
        displayCombo = font.render (str(highestCombo), True, (137,207,240))               #Renders the font onto pygame surface with the combo number in blue
        screen.blit (displayScore, (710, 350))
        screen.blit (displayCombo, (850, 500))                                          


        #Making the button
        buttonColour = pygame.image.load ("Images\Button colour.png").convert_alpha ()     
        buttonColour = pygame.transform.scale (buttonColour, (200,50))              
        
        returnToMenuBtn = button (950,700,buttonColour,"Return to menu", 5)
        returnToMenuBtn.buttonDraw (screen)

        pygame.display.flip ()


        #Calling storeGameHistory function- stores the data from the current game
        currentDateTime = datetime.now ()                                                #Gets the current time in yyyy-mm-dd h:m:s form
        Database.storeGameHistory (difficulty,score,currentDateTime,Database.username)    
        

        #Calling storeGameStats function- stores score and/or combo if they are the user's highest ever score/combo yet
        display = Database.storeGameStats (score, highestCombo, Database.username)                             
        

        ##Runs if score achieved is a new high score##
        while display == True:

            #Users can still close the window if needed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                    
                    pygame.quit ()
                    sys.exit ()                   

            #Displaying 'new high score' on the game over screen 
            newHighScoreImg = pygame.image.load ("Images\\New high score image.png")     
            screen.blit (newHighScoreImg, (0,0))                                       
            if returnToMenuBtn.buttonClicked ():
                displayGameOver = False
                break
            pygame.display.flip ()                             


        ##Runs if score achieved is not a new high score##
        notNewHS = True
        while notNewHS:
            #Users can still close the window if needed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                     
                    pygame.quit ()
                    sys.exit ()                  

            #If return to menu button is cilcked, the while loop ends and it returns to the menu screen
            if returnToMenuBtn.buttonClicked ():       
                displayGameOver = False 
                break                

    return displayGameOver
    

