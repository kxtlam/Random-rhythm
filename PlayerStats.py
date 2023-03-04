import pygame
import sys
import sqlite3
import Database
from datetime import *
from ButtonClass import button
from Background import drawDisplay


#Displays the back to menu button#
def backToMenu (screen,pressed):
    #Displaying the back to menu arrow
    arrow = pygame.image.load ("Images\Menu arrow.png").convert_alpha ()       
    arrow = pygame.transform.scale (arrow, (80,50))                             
    backBtn = button (20, 20, arrow, "", 75)                                    
    backBtn.buttonDraw (screen)                                                 

    #Checking if the back to menu arrow has been clicked
    if backBtn.buttonClicked ():                
        pressed = False                                       
    return pressed

#Fetches top 5 scores from database for parameter difficulty#
def getTopScores (difficulty, userID,screen):
    conn = sqlite3.connect ('UserData.db')                  
    c = conn.cursor ()
    font = pygame.font.SysFont ('Consolas', 30, False, False)  

    #Fetches top 5 scores in the form of one long string
    c.execute ("SELECT score FROM scores WHERE userID = ? AND difficulty = ? ORDER BY score DESC LIMIT 5", (userID, difficulty))
    scoreList = str(c.fetchall ())
    topScores = []
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    n = 0
    
    #Extracts the numbers from the string and stores into a new list
    while n < len(scoreList):                   #While loop to extract all the numbers in the string list retrieved from the database and store into a new integer list                                              
        currentNum = scoreList [n]                                      
        if currentNum in numbers:                                       #If currentNum is a number (i.e. is within 0-9)...

            if scoreList [n+1] in numbers:                              #Check if the character in string scoreList after that is also a digit (to see if it is a single digit or double digit number)
                currentNum = currentNum + scoreList [n+1]               #Concatenate the two characters together 
                n += 1                                                  #Adds an extra 1 to n so that it doesn't append the second digit of the number a second time

                if scoreList [n+2] in numbers:                          #Check if it is a three digit number
                    currentNum = currentNum + scoreList [n+2]       #Currently set at 3 digits max because that is how big the max number of blocks spawned is
                    n += 1                                          #Adds another extra 1 to n to not append the third digit of the number again

            topScores.append (int(currentNum))               #Converts the string number into an integer and stores it to the new list 
        n += 1      #Increments n to move onto the next character in the string

    #Setting the correct column the number should to in (depends on difficulty)
    if difficulty == "normal":
        x = 116
    elif difficulty == "hard":
        x = 281
    elif difficulty == "extreme":
        x = 444
    
    if len (topScores) != 0:         #If the list isn't empty...
        score1 = font.render (str(topScores [0]), True, (163,217,243))                 
        screen.blit (score1, (x,439))

        if len (topScores) > 1:                                                                                                         
            score2 = font.render (str(topScores [1]), True, (163,217,243))            
            screen.blit (score2, (x,497))

            if len (topScores) > 2:                                                    
                score3 = font.render (str(topScores [2]), True, (163,217,243))                 
                screen.blit (score3, (x,556))

                if len (topScores) > 3:                                                
                    score4 = font.render (str(topScores [3]), True, (163,217,243))      
                    screen.blit (score4, (x,616))

                    if len (topScores) == 5:                                            
                        score5 = font.render (str(topScores [4]), True, (163,217,243))  
                        screen.blit (score5, (x,675))

    return screen


def displayStats (screen):
    conn = sqlite3.connect ('UserData.db')                  
    c = conn.cursor ()
    username = Database.username

    #Displaying username#
    font = pygame.font.SysFont ('Consolas', 30, False, False)              
    usernameText = font.render (username, True, (163,217,243))     
    screen.blit (usernameText, (205, 225))                                 

    #Displaying Number of games played#
    c.execute ("SELECT numGamesPlayed FROM users WHERE username = ?", (username,))
    fetchedNumGames = c.fetchone () 
    fetchedNumGames = str(fetchedNumGames) [1]
    numGames = font.render (fetchedNumGames, True, (163,217,243))     
    screen.blit (numGames, (395, 288))                                  

    #Fetching userID according to username#
    c.execute ("SELECT userID FROM users WHERE username = ?", (username,))
    userID = str(c.fetchone ())
    userID = userID [2]

    #Displaying top five scores for each difficulty#
    getTopScores ("normal", userID, screen)
    getTopScores ("hard", userID, screen)
    getTopScores ("extreme", userID, screen)

    #Displaying highest combo#
    c.execute ("SELECT highestComboEver FROM users WHERE username = ?", (username,))
    fetchedCombo = str(c.fetchone ()) [1]
    fetchedComboDis = font.render (fetchedCombo, True, (163,217,243))
    screen.blit (fetchedComboDis, (286,730))

    return screen
    


def getAllScoresDates (difficulty,userID):
    conn = sqlite3.connect ('UserData.db')                 
    c = conn.cursor ()

    ####Getting all scores####
    #Fetching all scores in database from difficulty and storing it in new list allScores
    c.execute ("SELECT score FROM scores WHERE userID = ? AND difficulty = ? ORDER BY dateTime ASC", (userID, difficulty))
    scoreList = c.fetchall()
    allScores = []
    for row in scoreList:
        currentScore = int(row[0])
        allScores.append (currentScore)

    y = allScores

    ####Getting all datetimes####
    c.execute ("SELECT * FROM scores WHERE userID = ? AND difficulty = ? ORDER BY dateTime ASC", (userID, difficulty))
    fetchedDateTimes = c.fetchall()
    allDateTimes = []

    for row in fetchedDateTimes:
        currentDT = str(row [3])
        allDateTimes.append (currentDT)

    x = [datetime.strptime(d,'%Y-%m-%d %H:%M:%S.%f')for d in allDateTimes]

    return x,y


def displayScoresGraph ():
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    conn = sqlite3.connect ('UserData.db')                
    c = conn.cursor ()

    #Fetching userID according to username#
    c.execute ("SELECT userID FROM users WHERE username = ?", (Database.username,))
    userID = str(c.fetchone ())
    userID = userID [2]

    #Labelling the graph axes#
    plt.xlabel ("Date")                
    plt.ylabel ("Score")                

    #Formats the x-axis labels so that they are more visible
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()   

    #Fetching all normal scores and dates#
    plotN = getAllScoresDates ("normal", userID)
    xN = plotN [0]
    yN = plotN [1]
    
    plotH = getAllScoresDates ("hard", userID)
    xH = plotH [0]
    yH = plotH [1]

    plotE = getAllScoresDates ("extreme", userID)
    xE = plotE [0]
    yE = plotE [1]

    plt.plot (xN,yN, color = "b", label = "Normal")
    plt.plot (xH,yH, color = "g", label = "Hard")
    plt.plot (xE,yE, color = "r", label = "Extreme")

    plt.legend ()  #Makes a key to identify which colour belongs to which graph

    plt.show ()    #Displays the graph

    


def playerStatsMain (screen,pressed):
    while pressed:

        #Checking to see if the user closed the window 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                   
                pressed = False
                pygame.quit ()
                sys.exit ()

        drawDisplay (screen)

        #Displaying "Game Over"
        gameoverText = pygame.image.load ("Images\Player Stats title.png")
        screen.blit (gameoverText, (0,0))

        #Displaying back to menu arrow
        pressed = backToMenu (screen, pressed)
        
        #Displaying all user stats#
        displayStats (screen)

        #Displaying graph button
        buttonColour = pygame.image.load ("Images\Button colour.png")       
        buttonColour = pygame.transform.scale (buttonColour, (250,50))      
        graphBtn = button(769, 519, buttonColour, "View graphs", 50)
        graphBtn.buttonDraw(screen)

        if graphBtn.buttonClicked ():
            displayScoresGraph ()
        

        pygame.display.flip ()


       
        

