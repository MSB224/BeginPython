# 1 les fonctions lambda

# ttc = lambda prixHT: prixHT + (prixHT * 20 / 100)

# print(ttc(24))

# hello = lambda:print("saliou")

# hello()


# 2 la modularité
# un module c'est un fichier  qui contient des fonctions exemple le module math
# # 3 façon d'importer un module 
# 1 import nom_module
# 2 from nom_module import nom_fonction(exemple from math import sqrt)
# 3 from nom_module import *(tout fonction qui se trouve au sein du module pourra etre utiliser)

# 

# from math import *

# a = int(input("saisir un nombre"))
# print(f"la racine de {a} est {sqrt(a)}")

import includes.boucles as bou

bou.parler("saliou","hello web!")

