def frame(text):
  """
  Skriv en funktion frame som accepterar en textsträng som indata och skriver ut 
  textsträngen inramad med asterisker. 
  """
  text = "* " + text + " *"           # texten med inledande * och avslutande * 
  print_stars(len(text))
  print(text)                         # texten
  print_stars(len(text))

def triangle(num):
  """
  Skriv en funktion triangle som accepterar ett heltal som indata och skriver 
  ut en triangel av sterisker med deb höjd som heltalet anger.
  """
  num = num + 1                      # eftersom vi vill skriva ut hela antalet av num
  for i in range(1,int(num)):        #  i range loopen
    print_stars(i)

def flag(num):
  """
  Skriv en funktion flag som accepterar ett heltal som indata och skriver ut 
  en flagga av aserisker 22 gånger bredare än den storlek som heltalet anger,
  """
  flag_width = (int(num) * 22)            # detta är den totala bredden av flaggan
  print_square(flag_width/2) 
  print_space()                           # skriv ut en blankrad mellan de två delarna
  print_square(flag_width/2)              # skriv ut den nedre delen av flaggn
  
def print_square(num):
  """
  Skriver ut en del av flaggan
  """
  for i in range(1, 5):                   # flaggan skall vara 4 rader hög 
    print("*"*int(num), end="")           # vänstra delen av flaggan
    print(" ", end=" ")                   # skriv ut ett mellarum mellan delarna 
    print("*"*int(num), end="\n")         # högra delen av flaggan


def print_stars(num=1):
  """
  Skriver ut stjärnor.
  """
  for i in range(num):
    print('*', end='')
  print()                                 # avsluta med ny rad

def print_space(): 
  """
  Skriver ut en blankrad
  """
  print('')
