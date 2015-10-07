"""-----------------------------------------------------------------------------------------------------------------"""

def generate_list(operator, amount):
    return list(map(operator, range(1, amount + 1)))

"""-----------------------------------------------------------------------------------------------------------------"""

def partial(operator, amount):
    return lambda x: operator(amount, x)

"""-----------------------------------------------------------------------------------------------------------------"""

def compose(first_operator, second_operator):
    return lambda x: first_operator(second_operator(x))

"""-----------------------------------------------------------------------------------------------------------------"""

def make_filter_map(first_filter, second_filter):
    z = partial(filter, first_filter)
    y = partial(map, second_filter)

    return compose(list, compose(z, y))

def main(): 
      print("run in console!")

if __name__ == '__main__':
    main()
