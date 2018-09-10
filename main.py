from menu import Menu
from boardFunctions import BoardFunctions
from UserInteraction import UserInteraction


myGame = Menu()
myGame.game_menu()

myBoard = BoardFunctions()
myInteraction = UserInteraction()

size = myGame.board_size
mines = myGame.mines_num

myBoard.mines_num = mines

grid = myBoard.make_grid(size, size)
myBoard.generate_mines(grid, size, size)

myBoard.just_print(grid,size, size)
myBoard.print_board(size,size,grid)


# myGame.play_game()
