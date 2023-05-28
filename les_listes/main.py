# creation d'une liste


maListe = [2,3,0]

print(maListe)
#ajout de nouvelle valeur dans le tableau

maListe.append(9)
print(maListe)
maListe.insert(1,"msb")
print(maListe)
maListe.remove("msb")
print(maListe)
if not "msb" in maListe:
    print("hello word")
else:
    print("Oops! sorry you have delete this")
#Passer d'une chaine a une list 
secondListe = "developpement Humm it's my dreams! "
secondListe = secondListe.split(" ")
print(secondListe)
