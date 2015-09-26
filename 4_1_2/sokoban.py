import os
import sys

level_map = []
levels = []

def sokoban_levels():
    """ Loads all levels filenames into a list """
    for (dir, _, files) in os.walk("data_levels"):   
        for f in files:
            path = os.path.join(dir, f)
            levels.append(path)

def sokoban_load(filename, row=[]): 
    """ Loads a game map into level_data """
    with open(filename, encoding='utf-8') as level: 
        for line in level:
            x = 0
            for char in line:
                if char != " " and char !="\n":
                    row.append([x, char])
                x = x + 1
            level_map.append(row)
            row=[]
    print(level_map)

def sokoban_objects(obj):  
    """ dict containing game objects """
    objs = {'player': '@', 'crate': 'o', 'wall': '#', 'floor': ' ',
             'storage': '.', 'crate_stored': '*', 'player_stored': '+'}
    return objs[obj]

def sokoban_create_object(x, y, obj):
    """
    creates level and data 
    """
    level_map.append([x, y, obj])

def sokoban_render_map(level_map=[], dx=0, dy=0):
    """ read the level_data and append floor to empty structures """
    helper_clear_screen()
    for row in level_map: 
        for pos in row:
            while pos[0] > dx:
                print(pos, dx)
                print(sokoban_objects('floor'), end='')
                dx += 1
                continue
            print(pos[1], end='')
        print()
 
 #   for item[2] in sorted(level_map, key = lambda x : (x[1], x[0])):
 #       print(y)
 #       while dx < item[0]:
 #           _map.append([dx, dy, sokoban_objects('floor')])
 #           dx += 1
 #           print(dx, ":", dy, end=':')
 #           _map.append([dx, dy, item[2]])
 #       dx, dy = set_sokoban_xy(item[0],item[1], dx, dy, _map)
 #   print(_map)
 #   for item in _map: 
 #       print(item[2], end='')
            
def sokoban_render_object(obj=' ', sokoban_level=''):
    sokoban_level += obj         

def set_sokoban_xy(x, y, dx, dy, _map=[]):
    """ Set position of the dx, dy and adds """
    if y == dy:
        dx += 1 
    else:
        dy = y 
        dx = 0 
        _map.append([dx, dy, '\n'])
        print('\n', end='')
    return dx, dy

def sokoban_render_help(): 
    cli_help = """

    @ is you
    + is you standing on storage
    # is a wall
    . is empty storage
    o is a crate
    * is a create on storage

    to move:        w
                a       s
                    z

    to quit: q
    to show this message: ?

    you can input multiple commands like: lllllkkjjh
    """
    print(cli_help)

    """ Render level map from level_data """
    sokoban_map = sokoban_render_map(level_map)
    print(sokoban_map)

def sokoban_game(level=0, moves=0, level_complete=False):
    """ This is the main gameloop """
    direction = { 'w': 1, 'z': -1, 'a': 1, 's': -1 }
    while True:
        sokoban_render_map(level_map)
        inputs = helper_getmove(level, moves) 
        for cmd in inputs:
            if cmd in ['w''z''a''s']:
                if cmd in ['a''z']:
                    pass
                if cmd in ['w''z']:
                    pass
            if cmd == 'q':
                sokoban_exit()

def sokoban_exit():
    """ exits the game """
    sys.exit() # clean kill of application

def helper_debug_l(data):
    for item in data: 
        print(item)

def helper_debug_s(string): 
    print(string)

def helper_sort(level_map=level_map):
    """ sort the level on x and y cords """
    temp = []
    for item in sorted(level_map, key = lambda x : (x[1], x[0])): # sort by second arg in current item  
        temp += item[2]   
    return temp 

def helper_find_player():
    """ returns the x, y and sprite of player """
    for pos, data in enumerate(level_map):
        if data[2] == player:
            return data[0], data[1], data[2]

def helper_move(dx, dy):
    """ move objects to new location """
    pass

def helper_moveable(dx,dy): 
    """ can move to location """
    pass

def helper_getmove(level, moves): 
    """ input player move or quit command """
    str_help = 'level:{level} / moves:{moves} $: '
    keys = input(str_help.format(level=level + 1,moves=moves))
    keys = list(keys.lower())
    return keys

def helper_clear_screen():
    """ clear the screen """
    os.system("clear")
    return

def main():
    sokoban_levels()                        # loads leveles into list
    sokoban_load(levels[0])                 # loads current level into level_data
    sokoban_render_map(level_map)
    #sokoban_game()

if __name__ == '__main__':
    main()
