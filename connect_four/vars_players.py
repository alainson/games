from game_helper_functions import player_setup

player_selections = player_setup()

# Player info
class Player:
   def __init__(self, name, colour):
    self.name = name
    self.colour = colour

player_1 = Player(player_selections[0], player_selections[2])
player_2 = Player(player_selections[1], player_selections[3])