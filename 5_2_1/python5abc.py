"""-----------------------------------------------------------------------------------------------------------------"""

plus = lambda x, y: x + y
times = lambda x, y: x * y

from functools import reduce   # enda vettiga funktionen jag hittar för att köra i terminalen. men är inte aktuell i python 3.5 

"""-----------------------------------------------------------------------------------------------------------------"""

db = [
    {'name': 'Jakob', 'position': 'assistant'},
    {'name': 'Åke', 'position': 'assistant'},
    {'name': 'Ola', 'position': 'examiner'},
    {'name': 'Henrik', 'position': 'assistant'}
    ]

def dbsearch(db, column, value):
    """ search in db on column key and the value """
    return [item for item in db if item[column] == value]
    
"""-----------------------------------------------------------------------------------------------------------------"""

def contains(search, sentence):
    """ returns true/false if search is in sentence """
    return bool([word for word in sentence if search == word])

"""-----------------------------------------------------------------------------------------------------------------"""


def main(): 
    print(reduce(plus, range(1, 259)))
    print(reduce(times, range(1, 259)))
    # ---------------------------------------------------------------------------------------------------------------
    print(dbsearch(db, 'position', 'examiner'))
    # ---------------------------------------------------------------------------------------------------------------
    haystack = 'Can you find the needle in this haystack?'.split()

    print(contains('search', haystack))
    print(contains('needle', haystack))
    print(contains('haystack', haystack))

if __name__ == '__main__':
    main()
