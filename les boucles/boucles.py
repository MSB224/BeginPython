# compteur = 0

# while compteur < 10 :

#     print("bonjour vous devez choisir de plus")
#     compteur+=1


def parler(personnage,message):
    print(f"{personnage} : {message}")

def aurevoir():
    print("autres fois")

# PHASE DE TESTE DE NOTRE MODULE CONSEILLER POUR CHAQUE MODULE AVANT DE L'INTEGRER  DANS LE FICHIER PRINCIPAL

if __name__ == "__main__":

    print("PHASE DE TEST DE NOTRE MODUL BOUCLES")
    parler("bonjour","je vous salut")