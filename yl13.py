pet = input('give me a pet: ') #Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
print(pet[0])

mylist = ["chicken", "pig", "cow"] #Koosta list, mis koosneb kolmest loomast.

mylist.append(pet) #Lisa selle listi lõppu kasutaja sisestatud lemmikloom.

print(mylist) #Väljasta see lemmikloomade list.

print(mylist[-1][-1]) #Väljasta listi viimase elemendi viimane täht.
 #(sõne kui list, mitmemõõtmeline ilist - multi dimensional)
