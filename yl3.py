# yl3
# Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. Arvuta n + nn + nnn väärtus ja väljasta see.
# (Näiteks kui kasutaja sisestab 2, siis on vaja väljastada tulemus 2 + 22 + 222 = 246). Ära kasuta korrutamistehet. 
# Ülesanne on lahendatav ainult liitmise operaatorit kasuades.

a = (input('Kirjuta täisarv vahemikus 1-9: '))

b = (a+a)
b1 = int(b)

c = (a+a+a)
c1 = int(c)

a1 = int(a)

d1 = a1 + b1 + c1

print(a1, '+', b1, '+', c1, '=', d1)