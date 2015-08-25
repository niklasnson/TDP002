import random
i = 1 
list = []
while i < 100: 
    value = random.randint(1,100)
    if value not in list:
        list.append(value) 
        i = i + 1
list.sort()
print(list)
