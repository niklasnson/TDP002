#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

# -- declarations ----------------------------------------------------- 
level_map = []
levels = []
key_up = 'w' 
key_down = 'z'
key_left = 'a' 
key_right = 's'
player_normal='@'
floor=' '
normal_crate='o'
storage='.'
player_on_storage='+'
crate_on_storage='*'
wall='#'

def sokoban_logo(): 
    logo = """ 
        .d88888b           dP                dP                         
        88.    "'          88                88                         
        `Y88888b. .d8888b. 88  .dP  .d8888b. 88d888b. .d8888b. 88d888b. 
              `8b 88'  `88 88888"   88'  `88 88'  `88 88'  `88 88'  `88 
        d8'   .8P 88.  .88 88  `8b. 88.  .88 88.  .88 88.  .88 88    88 
         Y88888P  `88888P' dP   `YP `88888P' 88Y8888' `88888P8 dP    dP 
        oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

    """

    print(logo)


def sokoban_complete(): 
    logo = """


    dP                                   dP     a88888b.                               dP            dP            dP 
    88                                   88    d8'   `88                               88            88            88 
    88        .d8888b. dP   .dP .d8888b. 88    88        .d8888b. 88d8b.d8b.  88d888b. 88 .d8888b. d8888P .d8888b. 88 
    88        88ooood8 88   d8' 88ooood8 88    88        88'  `88 88'`88'`88  88'  `88 88 88ooood8   88   88ooood8 dP 
    88        88.  ... 88 .88'  88.  ... 88    Y8.   .88 88.  .88 88  88  88  88.  .88 88 88.  ...   88   88.  ...    
    88888888P `88888P' 8888P'   `88888P' dP     Y88888P' `88888P' dP  dP  dP  88Y888P' dP `88888P'   dP   `88888P' oo 
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo~88~ooooooooooooooooooooooooooooooooooooo
                                                                              dP                                      

    """

    print(logo)
    


def sokoban_levels(): 
    """ Loads all levels filenames into a list """
    for (dir, _, files) in os.walk("data_levels"):   
        for f in files:
            path = os.path.join(dir, f)
            levels.append(path)


def sokoban_load(filename, row=[]): 
    """ Loads a game map into level_data """
    
    with open(filename, 'r', encoding='utf-8') as level: 
        for line in level:
            x = 0
            for char in line:
                if char != " " and char !="\n":
                    row.append([x, str(char)])
                x = x + 1
            level_map.append(row)
            row=[]


def sokoban_render_map(level_map=[], dx=0, dy=0):
    """ read the level_data and append floor to empty structures """
    clear_screen()
    # -- debug print(level_map)
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
    return move.lower()


def sokoban_game():
    """ This is the main gameloop """
    level = False 
    clear_screen()
    sokoban_logo()
    while not level: 
        try: 
            level = input("Select a level 1 - 2")
            int(level) 
        except: 
            print("A level number!")
            level = False 
    level = int(level) - 1

    sokoban_load(levels[level])
    sokoban_render_map(level_map)
    while True:
        key = sokoban_cmd()
            
        x, y, player = find_player()
            
        if key == key_up and player_moveable(x, y, x, y - 1): 
            move(x, y, x, y - 1, player)
        if key == key_down and player_moveable(x, y, x, y + 1):
            move(x, y, x, y + 1, player)
        if key == key_left and player_moveable(x, y, x - 1, y):
            move(x, y, x - 1, y, player)
        if key == key_right and player_moveable(x, y, x + 1, y):
            move(x, y, x + 1, y, player)
        if key == 'q':
            exit()
                
        sokoban_render_map(level_map)
        if did_player_win(level_map):
            clear_screen()
            sokoban_complete()
            time.sleep(2) 
            break

def did_player_win(level_map):
    for row in level_map:
        for item in row: 
            if item[1] == normal_crate:
                return False 
    return True


def find_player(x=0, y=0):
    """ locate the player on the board, returns x, y and current player sprite """
    for row in level_map:
        for item in row:
            if item[1] == player_normal or item[1] == player_on_storage:
                x = item[0]
                y = level_map.index(row)
                player = item[1]
    return [x, y , player]


def player_moveable(x, y, dx,  dy):
    """ can user move to a new location ? """
    xx, yy = crate_destination(x, y, dx, dy)
    map_object = get_object(dx, dy)
    if map_object == wall:
        return False
    if map_object == normal_crate and crate_moveable(xx,yy) == False: 
        return False
    if map_object == crate_on_storage and crate_moveable(xx,yy) == False:
        return False
    return True 


def crate_moveable(dx, dy): 
    """ can crate move to a new location ? """ 
    map_object = get_object(dx, dy) 
    if map_object == floor: 
        return True
    if map_object == storage: 
        return True
    return False


def move(x, y, dx, dy, obj):
    """ experimental move command """ 
    target = get_object(dx, dy)
    xx, yy = crate_destination(x, y, dx, dy)

    destroy_object(x, y)

    if obj in [player_normal, player_on_storage]:
    # we are moving the player     
        player = player_normal

        if target == storage:
            destroy_object(dx, dy)
            player = player_on_storage

        if target == normal_crate:
            move(dx, dy, xx, yy, normal_crate)

        if target == crate_on_storage: 
            move(dx, dy, xx, yy, crate_on_storage)
            player = player_on_storage
            
        if obj == player_on_storage: 
            create_object(x, y, storage)

        create_object(dx, dy, player)

    if obj in [crate_on_storage, normal_crate]:
    # we are moving crates
        crate = normal_crate
        if target == storage and obj == normal_crate:
            destroy_object(dx, dy)
            crate = crate_on_storage 
        
        if target == storage and obj == crate_on_storage: 
            destroy_object(dx, dy)
            crate = crate_on_storage

        create_object(dx, dy, crate)


def crate_destination(x, y, dx , dy): 
    """ where is the player moving """
    if x == dx: 
        xx = dx
        if y > dy: 
            yy = dy - 1
        else:
            yy = dy + 1

    if y == dy: 
        yy = dy
        if x > dx:
            xx = dx - 1
        else: 
            xx = dx + 1
    
    return xx, yy 


def get_object(dx,dy): 
    for item in level_map[dy]:
        if item[0] == dx:
            return item[1]
    return floor 


def create_object(dx, dy, obj): 
    """ create a object in level_map """ 
    for item in level_map[dy]:
        if item[0] > dx:
            level_map[dy].insert(level_map[dy].index(item), [dx, obj]) #kommer kanske att dö om vi är på 0?
            break 


def destroy_object(x, y, obj=''):
    if obj == '':
        obj = get_object(x, y)
    level_map[y].remove([x, obj])


def d(text): 
    print(text)
    time.sleep(3)


def clear_screen():
    """ clear the screen """
    os.system("clear")
    return 

def exit():
    """ exits the game """
    sys.exit() # clean k ill of application

def main():
    sokoban_levels()                        # loads leveles into list
    sokoban_game()
    
if __name__ == '__main__':
    main()
