# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

# küsime kasutajalt raadiuse
# teeme tehted
# väljastame ringi pindala ja ümbermõõdu

a = int(input('Anna mulle ringi raadius!: '))
import math

s = math.pi * (a * a)
c = math.pi * a * 2
print('Ringi pindala on', round (s, 3))
print('Ringi ümbermõõt on', round (c, 3))