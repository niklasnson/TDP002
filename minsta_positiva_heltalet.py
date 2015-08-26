# Ibland är det inte lika lätt att hitta ett intervall att iterera igenom. Istället får ni bestämma er för ett villkor som bara är sant när ni hittat rätt svar och sedan söka igenom ett mycket stort (ibland oändligt) intervall efter rätt svar.

# Det minsta positiva heltalet som är jämt delbart med siffrorna 1 till och med 10 är talet 2520. Er uppgift är att ta reda på vilket det minsta talet är som är jämt delbart med alla siffror från 1 till och med 13.

# Tips: För att kontrollera ifall ett tal är jämt delbart med ett annat använder ni er av operatorn modulo (%). Ifall resultatet av operationen är noll är talen jämt delbara med varandra.

# defintioner
is_done     = False
svar        = 0


# main - brutalforce
while is_done == False:
    svar = svar + 1
    is_done = True
    for number in range(1, 13):
        if svar % number != 0:
            is_done = False
print(svar)
