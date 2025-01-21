from classes import GameVariables as GVar
from .shared_functions import skip_next_input
#TODO give player choice between heal, other

def campfire():
    plr = GVar.main_player
    plr.current_hp = plr.max_hp # TODO make a function heal("max")
    GVar.game_nav = "room_transition"
    skip_next_input()