"""
    tupler kan inte få nya värden efter att dom är satta. så varför använda
    tupler i stället för en lista? just för att dom inte går att ändra till,
    dom är på detta sätt skriv skyddade även om du använder dom i andra
    funktioner. värdet kommer alltid vara det samma som du började på.
"""

t = (1,2,3,4)
print(len(t))               # längden av listan
print(t + (5,6))            # addera men spara inte
t += (5,6)                  # addera och spara
print(t)
print(t[0])                 # vad finns det för värde på position 0
print(t.index(4))           # vilken position har värdet 4
print(t.count(4))           # hur många gånger finns värdet 4
