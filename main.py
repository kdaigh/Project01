import math
print ("Welcome to Minesweeper!")
print ("Please, chose from the menu:")
while True:
    print("""1. Play the Game
             2. Quit""")
    choice = input(": ")
    if choice == 1 :
        print ("Please Enter the board size, it should be at least 2")
        boardSize = input(": ")
        print("Awsome!")
        minMines = 1
        minesMax = sqrt (boardSize) - 1
    else:
        break
