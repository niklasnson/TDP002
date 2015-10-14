from pprint import pprint                                   # imporove readablity 

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def linear_search(haystack, needle, f= lambda e: e['title']): 
    for item in haystack:
        if str(f(item)).lower() == str(needle).lower():     # loop, if item is found return and quit, using lower to imporve match 
            return item
""" ------------------------------------------------------------------------------------------------------------------------------------ """

def binary_search(haystack, needle, f= lambda e: e['title']): 
    haystack.sort(key = f)                                  # binary search only work if the data is sorted - so lets sort! 
    base = 0                                                # min value  
    head = len(haystack)                                    # highest value 

    while base <= head: 
        inner = (base + head) // 2                          # get the middle value of current base & head
        if f(haystack[inner]) < needle:                     # if inner, value is less then needle value 
            base = inner + 1                                # set base to inner and add one 
        elif f(haystack[inner]) > needle:                   # if inner is more then needle 
            head = inner - 1                                #     
        else: return haystack[inner]                        # we got a match

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def insertion_sort(db, f= lambda e: e[0]):
    
    for pos in range(len(db)):                              # for pos in length of db:
        while pos > 0 and f(db[pos - 1]) > f(db[pos]):      # while pos is larger then 0 | db position (-1) is larger the db(pos)
            db[pos - 1], db[pos] = db[pos], db[pos -1]      # swap values 
            pos -= 1                                        # decrease pos and continue the while. 

                                                            # if not found return will be None 

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def quicksort(db, f= lambda e: e[0]):
    less = []
    equal = []
    greater = []

    if len(db) > 1:                                         # if lenght of db larger then 1 
        inner = db[len(db)//2]                              # inner value is half of the lenght of db.
        for item in db:                                     # loop
            if f(item) < f(inner):                          # if function item is smaller then f inner: 
                less.append(item)                           # append item to less 
            elif f(item) == f(inner):                       # if function item is function inner 
                equal.append(item)                          # append to equal
            elif f(item) > f(inner):                        # if function item is larger then f inner: 
                greater.append(item)                        # greater append 
        return quicksort(less) + equal + quicksort(greater) # sort the (less), dont sort (equal) sort (greater) loop

    else: return db                                         # if lenght is less then 1 just return 

""" ------------------------------------------------------------------------------------------------------------------------------------ """

def main():
    data= [
            {'title': 'The Purge: Anarchy', 'director': 'James DeMonaco', 'score': 6.5}, 
            {'title': 'The Bunny Game', 'director': 'Adam Rehmeier', 'score': 3.6},
            {'title': 'Suicide Squad', 'director': 'David Ayer', 'score': 7.2},
            {'title': 'Ant-Man', 'director': 'Peyton Reed', 'score': 7.7}
    ]
    print(linear_search(data, 3.6, lambda e: e['score']))

    print(binary_search(data, 7.7, lambda e: e['score']))
    print(binary_search(data, 6.5, lambda e: e['score']))
    print(binary_search(data, 3.6, lambda e: e['score']))
    print(binary_search(data, 7.2, lambda e: e['score']))

    db = [
            ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
            ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
    ]
    
    print('\n')
    print('unsorted db (insertion_sort):')
    print('-' * 100)
    pprint(db)
    insertion_sort(db, lambda e: e[0])
    print('\n')
    print('sorted db (insertion_sort):')
    print('-' * 100)
    pprint(db)


    db = [
            ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
            ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
    ]

    print('\n')
    print('unsorted db (quicksort:)')
    print('-' * 100)
    pprint(db)
    db= quicksort(db, lambda e: e[1])
    print('\n')
    print('sorted db (quicksort:)')
    print('-' * 100)
    pprint(db)
        


if __name__ == '__main__': 
    main()
