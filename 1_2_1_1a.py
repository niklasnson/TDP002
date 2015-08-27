# Ofta när ni utför beräkningar kommer ni i förväg att kunna räkna ut vilket intervall ni måste gå igenom för att komma fram till svaret. Då är en iteration att föredra eftersom ni med säkerhet kan säga att inga yttre faktorer kommer att påverka resultatet.

# Naturliga tal är de heltal som inte är negativa, det vill säga alla tal från 0 och uppåt. Om ni summerar alla naturliga tal upp till och med 128 får ni summan 8256. Er uppgift är att ta reda på vad summan för alla naturliga tal upp till och med 512 är för något.

# defintioner
summa   = 0
lower   = 0
upper   = 512

# main
for i in range(lower, upper + 1):       # för alla tal i in range (upper + 1)
    summa = summa + i                   # summa är lika med summa plus 1

print(summa)                            # skriv ut summa!
