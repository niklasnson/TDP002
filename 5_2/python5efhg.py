"""-----------------------------------------------------------------------------------------------------------------"""

def generate_list(operator, amount):
    return list(map(operator, range(1, amount + 1)))   # use the function at each index. 

"""-----------------------------------------------------------------------------------------------------------------"""

def partial(operator, amount):
    """ Skriv en funktion partial som tar en annan funktion och ett värde som indata. Partial ska returnera en ny funktion som gör samma sak som den angivna funktionen men där första argumentet till den angivna funktionen är bundet till det värde som angavs som andra argument till partial. """
    return lambda x: operator(amount, x) #  returns function with ammount as the first argument. 

"""-----------------------------------------------------------------------------------------------------------------"""

def compose(first_operator, second_operator):
    """ Skriv en funktion compose som tar två funktioner som argument, vi kallar dem Fa och Fb, och returnerar en funktion, Fres, som innebär att utdata från den andra funktionen blir indata till den första, dvs Fres(x) = Fa (Fb(x)). """
    return lambda x: first_operator(second_operator(x))

"""-----------------------------------------------------------------------------------------------------------------"""

def make_filter_map(first_func, second_func):
    """ Skriv en funktion make_filter_map som tar en filter-funktion och en map- funktion som argument. Funktionen ska returnera en funktion som tar en lista som argument och applicerar map-funktionen på varje element i listan som filter- funktionen är sann för. make_filter_map ska använda funktionerna partial och compose från tidigare uppgifter för att sätta ihop funktionerna map och filter med indatafunktionerna till det önskade resultatet."""""
    
    # ex körning: process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)
                                            # första funktionen   # andra funktenen
                                            # om resten av %2 == 1  andra funtionen  x * x 
    z = partial(filter, first_func)   # retunera första funktionen med  
    y = partial(map, second_func)     # 
        # sen körs partial som retunerar operator med värdet som argument

    return compose(list, compose(z, y))
    
    # ex körning: process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)

    # filter tar en function och en lista och retunerar true|false (vilket här ger tal som är ojämna, ej tar som är delbara med 2 
    # retunerar en lista med de värden som är True. 
    
    # ger oss en lista med tal som är ojämna. 

    # map tar en funktion och en sekvens (lista) och applicerar funktionen på alla världen in listan 
    # ger oss ex 1 * 1, 3 * 3, 5 * 5 etc 

    # compose använder vi för att skicka in de två funktionerna och sedan köra den första funktionen på den andra funktionens, (endast tal som inte är delbara med 2). 
    # för att få en lista så skickar jag in funktionen i sig själv och skapar en lista av resultaten. 

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
