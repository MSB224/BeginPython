class Hummain:
   def __init__(self,nom, prenom) :
      print("La creation du premier objet Hummain...")
      self._nom = nom
      self._prenom = prenom

   def _getnom(self) :
      print("warning acces interdit")
#   notion de getters and setters
   nom = property(_getnom)


# programme main()

h1 = Hummain("balde","mamadou saliou")
print("-------Premier extenciation--------")
print(h1.nom)
print("-------second extenciation--------")
