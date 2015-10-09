"""-----------------------------------------------------------------------------------------------------------------"""

def generate_list(operator, amount):
    return list(map(operator, range(1, amount + 1)))

"""-----------------------------------------------------------------------------------------------------------------"""

def partial(operator, amount):
    return lambda x: operator(amount, x)
    """ Skriv en funktion partial som tar en annan funktion och ett värde som indata. Partial ska returnera en ny funktion som gör samma sak som den angivna funktionen men där första argumentet till den angivna funktionen är bundet till det värde som angavs som andra argument till partial. """

"""-----------------------------------------------------------------------------------------------------------------"""

def compose(first_operator, second_operator):
    """ Skriv en funktion compose som tar två funktioner som argument, vi kallar dem Fa och Fb, och returnerar en funktion, Fres, som innebär att utdata från den andra funktionen blir indata till den första, dvs Fres(x) = Fa (Fb(x)). """
    return lambda x: first_operator(second_operator(x))

"""-----------------------------------------------------------------------------------------------------------------"""

def make_filter_map(first_filter, second_filter):
    """ Skriv en funktion make_filter_map som tar en filter-funktion och en map- funktion som argument. Funktionen ska returnera en funktion som tar en lista som argument och applicerar map-funktionen på varje element i listan som filter- funktionen är sann för. make_filter_map ska använda funktionerna partial och compose från tidigare uppgifter för att sätta ihop funktionerna map och filter med indatafunktionerna till det önskade resultatet."""""
    
    z = partial(filter, first_filter)
    y = partial(map, second_filter)

    return compose(list, compose(z, y))

def main(): 
      print("run in console!")

      """
        >> def mirror(x): return x
        >> python5efhg.generate_list(mirror, 4)

        >> def stars(n): return '*' * n
        >> python5efhg.generate_list(stars, 5)

        >> def add(n, m): return n + m
        >> add_five = python5efhg.partial(add, 5)
        >> add_five(3)

        >> def multiply_five(n):
        >>     return n * 5
        >> def add_ten(x):
        >>     return x + 10
        >> composition = compose(multiply_five, add_ten)
        >> composition(3)

        >> another_composition = compose(add_ten, multiply_five)
        >> another_composition(3)
        
        >> process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x) 
        >> process(range(10))
      """

if __name__ == '__main__':
    main()
