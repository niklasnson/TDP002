import os
import sys
# -- declarations
level_map = []
levels = []
key_up = 'w' 
key_down = 'z'
key_left = 'a' 
key_right = 's'
player_normal='@'
floor=' '
crate='o'
storage='.'
player_on_storage='+'
crate_on_storage='*'
player='@'

def sokoban_levels():
    """ Loads all levels filenames into a list """
    for (dir, _, files) in os.walk("data_levels"):   
        for f in files:
            path = os.path.join(dir, f)
            levels.append(path)

def sokoban_load(filename, row=[]): 
    """ Loads a game map into level_data """
    with open(filename, encoding='utf-8') as level: 
        y = 0
        for line in level:
            x = 0 
            for char in line:
                if char != " " and char !="\n":
                    level_map.append([x, y, char])
                    x = x + 1
            y = y + 1
            
#        for line in level:
#            x = 0
#            for char in line:
#                if char != " " and char !="\n":
#                    row.append([x, char])
#                x = x + 1
#            level_map.append(row)
#            row=[]
#    print(level_map)

def sokoban_render_map(level_map=[], dx=0, dy=0):
    """ read the level_data and append floor to empty structures """
    helper_clear_screen()

    for y in level_map:
        for x in y:
            while x[0] > dx:
                print(' ', end='')
                dx += 1
            print(x[1], end='')
            dx += 1
        dx = 0
        dy += 1
        print('')
              
def sokoban_cmd():
    move = input("\nMake your move [w] [a] [s] [z] or (q): ")
    return list(move.lower())

def sokoban_game(level=0, moves=0, level_complete=False):
    """ This is the main gameloop """
    while level_complete == False:
        for key in sokoban_cmd():
            sokoban_render_map(level_map)
            x, y = find_player()
            print(x,y)
            if key == key_up and moveable(x, y - 1): 
                move(x, y - 1)
            if key == key_down:
                pass
            if key == key_left:
                pass
            if key == key_right:
                pass
            if key == 'q':
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

def find_player():
    """ locate the player on the board """
    for row in level_map: 
        x = 0 
        y = 0
                       
    return x ,y

def moveable(dx, dy):
    return true
    
def move(dx, dy):
    pass

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
    sokoban_game()
    
if __name__ == '__main__':
    main()
