import pygame
import sys
from Background import drawDisplay
from Database import searchDatabase
pygame.init ()


#Creating the display#
screen = pygame.display.set_mode([1200,800], pygame.RESIZABLE)                
pygame.display.set_caption ("Random Rhythm")                #Sets the game title for the window


#Displays all text: Login, username, password
def displayUI (screen):

    #Displaying the base starry background
    drawDisplay (screen)

    #Displaying the 'Random Rhythm' logo 
    logo = pygame.image.load ("Images\Random Rhythm logo.png")          
    screen.blit (logo, (520,50)) 

    #Displaying 'Login'
    font = pygame.font.SysFont ('Calibri', 60, False, False)   
    loginTitle = font.render ("Login", True, (255,255,255))    
    screen.blit (loginTitle, (70, 190))                         

    #Displaying 'Username'
    smallfont = pygame.font.SysFont ('Calibri',25,False,False)
    usernameText = smallfont.render ("Username", True, (255,255,255))
    screen.blit (usernameText, (65,280))

    #Displaying 'Password'
    passwordText = smallfont.render ("Password", True, (255,255,255))
    screen.blit (passwordText, (65,420))


#Carries out validation checks
def validationCheck (userInputUN, userInputPW, activeBTN): 
    errorFont =pygame.font.SysFont ('Calibri', 20, False, True)                 

    while activeBTN == True:          #While button has been pressed...

        #If the username or password entry box is empty, display "Invalid input" to avoid empty boxes
        if userInputUN == "" or userInputPW == "":                                                          
            displayUI (screen) 
            errorText = errorFont.render ("Invalid input - enter username and password", True, (255,0,0))
            screen.blit (errorText, (65,520))
            
        #If username entered isn't between 5 and 15 characters, display 'Invalid username or password'
        elif len(userInputUN) <= 4 or len(userInputUN) >= 16:
            displayUI (screen) 
            errorText = errorFont.render ("Invalid username or password", True, (255,0,0))
            screen.blit (errorText, (65,520))

        #If password entered isn't between 9 and 19 characters, display 'Invalid username or password'
        elif len(userInputPW) <= 8 or len(userInputPW) >= 20:
            displayUI (screen) 
            errorText = errorFont.render ("Invalid username or password", True, (255,0,0))
            screen.blit (errorText, (65,520))

        #If there are no errors...
        else:
            searchDatabase (userInputUN, userInputPW,screen) 

            #If the username and password wasn't found in the database:     
            displayUI (screen) 
            errorFont =pygame.font.SysFont ('Calibri', 20, False, True)
            errorText = errorFont.render ("Incorrect username and/or password", True, (255,0,0))
            screen.blit (errorText, (65,520))
                

        return screen


def login ():
    run = True
    userInputUN = ""        
    userInputPW = ""          
    activeUN = False
    activePW = False
    activeBTN = False
    displayUI (screen)       

    while run:

        for event in pygame.event.get():

            #Checking to see if players closed window
            if event.type == pygame.QUIT:                                 
                run = False                                  
            
            #Checking if users clicked on a rectangle
            if event.type == pygame.MOUSEBUTTONDOWN:                
                if usernameRect.collidepoint (event.pos):           
                    activeUN = True                                 
                    activePW = False

                elif passwordRect.collidepoint (event.pos):        
                    activePW = True                                 
                    activeUN = False

                elif loginBtn.collidepoint (event.pos):                    
                    activeBTN = True                                        
                    validationCheck (userInputUN, userInputPW,activeBTN)   
                
                else:                                               #if mouse click wasn't on any rectangle boxes, they're both set inactive 
                    activeUN = False
                    activePW = False

            #Storing what the user has typed into variable userInputUN/PW
            if event.type == pygame.KEYDOWN:                           
                if activeUN == True:
                    #Detects for use of backspaces (because it isn't unicode and isn't detected by the other line of code)
                    if event.key == pygame.K_BACKSPACE:                      
                        userInputUN = userInputUN [0:-1]                     

                    else:
                        if len(userInputUN) <= 19:                           
                            userInputUN += event.unicode                      

                if activePW == True:    
                    if event.key == pygame.K_BACKSPACE:               
                        userInputPW = userInputPW [0:-1]                     
                    else:
                        if len(userInputPW) <= 19:
                            userInputPW += event.unicode   
                    
        #Creating the username input box
        darkerGrey_notclicked = (180,180,180)
        lightGrey_clicked = (210,210,210)
        if activeUN == True:
            usernameRect = pygame.draw.rect (screen,lightGrey_clicked, (65,335,410,35)) 
        else:
            usernameRect = pygame.draw.rect (screen,darkerGrey_notclicked, (65,335,410,35)) 


        #Creating the password input box
        if activePW == True:
            passwordRect = pygame.draw.rect (screen,lightGrey_clicked, (65,475,410,35))
        else:
            passwordRect = pygame.draw.rect (screen,darkerGrey_notclicked, (65,475,410,35)) 


        #Displaying username user input (i.e. what the user has typed)                                                    
        inputFont = pygame.font.SysFont ('Calibri',25, False, False)            
        displayUserInputUN = inputFont.render (userInputUN, True, (0,0,0))
        screen.blit (displayUserInputUN, (usernameRect.x, usernameRect.y + 5))               


        #Displaying password user input (i.e. what the user has typed)
        displayUserInputPW = inputFont.render (userInputPW, True, (0,0,0))
        screen.blit (displayUserInputPW, (passwordRect.x, passwordRect.y +5))

        #Creating the login button
        loginBtn =pygame.draw.rect (screen,darkerGrey_notclicked, (388,554,85,27))
        loginFont = pygame.font.SysFont ('Calibri', 20, False, False)
        loginBtnText = loginFont.render ("Login", True, (0,0,0))
        screen.blit (loginBtnText, (loginBtn.x+22,loginBtn.y + 4))

        pygame.display.flip ()      

    pygame.quit ()
    sys.exit ()

login ()

