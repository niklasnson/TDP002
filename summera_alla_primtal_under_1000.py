# Ett primtal är ett naturligt tal som är större än 1 och jämt delbart endast med sig själv och med 1. Att avgöra ifall ett tal är ett primtal eller inte är väldigt kostsamt så ni bör därför tänka efter extra noga när ni formulerar er lösning så att ni inte kontrollerar tal som omöjligt kan vara primtal.

# Summan av alla primtal under 100 är 1060. Er uppgift är att ta reda på summan för samtliga primtal under 1000.

lower = 0
upper = 1000
primes = []

for num in range(lower,upper + 1):
    if num > 1:                              # ett primtal är sörre än 1
        for i in range(2,num):               # för alla i med start 2 till num
           if (num % i) == 0:                # om num är delbart
               break                         # inte ett primtal
        else:
           primes.append(num)                # lägg till som primtal

print("Summan av primtalen mellan {} och {} är {}".format(lower, upper, sum(primes)))
