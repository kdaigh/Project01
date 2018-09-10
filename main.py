##import math
##import random
##from boardFunctions import BoardFunctions

##print ("Welcome to Minesweeper!")
##print ("Please, chose from the menu:")

##theBoard=BoardFunctions()

##rows = input("How many rows?")
##cols = input("How many cols?")

##theBoard.makeGrid(rows, cols)

from boardFunctions import BoardFunctions

if __name__ == "__main__":
    myGame = BoardFunctions()
    myGame.game_menu()
    size = myGame.boardSize
    mines = myGame.mines_num
    grid = myGame.makeGrid(size, size)
    myGame.justPrint(size, size, grid)
