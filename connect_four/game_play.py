from vars_game_board import *
from vars_players import *
from game_helper_functions import *

print("\nWelcome to Connect4!")
print("\nMatch:", player_1.name, "vs.", player_2.name)

print_game_board()

turn_counter = 0
while True:
    if turn_counter % 2 == 0:
        turn(player_1.colour)
        winner = check_for_winner(colour_assignment(player_1.colour), player_1.name)
        turn_counter += 1
        print_game_board()
    else:
        turn(player_2.colour)
        winner = check_for_winner(colour_assignment(player_2.colour), player_2.name)
        turn_counter += 1
        print_game_board()

    if winner:
        break