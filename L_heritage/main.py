# une classe mere vehicule

class Vehicule:
      
 def __init__(self,m_marque,m_nombreVitesse):
              self.marque = m_marque
              self.qEssence = m_nombreVitesse
 def frainner(self):
       print(f"Oops ! l' automobile  { self.marque} vien de frainner")              

   # une classe fille qui herite de la classe mere
class Voiture(Vehicule):
   def __init__(self,m_marqueVoiture,m_nombreVitesseVoiture,m_nombrePlaceVoiture):
         Vehicule.__init__(self,m_marqueVoiture,m_nombreVitesseVoiture)
         self.nbrePlaceVoiture = m_nombrePlaceVoiture

         
       
# dans notre programme principal


print("extension la class fille")
v2 = Voiture("ferrari",8,58)
print(v2.marque)
v2.frainner()

 
