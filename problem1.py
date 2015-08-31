"""

    # läs in tal av användaren, avsluta med 0
    # lägg samman alla tal och retunera till användaren

"""

is_done          = False
sum_of_numbers   = 0


def adder(a, b):
    return a + b

def output(text):
    print(text)

while not is_done:
    if sum_of_numbers > 0:
        number = input("Mat in tal, avsluta med [0], summan är nu " + str(sum_of_numbers) + ": ")
    else:
        number = input("Mata in tal, avsluta med [0]: ")

    is_done = True

    if int(number) != 0:
        sum_of_numbers = adder(sum_of_numbers, int(number))
        is_done = False

output("summan av dina tal är " + str(sum_of_numbers))
