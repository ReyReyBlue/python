# Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi (ära kasuta min funktsiooni). 
# (muutuja - variable, tingimus - condition, if-lause - if statement)
# float toimib komaga arvude puhul

a = int(input('Anna number: '))
b = int(input('Anna veel üks number: '))

if b > a:
  print(a, "on väikseim antud numbritest")
elif a == b:
  print(a)
else:
  print(b, "on väiksem antud numbritest")