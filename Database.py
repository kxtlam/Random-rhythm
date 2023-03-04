
import sqlite3
import hashlib
from datetime import datetime


#Creating a hash
def createHash (password):
    hashedPassword = hashlib.sha256(str.encode(password)).hexdigest ()          
    return hashedPassword
#^Hashes password using sha256 
#str.encode(password) turns the string password into byte form in order for it to work
#When hashed, it becomes an hashed object so to get the data out of that object to make it a string, you do .hexdigest ()


#Creating the user table and inserting login values into it
def createUserDatabase ():
    conn = sqlite3.connect ('UserData.db')                 
    c = conn.cursor ()

    #Creating the table 'users' and stating attributes
    c.execute ("""CREATE TABLE IF NOT EXISTS users
    (
        userID text primary key, 
        username text, 
        password_hash text, 
        numGamesPlayed int, 
        highestScore int,
        highestComboEver int
                            )
    """)

    #Creating the table scores          #Uses foreign key userID to link users and scores table
    c.execute ("""CREATE TABLE IF NOT EXISTS scores
    (
        gameID int primary key,
        difficulty text,
        score int,
        dateTime text,
        userID int,
        FOREIGN KEY (userID) REFERENCES UserData (users)        
                                                        )       
    """)               


    #Creating user logins
    userLogins = [ ("a", "User1", createHash("Easypassword"), 0, 0, 0),
                   ("b", "User2", createHash("An0therPswd1"), 0, 0, 0),
                   ("c", "User3", createHash("comppwd253"), 0, 0, 0),
                   ("d", "User4", createHash("asjd29dnskdw"), 0, 0, 0),
                   ("e", "User5", createHash("hhhhhhh222"), 0, 0, 0) ]      
    c.executemany ("INSERT or IGNORE INTO users VALUES (?,?,?,?,?,?)", userLogins)     #Inserts user logins into table users

    #Setting users with random initial score starting time
    time = datetime.strptime("20/03/2022 17:37:52.22", "%d/%m/%Y %H:%M:%S.%f")        
    time1 = datetime.strptime("20/03/2022 17:37:53.22", "%d/%m/%Y %H:%M:%S.%f")       
    time2 = datetime.strptime("20/03/2022 17:37:54.22", "%d/%m/%Y %H:%M:%S.%f")      
    time3 = datetime.strptime("20/03/2022 17:37:55.22", "%d/%m/%Y %H:%M:%S.%f")       
    time4 = datetime.strptime("20/03/2022 17:37:56.22", "%d/%m/%Y %H:%M:%S.%f")       

    #Creating user starting history- all players start with an initial score of 0
    history = [(0, "normal", 0, time, "a"),
               (1, "normal", 0, time1, "b"),
               (2, "normal", 0, time2, "c"),
               (3, "normal", 0, time3, "d"),
               (4, "normal", 0, time4, "e"),]
            
               
    c.executemany ("INSERT or IGNORE INTO scores VALUES (?,?,?,?,?)", history)         

    conn.commit ()      
    conn.close ()      


def searchDatabase (userInputUN, userInputPW,screen):
    from Menu import menu

    #Connecting and opening the database
    conn = sqlite3.connect ('UserData.db')          
    c = conn.cursor ()  

    #Searching database to see if the username has a password in the database
    c.execute ("SELECT password_hash FROM users WHERE username = ?", (userInputUN,))       
    passwordFound = c.fetchone ()                                                   
    passwordFound = str(passwordFound)                                             

    #Checks if the password found in the database = user inputted password
    if passwordFound [2:len(passwordFound)-3] == createHash(userInputPW):      
        global username                                                         #Making variable username global so that it can be accessed in the gameover module
        username = userInputUN
        menu (screen)                                                           
    #If password was incorrect, returns to where the function was called

    conn.close ()   
       

def storeGameHistory (difficulty, score, dateTime, username):    
    conn=sqlite3.connect ('UserData.db')
    c=conn.cursor ()

    #Fetching userID according to username
    c.execute ("SELECT userID FROM users WHERE username = ?", (username,))
    userID = str(c.fetchone ())
    userID = userID [2]

    #Fetching the last gameID in the table so that it can be incremented by 1 to produce a unique primary key
    c.execute ("SELECT gameID FROM scores ORDER BY dateTime DESC LIMIT 1")     
    gameCountID =  str(c.fetchone ())
    gameCountID = int(gameCountID [1])
    gameCountID += 1                                
    
    #Inserting the new record data into the table
    c.execute ("INSERT INTO scores (gameID, difficulty, score, datetime, userID) VALUES (?,?,?,?,?)",(gameCountID, difficulty, score, dateTime, userID))

    conn.commit ()
    conn.close ()     



def storeGameStats (score,combo, username):      
    conn = sqlite3.connect ('UserData.db')
    c=conn.cursor ()


    #Fetching numGamesPlayed from database 
    c.execute ("SELECT numGamesPlayed FROM users WHERE username = ?", (username,))       
    numGamesPlayed = str(c.fetchone ())                                                
    numGamesPlayed = numGamesPlayed [1:len(numGamesPlayed) - 2]                          #Slices the string to extract just the number of games played 

    #Updating database with new numGamesPlayed (incrementing it by 1)
    numGamesPlayed = int(numGamesPlayed) + 1
    c.execute ("UPDATE users SET numGamesPlayed = ? WHERE username = ?",(numGamesPlayed,username))


    #Fetching highestComboEver from database
    c.execute ("SELECT highestComboEver FROM users WHERE username = ?", (username,))   
    highestComboEver = str(c.fetchone ())                                               
    highestComboEver = highestComboEver [1:len(highestComboEver) - 2]                   #Slices the string to extract just the combo number

    #Updating database with new highestCombo if combo > highestComboEver    
    if combo > int(highestComboEver):                                                                          
        c.execute ("UPDATE users SET highestComboEver = REPLACE (highestComboEver,?,?) WHERE username = ?",(highestComboEver,combo,username))   



    #Fetching highscore from database
    c.execute ("SELECT highestScore FROM users WHERE username = ?", (username,))       
    highestScore = str(c.fetchone ())                                                   
    highestScore = highestScore [1:len(highestScore) - 2]                              #Slices the string to extract just the score number

    conn.commit ()      

    #Updating database with new highscore if current score > highestScore
    if score > int(highestScore):                                                                       
        c.execute ("UPDATE users SET highestScore = REPLACE (highestScore,?,?) WHERE username = ?",(highestScore,score,username))   

        conn.commit ()         
        conn.close ()         
        display = True
        return display          #Will result in 'new high score!' being displayed in the gameover screen



    
createUserDatabase ()

#Prints what is currently stored in the database in termial
conn = sqlite3.connect ('UserData.db')                 
c = conn.cursor ()

print ("USERS")
for row in c.execute ("SELECT * FROM users"):
    print (row)

print ("SCORES")
for row in c.execute ("SELECT * FROM scores"):
    print (row)

conn.close ()




