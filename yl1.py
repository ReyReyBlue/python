# yl1
# Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa'
#  eurodesse ja väljastab ümardatud tulemuse. (round)

# küsime kasutajalt summa kroonides
# teisendame eurodesse
# väljastame tulemuse

a = int(input('Sisesta summa kroonides: '))
b = (a / 15.6466)
print('Sinu summa eurodes', round(b, 2 ))
