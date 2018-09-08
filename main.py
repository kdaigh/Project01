from BoardFunctions import BoardFunctions

if __name__ == "__main__":
    myGame = BoardFunctions()
    myGame.game_menu()
    size = myGame.boardSize
    mines = myGame.mines_num
    myGame.make_grid(size, size)
    myGame.print_board(size, size)
