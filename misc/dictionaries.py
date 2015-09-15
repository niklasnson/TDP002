import libs.asciiart

libs.asciiart.frame("Dictonaries")
d = {'mat': 'Spam', 'antal': 4, 'färg': 'rosa'}
print('detta är hela vår tabell (dictonary)')
print(d)
print('-' * 110)
print('vi kan hämta ett speciellt värde med hjälp av en nyckel:')
print(str(d['antal']) + ' eller ' + d['färg'] )
print(d['antal'])
print('-' * 110)
d = dict(name='Niklas', job='dev', age=40) #genom att använda dict kan vi defienera listan på ett lite annat sätt. vi slipper att sätta '' på nycklarna.
print(d)
print('-' * 110)
d = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', '40'])) #genom att använda zip så kan vi sätta värdena så här. att observera är att vi kommer att få en annan ordning på nycklar än vad vi matar in.
print(d)
libs.asciiart.frame("Nesting dictonaries")
rec = {'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr'], 'age': 40.5}
print(rec)
print('-' * 110)
print(rec['name'])
print('-' * 110)
print(rec['name']['last'])
print('-' * 110)
print(rec['jobs'])
print('-' * 110)
print(rec['jobs'][-1])
print('-' * 110)
rec['jobs'].append('janitor')
print(rec)
print('-' * 110)
libs.asciiart.frame("Missing keys: if test's")
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
d['e'] = 99
print(d)
if not 'f' in d:                        # testa om det finns ett värde
    print('missing key')
value = d.get('x', 0)                   # sätt ett default värde om inte finns
print(value)                            # annars retuneras värdet

value = d['x'] if 'x' in d else 0       # eller så kan vi köra en if
print(value)
libs.asciiart.frame("Sorting keys")
d = {'a': 1, 'b': 2, 'c': 3}
ks = list(d.keys())
print(ks)
ks.sort()
print(ks)
print('-' * 110)
for key in ks:                          # gå genom och skriv ut alla nycklar
    print(key, '=>', d[key])            # och alla värden
print('-' * 110)
for key in sorted(d):                   # vi kan även sortera direkt i loopen
    print(key, '=>', d[key])

for c in 'spam':                        # loopa genom text
    print(c.upper())                    # sätt stor bokstav

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1                              # vi kan använda -= och +=

x = 1
while x <= 4:                           # lika med eller större!
    print('spam!' * x)
    x += 1
