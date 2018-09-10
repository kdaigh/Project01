from menu import Menu
from boardFunctions import BoardFunctions


myGame = Menu()
myGame.game_menu()

myBoard = BoardFunctions()

size = myGame.board_size
mines = myGame.mines_num

myBoard.mines_num = mines

grid = myBoard.make_grid(size, size)
myBoard.generate_mines(grid, size, size)
   
myBoard.just_Print(size, size)

# myGame.play_game()
