# See LexeCMD for more informations
class BaseColor :
    SYS_RED = [145, 32, 49]
    SYS_PURPLE = [161, 141, 181]
    RARITY_WHITE = [200, 200, 200]
    RARITY_GREEN = [101, 153, 104]
    RARITY_BLUE = [116, 130, 176]
    RARITY_PURPLE = [130, 73, 115]
    RARITY_YELLOW = [181, 179, 110]
    
    
class Color :
    pass

for i in {k: v for k, v in vars(BaseColor).items() if not k.startswith('__')}:
    setattr(Color, i, "\x1b[38;2;{};{};{}m".format(*getattr(BaseColor, i)))
    
    
Color.rarity_colors = {
    "white": Color.RARITY_WHITE,
    "green": Color.RARITY_GREEN,
    "blue": Color.RARITY_BLUE,
    "purple": Color.RARITY_PURPLE,
    "yellow": Color.RARITY_YELLOW
}