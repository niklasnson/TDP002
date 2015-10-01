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
    return list(move.lower())

def sokoban_game(level=0, moves=0, level_complete=False):
    """ This is the main gameloop """
    sokoban_render_map(level_map)
    while level_complete == False:
        for key in sokoban_cmd():
            
            x, y, player = find_player()
            
            if key == key_up and player_moveable(x, y, x, y - 1): 
                move_player(x, y - 1)
                if get_map_object(x, y - 1) == normal_crate:
                    move_crate(x, y - 1, x , y - 2)

            if key == key_down and player_moveable(x, y, x, y + 1):
                move_player(x, y + 1) 
                if get_map_object(x, y + 1) == normal_crate:
                    move_crate(x, y + 1, x, y + 2)
            
            if key == key_left and player_moveable(x, y, x - 1, y):
                move_player(x - 1, y) 
                if get_map_object(x-1, y) == normal_crate:
                    move_crate(x - 1, y, x - 2, y)

            if key == key_right and player_moveable(x, y, x + 1, y):
                move_player(x + 1, y)
                if get_map_object(x+1, y) == normal_crate:
                    move_crate(x + 1, y, x + 2, y)

            if key == 'q':
                exit()
            
            sokoban_render_map(level_map)

def find_player(x=0, y=0):
    """ locate the player on the board, returns x, y and current player sprite """
    for row in level_map:
        for item in row:
            if item[1] == player_normal or item[1] == player_on_storage:
                x = item[0]
                y = level_map.index(row)
                player = item[1]
    return [x, y, player]

def player_moveable(x, y, dx, dy):
    """ can user move to a new location ? """
    xx, yy = crate_destination(x, y, dx, dy)
    map_object = get_map_object(dx, dy)
    
    if map_object == wall:
        return False

    if map_object == normal_crate and crate_moveable(xx,yy) == False: 
        return False
    
    return True

def move_player(dx, dy):
    """ moves a player to a new position and deletes the old """
    x, y, player = find_player()
    destroy_map_object(x, y, player)

    if player == player_on_storage: 
        create_map_object(x, y, storage)
        if get_map_object(dx, dy) == floor:
            player = player_normal
        if get_map_object(dx, dy) == storage:
            destroy_map_object(dx, dy, storage)

    elif player == player_normal:
        if get_map_object(dx, dy) == storage:
            player = player_on_storage
            destroy_map_object(dx, dy, storage)

    create_map_object(dx, dy, player)

def crate_moveable(dx, dy): 
    """ can crate move to a new location ? """ 
    map_object = get_map_object(dx, dy) 
    if map_object == floor: 
        return True
    if map_object == storage: 
        return True
    return False

def move_crate(x, y, dx, dy):
    """ move a crate to a new position """ 
    crate = get_map_object(x,y)
    destroy_map_object(x,y)
    if crate == crate_on_storage:
        destroy_map_object(x,y)
    if get_map_object(dx, dy) == storage:
        destroy_map_object(dx,dy)
    else: 
        crate = normal_crate
    create_map_object(dx, dy, crate)

def crate_destination(x, y, dx, dy): 
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

def get_map_object(dx,dy): 
    for item in level_map[dy]:
        if item[0] == dx:
            return item[1]
    return floor 

def create_map_object(dx, dy, obj): 
    """ create a object in level_map """ 
    for item in level_map[dy]:
        if item[0] > dx:
            level_map[dy].insert(level_map[dy].index(item), [dx, obj]) #kommer kanske att dö om vi är på 0?
            break 

def destroy_map_object(x, y, obj=''):
    if obj == '':
        obj = get_map_object(x, y)
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
    sokoban_load(levels[0])                 # loads current level into level_data
    sokoban_render_map(level_map)
    sokoban_game()
    
if __name__ == '__main__':
    main()
