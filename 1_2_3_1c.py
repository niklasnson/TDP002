# Ibland är det inte lika lätt att hitta ett intervall att iterera igenom. Istället får ni bestämma er för ett villkor som bara är sant när ni hittat rätt svar och sedan söka igenom ett mycket stort (ibland oändligt) intervall efter rätt svar.

# Det minsta positiva heltalet som är jämt delbart med siffrorna 1 till och med 10 är talet 2520. Er uppgift är att ta reda på vilket det minsta talet är som är jämt delbart med alla siffror från 1 till och med 13.

# Tips: För att kontrollera ifall ett tal är jämt delbart med ett annat använder ni er av operatorn modulo (%). Ifall resultatet av operationen är noll är talen jämt delbara med varandra.

# defintioner
is_done     = False
answer      = 0
try_num     = 13

# main - brutalforce
while not is_done:
    answer = answer + 1                     # addera 1 till svar
    is_done = True                          # vi är klara om inte:
    for number in range(1, try_num):             # för alla tal mellan 1-13
        if answer % number != 0:            # om det finns en rest
            is_done = False
            break                           # så är vi inte klara
print(answer)                               # skriv ut svar
