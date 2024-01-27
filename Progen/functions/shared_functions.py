import curses

from constants import Color
        
# Return the total stats of the player from their gears
def full_stat(player,stat_type):
    return sum(item.stats[stat_type] for item in player.equipped_items)

# Return a simple colored string with the item symbol and name
def item_print(stdscr,x,y,item):
    stdscr.addstr(x,y,f"{item.name}")
    
# Return an advance colored string with the item symbol, name, id, and stats
def full_item_print(item):
    return (f"\x1b[38;2;{item.color[0]};{item.color[1]};{item.color[2]}m"
          f"▣ " 
          f"{Color.rarity_colors[item.rarity]}"
          f"{item.name}" 
          f"\033[39m"
          f"\n"
          f"{str(item.stats['defense'])}"
          f" defense\n"
          )

# Return a simple colored string the character's name
def character_print(character):
    return (f"\x1b[38;2;{character.color[0]};{character.color[1]};{character.color[2]}m"
            f"{character.name}"
            f"\033[39m"
            )