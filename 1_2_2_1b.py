# I denna uppgift ska ni använda er av samma kod som ni skrev i föregående uppgift men nu ska ni göra små ändringar så att ni räknar ut produkten istället för summan.
# Produkten för alla positiva heltal upp till och med 12 är 479001600, produkten för alla positiva heltal upp till och med 512 kommer således bli ett fruktansvärt stort tal.

lower   = 1
upper   = 512
summa   = 1

for i in range(lower, upper + 1):     # eftersom range annars inte kör sista.
    summa = summa * i                 # summan är lika som summa * akt talk.

print(summa)                          # skriv ut summan
