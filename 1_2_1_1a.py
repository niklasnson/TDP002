# Ofta när ni utför beräkningar kommer ni i förväg att kunna räkna ut vilket intervall ni måste gå igenom för att komma fram till svaret. Då är en iteration att föredra eftersom ni med säkerhet kan säga att inga yttre faktorer kommer att påverka resultatet.
# Naturliga tal är de heltal som inte är negativa, det vill säga alla tal från 0 och uppåt. Om ni summerar alla naturliga tal upp till och med 128 får ni summan 8256. Er uppgift är att ta reda på vad summan för alla naturliga tal upp till och med 512 är för något.

summa   = 0
lower   = 0
upper   = 512 # input("max tal?: ")

while lower < upper:
    summa = summa + lower
    lower = lower + 1
print(summa)
