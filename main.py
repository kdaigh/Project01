from menu import Menu
from boardFunctions import BoardFunctions
from UserInteraction import UserInteraction

myGame = Menu()
myGame.game_menu()

size = myGame.board_size
mines = myGame.mines_num

playing = UserInteraction()
playing.play(mines,size)


# myGame.play_game()
