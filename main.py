import math
import random
def generateBoard (size, mines):
    board = []
    for i in range (size):
        for j in range (size):
            board = random.randint (0,2)
        board = random.randint (0,2)
    print ("board has been generated")
    return board
		    
def printBoard(board):
    print (board)
    print ("printed")
	

print ("Welcome to Minesweeper!")
print ("Please, chose from the menu:")
while True:    
    print("""1. Play the Game
2. Quit""")
    choice = int (input(": "))    
    if choice == 1 :
        print ("Please Enter the board size, it should be at least 2, and maximum 15")
        boardSize = int (input(": "))
        print ("Awsome! Let the fun begin!")
        minMines = 1
        maxMines = (boardSize)**2 - 1
        print ("Enter the number of mines, it should be between 1 and " + str (maxMines))
        minesNum = int (input ())
        
        gameBoard = []
        gameBoard = generateBoard (boardSize, minesNum)		
        printBoard (gameBoard)
        print ("I am here")
    
    else:
	    break
