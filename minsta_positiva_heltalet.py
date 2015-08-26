start_tal   = 1
slut_tal    = 10
produkt     = 0

while True:
    for number in range(start_tal, slut_tal):
        if start_tal % number != 0:
            break
        else:
            print(number)
    start_tal = start_tal + 1 # vill inte byta bort den här
    break # här kan man bryta loopen
