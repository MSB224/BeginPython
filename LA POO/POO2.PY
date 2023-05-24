#  Methode             function sur une instance
# Methode de classe    :function sur une classe
# Methode static      :funtion independant mais lié à une classe

# definition de la class Personne

class Personne:
     ageUnitial = 0;
     def __init__(self,nom,prenom) :
          self.nom    = nom
          self.prenom = prenom
# creation d'une methode
     def afficher(self):
           print(f"Bonjour {self.nom} {self.prenom}")
# Methode de classe
    
     def YearOfBrith(cls,nouvelleAgeInitial):
          Personne.ageUnitial = nouvelleAgeInitial
          
     YearOfBrith =  classmethod(ageUnitial)     
        
        #   begin program main
# personne("Balde","Mamadou saliou")
# personne.afficher()
print(f"l'age initial de la personne actuellement est {Personne.ageUnitial}")
Personne.YearOfBrith = 12
print(f"en utilisans la methode de class on obtient\n quel'age initial de la personne actuellement est {Personne.YearOfBrith}")