from menu import Menu
from boardFunctions import BoardFunctions


myGame = Menu()
myGame.game_menu()

myBoard = BoardFunctions()

size = myGame.board_size
mines = myGame.mines_num

myBoard.mines_num = mines

grid = myBoard.make_grid(size)
myBoard.generate_mines(size,grid)

myBoard.just_print(size,grid)
myBoard.print_board(size,grid)

# myGame.play_game()
