from menu import Menu
from boardFunctions import BoardFunctions


myGame = Menu()
myGame.game_menu()

myBoard = BoardFunctions()

size = myGame.board_size
mines = myGame.mines_num

myBoard.mines = mines
   
myBoard.makeGrid(size, size)
myBoard.printBoard(size, size)

# myGame.play_game()
