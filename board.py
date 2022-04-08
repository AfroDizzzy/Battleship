import math
import random
 
class board:
    def __init__(self, xSize, ySize):
        self.x = xSize
        self.y = ySize
        self.firstEnemyPosition = []
        self.secondEnemyPosition = []
        self.grid = [[0 for j in range(xSize)] for i in range(ySize)] #creates a grid filled with zeros based on the x and y size inputed 

    def getGrid(self):
        return self.grid
    
    def getFirstShipPosition(self):
        return self.firstEnemyPosition

    def getSecondShipPosition(self):
        return self.secondEnemyPosition



    #will also set position of enemy to null
    def setGridPos(self, firstIndex, secondIndex, value):
        self.getGrid()[firstIndex][secondIndex] = value

        #checks if the first ship exists, and then if the ship exists remove it from the board
        if self.firstEnemyPosition:
            if (firstIndex == self.firstEnemyPosition[0]) & (secondIndex == self.firstEnemyPosition[1]):
                self.firstEnemyPosition = []
        if self.secondEnemyPosition:
            if (firstIndex == self.secondEnemyPosition[0]) & (secondIndex == self.secondEnemyPosition[1]):
                self.secondEnemyPosition = []



    #places enemy ships within the grid
    def initialiseEnemyShips(self):
        firstShipInt = random.randint(0, (self.x * self.y)-1) #gets a random number between 0 and the total number of cells in the grid
        self.shipDeployment(firstShipInt, 1)

        secondShipInt = random.randint(0, (self.x * self.y)-1)
        self.shipDeployment(secondShipInt, 2)



    #calculates the a free position on the board and places a ship there
    def shipDeployment(self, proposedShipPosition, shipNumber):
        firstArrayPosition = 0
        secondArrayPosition = proposedShipPosition % self.x

        #Make sure the first position of the array is divisor is too small
        if ((math.floor(proposedShipPosition / self.x)) < 1):
            firstArrayPosition = 0;
        else:
            firstArrayPosition = math.floor(proposedShipPosition / self.x)

        #check to not put 2 ships on same position, performs recersion of position clash with a new random number
        if (self.grid[firstArrayPosition][secondArrayPosition] == 1):
            self.shipDeployment(random.randint(0, self.x * self.y))
        else:
            self.grid[firstArrayPosition][secondArrayPosition] = 1

            #stores the ships positions are coordinates
            if shipNumber == 1:
                self.firstEnemyPosition.append(firstArrayPosition)
                self.firstEnemyPosition.append(secondArrayPosition)
            else:
                self.secondEnemyPosition.append(firstArrayPosition)
                self.secondEnemyPosition.append(secondArrayPosition)
          
          
           
    # function to display the battlefield grid on the console
    def cheaterDisplay(self, gridInput):
        print('\n'.join(' '.join(str(value) for value in row) for row in gridInput) + '\n')

    def display(self, gridInput):
        stringToPrint = '\n'

        for row in gridInput:
            for value in row:
                if value == 1:
                    stringToPrint += ' 0'
                else:
                    stringToPrint += ' ' + str(value)
            stringToPrint += '\n'

        print(stringToPrint)
   
        