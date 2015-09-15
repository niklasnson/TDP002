import random

values = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13 }
suits  = { 'clubs': 1, 'diamonds': 2, 'hearts': 3, 'spades': 4 }

joker_a = ['joker_a']
joker_b = ['joker_b']
    
def create_deck():
    """
    Skapar kortleken
    """
    _deck = []
    for i in range(1, 5):
        for t in range(1, 14): 
            _deck.append([i,t])
    return _deck
    
def pick_card(deck_list):
    """
    Väljer ett slumpvalt kort genom att använda funktionen random.choice från random biblioteket.
    """
    return random.choice(deck_list) 

def shuffle_deck(deck_list):
    """
    Blandar kortleken genom att använda funktionen shuffle från random biblioteket. 
    """
    deck_list = random.shuffle(deck_list)

def solitare_deck(deck_list): 
    """
    Om joker_a befinner sig på position sist så flytta till index 1 
    """
    if find_card(deck_list, ['joker_a']) == 53:     
        move_card(['joker_a'], deck_list, 1)
    move_card(['joker_b'], deck_list, deck_list.index(['joker_b']) + 2) 
    if find_card(deck_list, ['joker_b']) == 53: 
        move_card(['joker_b'], deck_list, 3)    
    if find_card(deck_list, ['joker_b']) == 52:
        move_card(['joker_b'], deck_list, 2)

def solitaire_keystream(length=30, deck_list={}):
    return False  

def split_deck(start_position, end_position, deck=create_deck()):
   return deck[int(start_position):int(end_position)] 

def get_value(parse_text): 
    return False

def insert_card(card, position=0, deck=create_deck()):
    if position == 0: 
        deck.append(card)
    else:
        deck.insert(position, card)

def find_card(deck, card_name):
    return deck.index(card_name)

def move_card(card_name, deck, new_position): 
    deck.insert(new_position, deck.pop(deck.index(card_name)))

def get_suit(parse_text): 
    return False 

def display_card(parse_text): 
    return False 

def main():
    deck = create_deck()
    shuffle_deck(deck)
    insert_card(joker_a, 0, deck)
    insert_card(joker_b, 0, deck)
    solitare_deck(deck)
    deck_a = split_deck(0, deck.index(joker_a) -1, deck) 
    #deck_a = split_deck(0, deck.index(joker_a) -1, deck)
    #deck_b = split_deck(deck, deck.index(['joker_a']), deck.index(['joker_b']))
    #deck_c = split_deck(deck, deck.index(['joker_b']) +1, len(deck))
   
    #deck = deck_c + deck_b + deck_a         # ersätt den tidigare listan med en ny. 
    
    print(deck_a)
if __name__ == '__main__':
    main()

