#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# -- declarations ----------------------------------------------------- 
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
    print(level_map)
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
            if key == key_up and player_moveable(x, y - 1): 
                move_player(x, y - 1)    
            if key == key_down and player_moveable(x, y + 1):
                move_player(x, y + 1) 
            if key == key_left and player_moveable(x - 1, y):
                move_player(x - 1, y) 
            if key == key_right and player_moveable(x + 1, y):
                move_player(x + 1, y) 
            if key == 'q':
                exit()
            sokoban_render_map(level_map)
        # kontrollera om level är klar

def find_player(x=0, y=0):
    """ locate the player on the board, returns x, y and current player sprite """
    for row in level_map:
        for item in row:
            if item[1] == player_normal or item[1] == player_on_storage:
                x = item[0]
                y = level_map.index(row)
                player = item[1]
    return [x, y, player]

def player_moveable(dx, dy):
    """ is the target a wall """
    x, y, player = find_player()
    moveable = False 
    return True
    try:
        if level_map[dy][dx][1] != wall:
            return True   
        elif level_map[dy][dx][1] == wall: 
            return False 
    except: 
        return True

def move_player(dx, dy):
    """ moves a player to a new position and deletes the old """
    x, y, player = find_player()
    level_map[dy].remove([x, player]) 
    for item in level_map[dy]:
        if item[0] > dx:
            level_map[dy].insert(level_map[dy].index(item), [dx, player])
            break
        
def clear_screen():
    """ clear the screen """
    os.system("clear")
    return

def exit():
    """ exits the game """
    sys.exit() # clean kill of application

def main():
    sokoban_levels()                        # loads leveles into list
    sokoban_load(levels[0])                 # loads current level into level_data
    sokoban_render_map(level_map)
    sokoban_game()
    
if __name__ == '__main__':
    main()
