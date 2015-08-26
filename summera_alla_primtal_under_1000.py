# Ett primtal är ett naturligt tal som är större än 1 och jämt delbart endast med sig själv och med 1. Att avgöra ifall ett tal är ett primtal eller inte är väldigt kostsamt så ni bör därför tänka efter extra noga när ni formulerar er lösning så att ni inte kontrollerar tal som omöjligt kan vara primtal.

# Summan av alla primtal under 100 är 1060. Er uppgift är att ta reda på summan för samtliga primtal under 1000.

n = 100
primals = []
# skapa en lista med alla tal
for a in range(2, 101):
    primals.append(a)
# radera alla jämna tal
for a in primals:
    if a % 2 == 0 and a < 3:
        primals.pop(a)


print(primals)
