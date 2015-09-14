import random

joker_a = 'joker A'
joker_b = 'joker B'
seed = '404'

def create_deck():
    # Skapar alltid en blandad lek som ser precis lika ut! 
    suits = [1,2]
    values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    deck = []
    for i in suits: 
        for v in values: 
            deck.append([i,v,int(len(deck) + 1)]) 
    
    insert_joker(joker_a, deck)
    insert_joker(joker_b, deck)

    #shuffle_deck(deck)
    #cut_deck(deck)
    print(deck)
    return deck

def insert_joker(name, deck): 
    deck.append([name, 27, int(len(deck) + 1)]) 

def shuffle_deck(deck): 
    random.seed(seed)
    deck = random.shuffle(deck)                                 # för att vi skall få en lika blandad funktion varje gång.

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
    #retunerar värdet av visst position i korleken. 
    return deck[position][1]
    # 0 = färgen
    # 1 = värdet 
    # 2 = unikt nummer 

def convert_char_to_number(char): 
    return int(ord(char) - 64) # A = 1 

def convert_number_to_char(number): 
    return chr(number + 64)  # 1 = A 


def convert_string_to_numbers(string): 
    temp = []
    for char in string: 
        temp.append(convert_char_to_number(char))

    return temp

def solitare_keystream(length = 30, deck=create_deck()):
    temp_deck = deck 
    shuffle_deck(temp_deck)                 # skall köras innan vi kommer in i loopen >>>>
    cut_deck(temp_deck)                     # skall köras innan vi kommer in i loopen >>>>

    keychain = []
    while len(keychain) < length:
        jokers_is_at = find_jokers_in_deck(temp_deck)
        deck_a = split_deck(0, jokers_is_at[0], deck) # från 0 till första jokern
        deck_b = split_deck(jokers_is_at[0], int(jokers_is_at[1] + 1), temp_deck) # från första jokern till sista.
        deck_c = split_deck(jokers_is_at[1] + 1, int(len(temp_deck) - 1), temp_deck) # från sista jokern till slutet
        deck = deck_c + deck_b + deck_a # flytta runt delarna enligt mönster
        value_of_last_card = get_value_of_card(int(len(temp_deck)-1), temp_deck) # hämta värdet på det sista kortet
        deck_a = split_deck(0, value_of_last_card, temp_deck) # från position 0 till värdet på det sista kortet i leken.
        deck_b = split_deck(value_of_last_card, int(len(temp_deck)-1), temp_deck) #från positionen av det sista kortet till längden av leken. 
        temp_deck = deck_b + deck_a 
        
        print(temp_deck)


        index_of_card = get_value_of_card(0, temp_deck)          # bestäm värdet på det första kortet
                                                                 # kan det vara en joker ?!
        if index_of_card <= 26:
            if get_value_of_card(index_of_card, temp_deck) <= 26:
                 keychain.append(get_value_of_card(index_of_card, temp_deck))

    return keychain 


def sum_of(list_1, list_2):
    # för varje värde i lista_1 gå igenom och lägg till med värde 2. Om vi blir < 26 dra ifrån 26 
    temp = []
    for i in range(len(list_1)):
        value = list_1[i] + list_2[i]
        if value <= 26:
            temp.append(value)
        else: 
            temp.append(value - 26)
    return temp 

def diff_of(list_1, list_2):
    temp = []
    for i in range(len(list_1)): 
        value = list_1[i] - list_2[i]
        if value >= 0:
            temp.append(value)
        else:
            temp.append(value + 26)

    return temp

def solitare_encrypt(message, solitare_deck):
    message = message.upper()
    # TODO: här måste vi kolla om tecken är A-Z
    key_in_numbers = solitare_keystream(len(message), solitare_deck)
    message_in_numbers = convert_string_to_numbers(message)
    crypt_in_numbers = sum_of(key_in_numbers, message_in_numbers)
    crypt_in_letters = []

    for i in crypt_in_numbers:
        crypt_in_letters.append(convert_number_to_char(i))

    return "".join(crypt_in_letters)

def solitare_decrypt(message, solitare_deck):
    key_in_numbers = solitare_keystream(len(message), solitare_deck) # skapa en ny key
    message_in_numbers = convert_string_to_numbers(message)          # conv
    print(key_in_numbers)
    print(message_in_numbers)
    
    crypt_in_numbers = diff_of(key_in_numbers, message_in_numbers)
    
    message = []
    for i in crypt_in_numbers:
        print(str(i) + " => " + convert_number_to_char(i))
        message.append(convert_number_to_char(i))  

    return "".join(message) 

def main():
    #solitare_deck = create_deck()

    test_data = ['LENNART', 'ASTA', 'BILEN', 'GURKA', 'SIRI']
    for i in test_data: 
        solitare_keystream(len(i))
        #print(" ") 
        #print(solitare_keystream(len(i)))
        #print(solitare_keystream(len(i)))
        #secret_message = str(solitare_encrypt(i, solitare_deck)) 
        #print(i + " => " + secret_message + " => " + str(solitare_decrypt(secret_message, solitare_deck)))
    
if __name__ == '__main__':
    main()
