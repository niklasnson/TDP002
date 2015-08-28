num_list    = [1,2,3,4,5,6,7,8,9,10]
string_list = ['detta', 'är', 'en', 'lång', 'lista', 'med', 'ord']


print('summan av num_list är: ', sum(num_list) )
print('det första värdet i listan är: ', num_list[0]) # vi börjar på 0!
print('det sista värdet i listan är: ', num_list[9]) # och slutar på 9!

print('alla värden i num_list är:', end=' ')
for i in num_list:
    print(i, end=' ')                                # space mellan varje tal
print('')                                            # vi vill ha ny rad
print('lägger vi till talet [20] så får vi en ny summa: ', end='')
num_list.append(20)
print(sum(num_list), end='\n')
print('vi kan använda pop för att lästa det ´nthe värdet endast: ', end='')
print(num_list.pop(0))

print('\nsträngar i listor:\n')
print('Listan till att börja med: ', string_list)
print('Sortera stängen: ', end='')
string_list.sort()                                  # sort ersätter string_list
print(string_list)
print('Eller kör den baklänges: ', end='')
string_list.reverse()                               # reverse ersätter string_list
print(string_list)

print('Vi kan göra listor i listor:', end='')
combined_list=[num_list, string_list]
print(combined_list)
print('och då utföra kommandon på en av deltagarna: ', end='')
print(combined_list[0])
print('eller ta bort ett av elmenten: ', end='')
print(combined_list.pop(1))
