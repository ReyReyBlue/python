# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi (ära kasuta max funktsiooni). 
# (loogikatehted - logic operators)

a = int(input('Anna number: '))
b = int(input('Veel üks number: '))
c = int(input('Üks number veel: '))

if a > b:
    if a > c:
        print(a, "on kõige suurem number")
    elif a == c:
       print(a)
    else:
       print(c, 'on kõige suurem number')

elif a == b:
    if a > c:
        print(a, "on kõige suurem number")
    elif a == c:
         print(a)
    else:
         print(c, 'on kõige suurem number')
else:
    if b > c:
        print(b, 'on kõige suurem number')
    elif b == c:
        print(b, 'on kõige suurem number')
    else:
        print(c, 'on kõige suurem number')