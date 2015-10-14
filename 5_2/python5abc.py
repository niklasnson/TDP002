from functools import reduce  

"""-----------------------------------------------------------------------------------------------------------------"""

plus = lambda x, y: x + y
times = lambda x, y: x * y

def operations(operator, ammount):
    return reduce(operator, ammount)                            # reduce takes a function and an ammount and outputs single value

"""-----------------------------------------------------------------------------------------------------------------"""

db = [
    {'name': 'Jakob', 'position': 'assistant'},
    {'name': 'Åke', 'position': 'assistant'},
    {'name': 'Ola', 'position': 'examiner'},
    {'name': 'Henrik', 'position': 'assistant'}
    ]

def dbsearch(db, column, value):
    """ search in db on column key and the value """
    return [item for item in db if item[column] == value]       # l/c

    ## l/c
    ##
    ##
    ##
    ##    
"""-----------------------------------------------------------------------------------------------------------------"""

def contains(search, sentence):
    """ returns true/false if search is in sentence """
    return bool([word for word in sentence if search == word])  # l/c => bool (true if [] has value

"""-----------------------------------------------------------------------------------------------------------------"""

def main(): 
    print(operations(plus, range(1, 259)))
    print(operations(times, range(1, 259)))  # reduce tar en funnktion och en sekvens som invärde och retunerar ett ensamt värde
    # ---------------------------------------------------------------------------------------------------------------
    print(dbsearch(db, 'position', 'examiner'))
    # ---------------------------------------------------------------------------------------------------------------
    haystack = 'Can you find the needle in this haystack?'.split()

    print(contains('search', haystack))
    print(contains('needle', haystack))
    print(contains('haystack', haystack))

if __name__ == '__main__':
    main()
