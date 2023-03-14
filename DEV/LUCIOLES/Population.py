#import de la classe luciole du fichier luciole
from Luciole import Luciole

#création de la classe Population 
class Population:
    #définition du constructeur
    def __init__(self, nb_luciole: int):
        self.luciole = []
        for i in range(nb_luciole):
            self.luciole.append(Luciole.creerLuciole())
    #Getter Luciole
    def Getluciole(self):
        return self.luciole

    #Setter Luciole
    def Setluciole(self, v):
        self.luciole = v