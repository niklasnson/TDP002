import os

level_data = []
levels = []
key_right = 's'
key_left = 'a' 
key_up = 'w' 
key_down = 'z'
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

    to move:        w
                a       s
                    z

    to quit: q 
    to show this message: ? 

    you can input multiple commands like: lllllkkjjh

"""

 
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
                    append_level_data(x, y, char)
                x = x + 1
            y = y + 1 

def append_level_data(x, y, obj):
    """
    creates level and data 
    """
    level_data.append([x, y, obj])

def show_map(level_data=level_data, dx=0, dy=0):
    """
    render level map from level_data
    """
    #print(level_data)
    game_map = render_map(level_data)
    #sort_map(game_map)
    print(game_map)

def render_map(data=[], dx=0, dy=0):
    temp = []
    for obj in data:
        if obj[0] == dx:
            temp.append(obj)

def sort_map(level_data=level_data):
    temp = []
    for item in sorted(level_data, key = lambda x : (x[1], x[0])): # sort by second arg in current item  
        temp += item[2]   
    return temp

def find_player():
    """
    returns the x, y and sprite of player
    """
    for pos, data in enumerate(level_data):
        if data[2] == player:
            return data[0], data[1], data[2]

def move(dx, dy): 
    """
    move player to a new position
    """
    False 

def cmd(level, moves):
    """
    input player move or quit command
    """
    str_help = 'level:{level} / moves:{moves} $: '
    keys = input(str_help.format(level=level + 1,moves=moves))
    keys = list(keys.lower())
    return keys

def sokoban_display(level=0, moves=0, level_complete=False):
    show_map()

def main():
    sokoban_levels()                        # loads leveles into list
    sokoban_load(levels[0])                 # loads current level into level_data
    #sokoban_display(level_data)
    print(level_data)
if __name__ == '__main__':
    main()
