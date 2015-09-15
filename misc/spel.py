import random

comp_die = random.randint(1,6)
user_die = random.randint(1,6)

print("\n\n")
print("=========================================")
print("=                  kaBOM!               =")
print("=========================================")
print("\n\n")
print("Datorn slog: " + str(comp_die)) 
print("Du slog    : " + str(user_die))
print("----------------------------------------")
print("\n\n")
if comp_die > user_die:
    print('Datorn vann!')
elif comp_die < user_die: 
    print('Du vann!') 
else:
    print('Lika')
