import os
from operator import itemgetter
#
#
# game parameters 
#
#

level_complete = False 
moves_done=0
current_level = 0
levels = []
level_data = []

#
#
# game settings
#
#

key_right = 'l'
key_left = 'h' 
key_up = 'k' 
key_down = 'j'

player='@'
floor=' '
crate='o'
storage='.'
player_on_storage='+'
crate_on_storage='*'

#
#
# levels functions
#
#
def sokoban_levels():
    """
    loads all levels filenames into a list 
    """
    for (dir, _, files) in os.walk("data_levels"):   
        for f in files:
            path = os.path.join(dir, f)
            levels.append(path)

def sokoban_load(filename):
    """
    loads a game map into level_data
    """
    with open(filename, encoding='utf-8') as level: 
        y = 0 
        for line in level:
            x = 0
            for char in line:
                level_data.append([x, y, char])
                x = x + 1
            y = y + 1 
#
#
# render functions 
#
#

def get_map():
    """
    render level map from level_data
    """
    map = "\n"

    # loopa för varje y värde i level_data 
    for data in sorted(level_data, key = lambda x : (x[1], x[0])): # sort by second arg in current item   #for data in sorted(level_data, key=get_key):
        map += data[2]    
    return map

#
#
#  movement functions
#
#
def input_move():
    """
    input player move or quit command
    """
    str_help = 'level:{level} / moves:{moves}  [left: {left}] [up: {up}] [down: {down}] [right: {right}]  [q: quit]: '
    key = input(str_help.format(level=current_level,moves=moves_done,left=key_left, down=key_down, up=key_up, right=key_right))
    return key.lower()

def can_move(dx, dy):
    if get_obj(dx, dy) == " ":
        return True
    else: 
        return False

def move_player(dx, dy): 
    """
    moves player to a new position
    """
    x, y = find_player()
    
    level_data[get_pos(x, y)] = [x, y, " "]
    level_data[get_pos(dx, dy)] = [dx, dy, "@"]

def find_player():
    """
    returns the x, y position of player
    """
    for pos, data in enumerate(level_data):
        if data[2] == player:
            return data[0], data[1]

def get_pos(x, y): 
    for pos, data in enumerate(level_data): 
        if data[0] == x and data[1] == y: 
            return pos
        

def get_obj(x, y): 
    for pos, data in enumerate(level_data): 
        if data[0] == x and data[1] == y:
            return data[2]
#
#
# main and main loop functions 
#
#
def sokoban_display():
    """
    dsiplay the levelmap and wait for a input from user, this is the main game loop 
    """
    while level_complete == False:
        print(get_map())
        key = input_move()
        x, y = find_player()
        if key == 'q':
            False
            break
        if key == key_up and can_move(x, y - 1):
            move_player(x, y - 1) 
        if key == key_down and can_move(x, y + 1):
            move_player(x, y + 1)   
        if key == key_left and can_move(x - 1, y): 
            move_player(x - 1, y)   
        if key == key_right and can_move(x + 1 , y): 
            move_player(x + 1, y)  

def main():
    sokoban_levels()                        # loads leveles into list
    sokoban_load(levels[current_level])     # loads current level into level_data
    sokoban_display()                       # go into main game loop
if __name__ == '__main__':
    main()
