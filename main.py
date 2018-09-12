from menu import Menu
from boardFunctions import BoardFunctions
from UserInteraction import UserInteraction

#myGame = Menu()
#myGame.game_menu()

myGame = UserInteraction()
size = myGame.size
mines = myGame.mines
myGame.game_menu()

playing = UserInteraction()
playing.play()



# myGame.play_game()
