"""
    filer
"""

f = open('data.txt', 'w')           # öppna filen // med rättigheter!
f.write('Hello\n')                  # skriv till filen
f.write('Hello\n')                  # -------""-------
f.close()                           # stäng filen

f = open('data.txt')                # öppna filen // bara för att läsa
text = f.read()                     # läs in vad som finns till EOF
print(text)                         # skriv ut variablen!

print(text.split())                 # skriv ut som splittad till []

for line in open('data.txt'): print(line)  # snyggare linje
