import os

level_data = []
levels = []
key_right = 's'
key_left = 'a'
key_up = 'w'
key_down = 'z'
player_normal='@'
floor_object=' '
crate='o'
storage='.'
player_on_storage='+'
crate_on_storage='*'
player='@'


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
                if char != " " and char !="\n":
                    append_object(x, y, char)
                x = x + 1
            y = y + 1 

def append_object(x, y, obj):
    """
    creates level and data 
    """
    level_data.append([x, y, obj])

def sokoban_render_map(data=[], dx=0, dy=0, sokoban_map=''):
    for obj in sorted(level_data, key = lambda x : (x[1], x[0])):
        if obj[0] > dx: 
            sokoban_map += " "
        else:
            sokoban_map += obj[2]
        dx, dy, sokoban_map = set_sokoban_xy(obj[0],obj[1], dx, dy, sokoban_map)


    return [sokoban_map]
            
def sokoban_render_object(obj=' ', sokoban_level=''):
    sokoban_level += obj        

def set_sokoban_xy(x, y, dx, dy, sokoban_map):
    if y == dy:
        dy = y
        dx += 1 
    else:
        dy = dy 
        dx = 0   
        sokoban_map += '\n'

    return dy, dx, sokoban_map


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

def sokoban_show_map(level_data=level_data, dx=0, dy=0):
    """
    render level map from level_data
    """
    sokoban_map = sokoban_render_map(level_data)
    print(sokoban_map)


def sokoban_game(level=0, moves=0, level_complete=False):
    """
    This is the main gameloop
    """
    #print(sorted(level_data, key = lambda x : (x[1], x[0])))
    #helper_debug_l(level_data)
    sokoban_show_map(level_data)

def helper_debug_l(data):
    for item in data: 
        print(item)

def helper_debug_s(string): 
    print(string)

def helper_sort(level_data=level_data):
    temp = []
    for item in sorted(level_data, key = lambda x : (x[1], x[0])): # sort by second arg in current item  
        temp += item[2]   
    return temp 

def helper_find_player():
    """
    returns the x, y and sprite of player
    """
    for pos, data in enumerate(level_data):
        if data[2] == player:
            return data[0], data[1], data[2]

def helper_move(dx, dy):
    """
    Move objects to new location
    """
    pass

def helper_moveable(dx,dy): 
    """
    Can move to location 
    """
    pass

def helper_getmove(level, moves): 
    """
    input player move or quit command
    """
    str_help = 'level:{level} / moves:{moves} $: '
    keys = input(str_help.format(level=level + 1,moves=moves))
    keys = list(keys.lower())
    return keys

def main():
    sokoban_levels()                        # loads leveles into list
    sokoban_load(levels[0])                 # loads current level into level_data
    sokoban_game()
if __name__ == '__main__':
    main()
