"""

    konversation av strängar

"""

print(str('spam'), repr('spam'))  #skapar en stäng som kan återanvändas
print(repr('spam'))

print(ord('s'))                  # ASCII value av s
print(chr(115))                 # skriv ut tecken som har ASCII värde

text = "foobar Fobar FOOBAR"
print(text.capitalize())        # stor bokstav i början
print(text.casefold())
print(text.center(100))
