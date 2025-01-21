class GameConstants():
    GAME_HEIGHT = 50
    GAME_WIDTH = 120
    colors = {
        "white": (785, 785, 785),
        "green": (400, 600, 408),
        "blue": (455, 510, 702),
        "purple": (510, 73, 115),
        "yellow": (710, 702, 431),
        "player_color" : (1000, 1000, 1000),
        "RED": (800, 100, 100),
        "GREEN": (100, 800, 100),
        "BLUE": (100, 100, 800),
        "WHITE": (1000, 1000, 1000),
        "GRAY4":  (400, 400, 400), 
        "health_green": (150, 650, 150)
    }


class GameVariables():
    main_player = None
    paused = False
    closing_game = False
    skip_next_input = False
    game_nav = "progen"
        # Possible values:
        #   - "progen": Seting up
        #   - "combat"
        #   - "room_transition"
        #   - "game_over"
        #   - "shop"
        #   - "campfire"
        #   - "boss_room"
    current_floor=1
    current_room=1
    
            
class GameWindows():
    pass
        # Possible values :
        #   - "GWin.stdscr": whole window (includes empty space)
        #   - "GWin.main_win": actualgame space
        #   - "GWin.pause_menu"
        
        #   - "GWin.combat_monster": monster names and health
        #   - "GWin.combat_player": player health
        #   - "GWin.combat_logs": what happened in the fight
        #   - "GWin.combat_location": show room and floor
        
        #   - "GWin.room_transition_location": show room and floor
        #   - "GWin.room_transition_room_1": left choice
        #   - "GWin.room_transition_room_2": right choice
