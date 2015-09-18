# game parameters 
moves_spent     = 0
current_level   = 1

level_data      = []


# game settings
key_right   = "l"
key_left    = "h" 
key_up      = "k" 
key_down    = "j"

def input_player_move():
    key = input("level:{level} / moves:{moves}  [left: {left}] [up: {up}] [down: {down}] [right: {right}]  [q: quit]: ".format(level=current_level,moves=moves_spent,left=key_left, down=key_down, up=key_up, right=key_right))
    return key.lower()

def initialize_sokoban_level(level): 
    sokoban_load(level)

def render_game_map():
    """
    render level map from level_data
    """
    map = ""
    for position in level_data:
        map += position[2]
    return map

def update_game_map(data):
    """
    updates level data.
    """
    level_data[data[0]] = [data[1], data[2], "@"]

def player_position(player):
    """
    returns the user position. 
    """
    for pos, data in enumerate(level_data):
        if data[2] == player:
            position = [pos, data[0], int(data[1] + 1)]
    return position

def move_player(position): 
    """
    moves player to a new position
    """
    update_game_map(position)
    moves_spent = moves_spent + 1

def sokoban_move(key): 
    """
    moves user to a new
    """
    keys = [key_right, key_left, key_up, key_down]
    if key in keys:
        position = player_position("@")
        move_player(position)
    
def sokoban_display():
    """
    dsiplay the levelmap and wait for a input from user. 
    """
    while True:
        print("\n") 
        print(render_game_map()) 
        key = input_player_move()
        if key == "q":
            False
            break
        else: 
            try: 
                sokoban_move(key)
            except: 
                False

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

def main():
    initialize_sokoban_level('data_levels/level_1.sokoban')
    sokoban_display()

if __name__ == '__main__':
    main()
