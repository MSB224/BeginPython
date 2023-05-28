#creation d'une liste d'abord

# liste = ["naitre","grandir","reproduire","viellir","mourir"]

# for element,valeur in enumerate(liste):
#     print(f"{element}->{valeur}")
   
#-----------------------------

def return_deux_valeur():
    val1 = 245857
    val2  = 1958
    
    return (val1,val2)

# in programme main

a = 0
b = 0

print (f"les deux valeur sont {a} et {b}")
#appel de la fonction

(a,b) = return_deux_valeur()

print (f"les deux valeur sont {a} et {b}")
