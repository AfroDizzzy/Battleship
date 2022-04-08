from asyncio.windows_events import NULL
import sys
import re
import subprocess, platform
from board import *


#setting up game board
boardWidth = 8
boardHeight = 8
boardCellTotal = boardWidth * boardHeight
gameBoard = board(boardWidth, boardHeight)

#function that runs the game. Is run automatically on startup of this class. 
def gameLoop():
    hitCount = 0
    guessCount = 0

    print("ENEMY SHIPS DETECTED CAPTAIN, ARMING MAIN 120MM GUNS!")
    gameBoard.initialiseEnemyShips()

    #loop to run the game.
    #Game will end when guessCount > 20
    while True:

        #display current game state
        #Change to gameBoard.display(gameBoard.getGrid()) to play without enemy ships positions
        gameBoard.display(gameBoard.getGrid())

        #prints standard string to describe game state and get target input
        print('Please enter target coordinates commander.' +
            '\nWE ONLY HAVE ' + str(20 - guessCount) + ' SHELLS LEFT' +
            '\nOur gunners will only first on coordinates 0 to ' + str(boardCellTotal))
        val = input("\nInput : ")
        wasAFloat = False

        #janky way of checking if input was a decimal number
        try: 
            test = int(val)
        except:
            print("HOLD UP BUDDY, you've input something a decimal number.")
            wasAFloat = True


        #the regex will filter out all characters which are not numbers, including negatives and decimals
        regexNumber = re.compile(r'\d+')
        if regexNumber.match(val) and not wasAFloat:
            hitCount = hitCount + checkIfHit(int(val), boardWidth) 
        else:
            tryAgain = input("Commander, our systems can only take in positive whole numbers, please try again: ")
            if regexNumber.match(tryAgain) == None:
                print("....Your inputs were incorrect and the mistakes allowed the enemy ships to fire upon us!....")
                print("..................... GAME OVER DUDE .....................")
                sys.exit()
            else:
                hitCount = hitCount + checkIfHit(int(tryAgain), boardWidth)

        checkIfOver(hitCount)
        guessCount += 1
        checkGuessesleft(guessCount)

        #FOR A FUTURE UPDATE. INTENDED TO WIPE THE TERMINAL AFTER EACH HIT CYCLE. Currently wipes terminal of hit hot/cold distance output. 
        # if platform.system()=="Windows":
        #     subprocess.Popen("cls", shell=True).communicate() #I like to use this instead of subprocess.call since for multi-word commands you can just type it out, granted this is just cls and subprocess.call should work fine 
        # else: #Linux and Mac
        #     print("\033c", end="")



#checks if the number of guesses exceeds 20 and display an endgame text
endGameString = ("You're fresh out of guesses mate! The enemy ships landed direct hits on the ships of your fleet. \n" +
        "With your fleet destroyed, Hitler's Navy rampaged the Atlantic, leading to Hitler finding the lost city of Atlantis. \n" + 
        "True story.")
def checkGuessesleft(currentGuessNumber):
    if currentGuessNumber >= 20:
        print(endGameString)
        sys.exit()



#checks if the input target is a ship or not
def checkIfHit(target, boardX):
    firstArrayPosition = 0

    #sets which y values of a given array the target is on
    secondArrayPosition = target % boardX
    hitMarker = "x"

    #easy way to make sure the target is on the board
    if target > boardCellTotal:
        print("TARGET WAS OUT OF BOUNDS SIR!\n")
        return 0

    #sets which x axis array the target is on
    if (target / boardX) < 1:
        firstArrayPosition = 0
    else: 
        firstArrayPosition = math.floor(target / boardX)
    
    #sets target position on grid is the desired hitmarker
    if gameBoard.getGrid()[firstArrayPosition][secondArrayPosition] == 1:
        gameBoard.setGridPos(firstArrayPosition, secondArrayPosition, hitMarker)
        print("\n\n\n\n\nShip hit sir!")
        return 1
    else:
        gameBoard.setGridPos(firstArrayPosition, secondArrayPosition, hitMarker)
        print("\n\n\n\n\nNO HIT!")
        #reports if the target was close or not
        distance = hotOrCold(firstArrayPosition, secondArrayPosition, gameBoard.getFirstShipPosition(), gameBoard.getSecondShipPosition())
        print(distance)
        return 0



#Initialise endgame sequence
def checkIfOver(hits):
    if hits >= 2:
        print("---------------- Game over, Commander! WE GOT EM! ----------------")
        sys.exit()



#hot/cold checker
def hotOrCold(targetY, targetX, ship1Position, ship2Position):
    distanceToFirstShip = 0
    distanceToSecondShip = 0

    closestShip = 0

    try:
        if ship1Position:
            distanceToFirstShip = abs(targetX - ship1Position[1]) + abs(targetY - ship1Position[0])
        if ship2Position:
            distanceToSecondShip = abs(targetX - ship2Position[1]) + abs(targetY - ship2Position[0])
        
        #if the distance is distance is 0 for eithership, ignore that value because it means the ship doesnt exist anymore
        #we only want to consider ships still left on the board for the hot/cold calculator
        if distanceToFirstShip != 0 & distanceToSecondShip != 0:
            closestShip = min(distanceToFirstShip, distanceToSecondShip)
        elif distanceToFirstShip != 0:
            closestShip = distanceToFirstShip
        else:
            closestShip = distanceToSecondShip
    except:
        print("error when calculating hot or cold")
        
    match closestShip:
        case 1:
            return "SHOT WAS VERY CLOSE: HOT"
        case 2:
            return "SHOT WAS VERY CLOSE: HOT"
        case 3:
            return "SHOT WAS KINDA CLOSE: WARM"
        case 4:
            return "SHOT WAS KINDA CLOSE: WARM"
        case _: 
            return "SHOT WAS WAY OFF COURSE: COLD"



#initialises the game when this file is ran
if __name__ == '__main__':
    gameLoop()