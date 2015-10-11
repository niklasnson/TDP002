import random

values = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13 }

suits  = { 'hearts': 1, 'spades': 2 }

joker_a = ['joker_a', 27]

joker_b = ['joker_b', 27]
    
def create_deck():
    """
    Skapar kortleken
    """
    _deck = []
    for i in range(1, 3):
        for t in range(1, 14): 
            _deck.append([i,t])
    return _deck
    
def pick_card(deck):
    """
    Väljer ett slumpvalt kort genom att använda funktionen random.choice från random biblioteket.
    """
    return random.choice(deck) 

def shuffle_deck(deck_list):
    """
    Blandar kortleken genom att använda funktionen shuffle från random biblioteket. 
    """
    deck_list = random.shuffle(deck_list)

def solitare_deck(deck): 
    """
    Om joker_a befinner sig på position sist så flytta till index 1 
    """
    if find_card(joker_a, deck) == int(len(deck)-1):     
        move_card(joker_a, 1, deck)
    
    move_card(joker_b, deck.index(joker_b) + 2, deck) 
    
    if find_card(joker_b, deck) == int(len(deck)-1): 
        move_card(joker_b, 3, deck)    
    if find_card(joker_b, deck) == int(len(deck)-2):
        move_card(joker_b, 2, deck)

def split_deck(start_position, end_position, deck=create_deck()):
    """
    Splittar kortlekern och retnerar [start_position > end_position]
    """
    #print("start_position: " + str(start_position) + ", end_position: " + str(end_position))
    return deck[start_position:end_position]

def get_value(parse_text): 
    return False

def insert_card(card, position=0, deck=create_deck()):
    """
    Antingen lägger vi till kortet sist eller så lägger vi till det på 
    den position som anges. 
    """
    if position == 0: 
        deck.append(card)
    else:
        deck.insert(position, card)

def find_card(card_name, deck=create_deck()):
    return deck.index(card_name)

def find_jokers(deck=create_deck()):
    """
    Hittar positionen för den sista jokern
    """
    temp = []
    for position, i in enumerate(deck): 
        if i == joker_a or i == joker_b:
            temp.append(position)
    return temp

def value_of_card(position, deck=create_deck()):
    """
    Retunerar värdet på ett kort, ignorerar färgen på kortet. 
    """
    return deck[position][1]
    

def move_card(card_name, new_position, deck=create_deck()): 
    """
    Flyttar kort till en ny position
    """
    deck.insert(new_position, deck.pop(deck.index(card_name)))

def generate_keystream():
    keystream = []
    for i in "ABCDEFGHIHJLMNOPQRSTUVXYZ":
        keystream.append(i)
    return keystream 

def solitaire_keystream(length = 30, deck=create_deck()):
    """
    Skapar krypteringsnyckel av rätt längd.
    """
    insert_card(joker_a, 0, deck)
    insert_card(joker_b, 0, deck)
    shuffle_deck(deck)
    solitare_deck(deck)
    jokers = find_jokers(deck)
    deck_a = split_deck(0, jokers[0], deck) # från 0 till första jokern
    deck_b = split_deck(jokers[0], int(jokers[1] + 1), deck) # från första jokern till sista. 
    deck_c = split_deck(jokers[1] + 1, int(len(deck) - 1), deck) # från sista jokern till slutet
    solitaire_deck = deck_c + deck_b + deck_a # flytta runt delarna enligt mönster
    value_of_last_card = value_of_card(int(len(deck)-1), deck)
    deck_a = split_deck(0, value_of_last_card, deck)
    deck_b = split_deck(value_of_last_card, int(len(deck)-1), deck)
    solitaire_deck = deck_b + deck_a # flytta lika många från första
    
    start_at_card = value_of_card(0, deck)  # vilket är det första kortet som vi skall titta på

    keystream = generate_keystream()
    temp=""
    for i in range(0, length):
        temp += keystream[i] 

    return str(start_at_card)

def solitaire_encrypt(text, deck):
    """
    Skapar krypteringen 
    """
    # Skall ignorera alla tecken utom A-Z
    text = text.upper()
    key_phrase = solitaire_keystream(len(text), deck)
    return text

def solitare_decrypt(text, deck):
    """
    Krypterar upp ett krypterat meddelande
    """
    return false

def main():
    deck = create_deck()
    print(deck)
    #text = input("Ange text att kryptera: ")
    #secret_message = solitaire_encrypt(text, solitaire_deck)
    #print(solitaire_keystream(10))
    ##print(secret_message)
    #print(deck)
if __name__ == '__main__':
    main()

