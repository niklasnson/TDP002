import os
from operator import itemgetter
import sys

#
#
# game parameters 
#
#
level_complete = False 
moves_spent = 0
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

player_normal='@'
floor=' '
crate='o'
storage='.'
player_on_storage='+'
crate_on_storage='*'

player='@'

cli_help = """
    
    @ is you 
    + is you standing on storage 
    # is a wall 
    . is empty storage 
    o is a crate 
    * is a create on storage 

    to move:        k
                h       l
                    j

    to quit: q 
    to show this message: ? 

    you can input multiple commands like: lllllkkjjh

"""


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
def cmd():
    """
    input player move or quit command
    """

    str_help = 'level:{level} / moves:{moves} $: '
    keys = input(str_help.format(level=current_level + 1,moves=moves_spent))
    keys = list(keys.lower())
    return keys

def can_move(dx, dy):
    if get_obj(dx, dy) != "#":
        return True
    else: 
        return False

def move(dx, dy):
    x, y = find_player()    # where is plyer
    target = get_obj(dx, dy)   # what is on target
    
    if floor == target:
        player = player_normal
        level_data[get_pos(x, y)] = [x, y, " "]
        level_data[get_pos(dx, dy)] = [dx, dy, player]
    if crate == target: 
        False 
    if storage == target: 
        player = player_on_storage
        level_data[get_pos(x, y)] = [x, y, " "]
        level_data[get_pos(dx, dy)] = [dx, dy, player]
        
def find_player():
    """
    returns the x, y position of player
    """
    for pos, data in enumerate(level_data):
        if str(data[2]) == str(player):
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
# main, exit and main loop functions 
#
#
def sokoban_display():
    """
    dsiplay the levelmap and wait for a input from user, this is the main game loop 
    """
    while level_complete == False:
        for key in cmd():
            print(get_map())
            x, y = find_player()
            if key == 'q':
                exit()
            if key == key_up and can_move(x, y - 1):
                move(x, y - 1) 
            if key == key_down and can_move(x, y + 1):
                move(x, y + 1)   
            if key == key_left and can_move(x - 1, y): 
                move(x - 1, y)   
            if key == key_right and can_move(x + 1 , y): 
                move(x + 1, y)  
            if key == '?': 
                print(cli_help)

def exit():
    print("Bye bye")
    sys.exit() # clean kill of application

def main():
    sokoban_levels()                        # loads leveles into list
    sokoban_load(levels[current_level])     # loads current level into level_data
    print(get_map())                        # draw map for first time.
    sokoban_display()                       # go into main game loop    
    
if __name__ == '__main__':
    main()
