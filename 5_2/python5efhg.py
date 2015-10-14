from pprint import *

"""-----------------------------------------------------------------------------------------------------------------"""

def generate_list(operator, amount):
    return list(map(operator, range(1, amount + 1)))    # use the function at each index. 

"""-----------------------------------------------------------------------------------------------------------------"""

def partial(operator, amount):
    return lambda x: operator(amount, x)                # returns function with ammount as the first argument. 
                                                        # function filter [only the true values] with the result from first function (lambda x: x % 2 == 1 (odd numbers) 

"""-----------------------------------------------------------------------------------------------------------------"""

def compose(first_operator, second_operator):
    return lambda x: first_operator(second_operator(x)) # run the first operator with the result from the secound operator.  

"""-----------------------------------------------------------------------------------------------------------------"""

def make_filter_map(first_func, second_func):
    z = partial(filter, first_func)                     # filter returns the True values from the function  
    y = partial(map, second_func)                       # map runs the function on all values in the list

    return compose(list, compose(z, y))                 # sends result from first back to compose to get the list return and not the function.  

def main():

    process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x) 
    pprint(process(range(10)))

if __name__ == '__main__':
    main()
