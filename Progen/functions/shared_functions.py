import curses

from classes import GameVariables as GVar
        
# Return the total stats of the player from their gears
def full_stat(player,stat_type):
    all_stat=[]
    for item in player.equipped_items.values():
        all_stat.append(item.stats[stat_type])
    return sum(all_stat)

# TODO removed because unused?
# Return a simple colored string with the item symbol and name
def item_print(stdscr,x,y,item):
    stdscr.addstr(x,y,f"{item.name}")
    

def skip_next_input(state = True):
    GVar.skip_next_input = state