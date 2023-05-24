class Etudiants:
     def __init__(self,nom,age):
          self.nom = nom
          self._age = age
     
     def _setage(self,nouvelle_age):
          nouvelle_age = int(nouvelle_age)
          if nouvelle_age <0:
               print("l'age ne peut etre negatif nous allons la mettre a 0")
               self._age = 0
          else:
               self._age = nouvelle_age
     def _getage(self):
          return self._age
          
     age =  property(_getage,_setage)
     

    #  program main

etu1 = Etudiants("balde",-5)
print("LES INFORMATIONS DE L'ETUDIANT 1 EST ")

print(etu1.age)

age = input("Donner une autre valeur de l'age")
etu1.age = age
print(etu1.age)