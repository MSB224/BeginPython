# declaration ou creation d'un dictionnaire

dico = {
    "nom":"balde",
    "prenom":"mamadou saliou",
    "Dreams":"IA"
}

# parcour ou affichage du dictioonaire
# la valeur des clés
# for elem in dico :
    
   #  print(dico[elem])
#    autre methode
# for elem,valeur in   enumerate(dico) :
#     print(f"{elem}->{valeur}")

# print(dico)
# # remove keys nom 
# dico.pop("nom")
# print(dico)

# # afters add keys nom in dico

# dico["name"] = "BALDE"

# print(dico)
# dico["name"] = "MSB"
# print(dico)

# Autre methode de parcour 
for keys,content in dico.items():
    print(f"{keys} : {content}")


 
   