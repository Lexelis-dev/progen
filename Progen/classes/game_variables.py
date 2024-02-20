class GameConstants():
    GAME_HEIGHT = 50
    GAME_WIDTH = 120

class GameVariables():
    main_player = None
    paused = False
    closing_game = False
    skip_next_input = False
    game_nav = "progen"
        # All possible values : progen, combat,
            # room_transition, game_over, shop, campfire, boss_room
    current_floor=1
    current_room=1
            
class GameWindows():
    pass