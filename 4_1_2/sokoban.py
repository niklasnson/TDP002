# game parameters 
moves_spent     = 0
current_level   = 1

soko_walls      = []    #X,Y kordinater
soko_crates     = []    #X,Y kordinater
soko_storage    = []    #X,Y kordinater
soko_player     = []    #X,Y kordinater


# game settings
key_right   = "L"
key_left    = "H" 
key_up      = "K" 
key_down    = "J"


def input_player_move():
    input("level:{level}/moves:{moves} move: [Left: {left}] [Up: {up}] [Down: {down}] [Right: {right}] : ".format(level=current_level,moves=moves_spent,left=key_left, down=key_down, up=key_up, right=key_right))


# gå igenom filen och stoppa in kordinater för varje object i en lista. 
# denna lista kan vi sedan använda för att veta om vi kan röra oss eller inte. 

def initialize_sokoban_level(level): 
    level_data = sokoban_load(level)
    print(level_data)

def update_sokoban_data(soko_list, x, y):
    False 


def sokoban_display():
    """
    @ Lagerarbetare 
    O Lådorna 
    # Väggar 
      Golvyta 
    . Lagringsplats
    * Låda som står på en lagringsplats
    + Lagerarbetare som står på en lagringsplats
    """
    input_player_move()

def sokoban_load(filename):
    """
    Loads a game map and returns a string object.
    """
    f = open(filename)
    level = f.read()
    return level

def player_can_move(X,Y):
    """
    returns true or false if user can move to new position
    """
    False

def crate_can_move():
    False

def main():
    initialize_sokoban_level('data_levels/level_1.sokoban')
    sokoban_display()

if __name__ == '__main__':
    main()
