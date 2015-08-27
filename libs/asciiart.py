# Skriv en funktion frame som accepterar en textsträng som indata och skriver ut textsträngen inramad med asterisker.
def frame(text):
    text = "* " + text + " *"           # detta är texten med *
    print("*"*len(text))                # övre del som är lika lång som texten
    print(text)                         # texten
    print("*"*len(text))                # undedelen som är lika lång som texten

# Skriv en funktion triangle som accepterar ett heltal som indata och skriver ut en triangel av asterisker med den höjd som heltalet anger.
def triangle(num):
    for i in range(1,int(num) + 1):
        print("*"*i)

# Skriv en funktion flag som accepterar ett heltal som indata och skriver ut en flagga av asterisker 22 gånger bredare än den storlek som heltalet anger.
def flag(num):
    flag_width = (int(num) * 22)        # detta är den totala bredden av flaggan
    half_width = flag_width / 2         # detta är halva bredden
    print_flag(half_width)              # skriv ut den första delen av flaggan
    print(" ")                          # fyll på men en blankrad
    print_flag(half_width)              # skriv ut den nedre delen av flaggn

def print_flag(num):
    for i in range(1, 5):
        print("*"*int(num), end="")
        print(" ", end=" ")
        print("*"*int(num), end="\n")
