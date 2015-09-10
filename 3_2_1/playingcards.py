import random

joker_a = 'joker A'
joker_b = 'joker B'

def create_deck():
    suits = [1,2]
    values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    deck = []
    for i in suits: 
        for v in values: 
            deck.append([i,v,int(len(deck) + 1)]) 
    
    insert_joker(joker_a, deck)
    insert_joker(joker_b, deck)

    shuffle_deck(deck)
    cut_deck(deck)

    return deck

def insert_joker(name, deck): 
    deck.append([name, 27, int(len(deck) + 1)]) 

def shuffle_deck(deck): 
    deck = random.shuffle(deck)

def cut_deck(deck): 
    # flyttar 10 kort till slutet av leken.
    for i in range(0,11):
        move_card(0, len(deck) - 1, deck)

def split_deck(start_position, end_position, deck): 
    return deck[start_position:end_position]

def find_jokers_in_deck(deck):
    #retunerar en array med positionen av dom två jokrarna. 
    temp = []
    for position, i in enumerate(deck): 
        if i[0] == joker_a or i[0] == joker_b:
            temp.append(position)
    return temp

def move_card(old_position, new_position, deck):
    deck.insert(new_position, deck.pop(old_position))

def get_value_of_card(position, deck):
    #retunerar värdet av viss pisition i korleken. 
    return deck[position][2]

def create_alphabet():
    temp = {}
    for i in "ABCDEFGHIJKLMNOPQSTUVXYZ":
        temp[str(i)] = int(len(temp) + 1)
    return sorted(temp)         # eftersom vi vill ha listan från A=Z 

def convert_char_to_number(char, alphabet_list=create_alphabet()):
    # skicka in en boktsav och du får tillbaka en siffra. 
    return int(alphabet_list[char])

def convert_number_to_char(number, alphabet_list=create_alphabet()):
    # skicka in en siffra och du får tillbaka en bokstav. 
    for key, value in enumerate(alphabet_list):
        if int(key) == int(number): 
            return value
            break

def solitare_keystream(length = 30, deck=create_deck()): 
    jokers_is_at = find_jokers_in_deck(deck)
    deck_a = split_deck(0, jokers_is_at[0], deck) # från 0 till första jokern
    deck_b = split_deck(jokers_is_at[0], int(jokers_is_at[1] + 1), deck) # från första jokern till sista.
    deck_c = split_deck(jokers_is_at[1] + 1, int(len(deck) - 1), deck) # från sista jokern till slutet
    deck = deck_c + deck_b + deck_a # flytta runt delarna enligt mönster
    value_of_last_card = get_value_of_card(int(len(deck)-1), deck) # hämta värdet på det sista kortet
    deck_a = split_deck(0, value_of_last_card, deck) # från position 0 till värdet på det sista kortet i leken.
    deck_b = split_deck(value_of_last_card, int(len(deck)-1), deck) #från positionen av det sista kortet till längden av leken. 
    deck = deck_b + deck_a 
    alphabet = create_alphabet()

    return alphabet

def solitare_encrypt(message, solitare_deck):
    message = message.upper()
    #key_phrase = solitare_keystream(len(message), solitare_deck)

    message_in_numbers = []

    for char in message:
        #message_in_numbers.append(convert_char_to_number(char))
        print(char)
        
    return message_in_numbers

def solitare_decrypt():
    return false

def main():
    solitare_deck = create_deck()
    message = input("Text att kryptera: ")
    print(solitare_encrypt(message, solitare_deck))
    print(create_alphabet())

if __name__ == '__main__':
    main()
