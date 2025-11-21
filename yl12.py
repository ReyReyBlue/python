
mylist = ["apple", "banana", "cherry"] #Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
print(mylist)

print(mylist[0]) #Väljasta listi esimene väärtus

mylist.append("orange") #Lisa listi lõppu uus puuvili

print(mylist[-1]) #Väljasta listi viimane väärtus

mylist[1] = "blackcurrant" #Muuda ühe elemendi väärtust ja väljasta kogu list
print(mylist)

if "apple" in mylist: #Kontrolli kas väärtus (näiteks õun) eksisteerib listis
  print("yes, apple is in the list")

print(len(mylist)) #Väljasta listi pikkus

mylist.remove("apple") #Eemalda listist element ja väljasta kogu list
print(mylist)

mylist.sort(reverse=True)   #Muuda listi järjekord vastupidiseks
print(mylist)               #Sorteeri list ja väljasta
                            #(jada, list, listi element, listi meetodid)
print(mylist[2:5])