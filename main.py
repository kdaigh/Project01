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
    size = myGame.board_size
    mines = myGame.mines_num
    grid = myGame.make_grid(size, size)

    myGame.just_print(size, size, grid)
