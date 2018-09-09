from menu import Menu
from boardFunctions import BoardFunctions


myGame = Menu()
myBoard = BoardFunctions()
myGame.game_menu()

size = myGame.board_size
mines = myGame.mines_num
myBoard.mines = mines
   
myBoard.makeGrid(size, size)
myBoard.printBoard(size, size)

# myGame.play_game()

