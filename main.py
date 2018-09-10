from menu import Menu
from boardFunctions import BoardFunctions
from UserInteraction import UserInteraction

myGame = Menu()
myGame.game_menu()

size = myGame.board_size
mines = myGame.mines_num

playing = UserInteraction(size,mines)
playing.play()


# myGame.play_game()
