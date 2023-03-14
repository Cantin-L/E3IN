#import du module random pour créer des valeurs aléatoires
import random

#création de la classe Luciole
class Luciole:

    #définition du SEUIL à 50 en variable globales pour pouvoir le modifier 
    SEUIL = 50

    #définition du constructeur
    def __init__(self, e: float, d: float):
        self.energie = e
        self.delta = d

    #Getter Energie
    def Getenergie(self):
        return self.energie

    #Setter Energie
    def Setenergie(self, v: float):
        self.energie = v

    #Getter Delta
    def Getdelta(self):
        return self.delta

    #Setter Delta
    def Setdelta(self, v: float):
        self.delta = v

    #création de la méthode symbolise luciole
    def symboliseLuciole(self):
        if self.energie >= Luciole.SEUIL:
            return '*'
        else:
            return '.'

    #création de la méthode symbolise luciole
    def afficheLuciole(self, verbeux=False):
        symbol = self.symboliseLuciole()
        print(symbol, end=' ')
        if verbeux:
            print("(niveau d'énergie: {})".format(self.energie))
        print()

    #création de la méthode imcrémente luciole
    def incrementeLuciole(self):
        self.energie += self.delta

    #création de la méthode créer luciole
    @staticmethod
    def creerLuciole():
        energie = random.uniform(0, 100)
        delta = random.uniform(0, 1)
        return Luciole(energie, delta)

    #création de la méthode simule luciole nbPaas
    def simuleLucioleNbPas(self, nbPas: int):
        for i in range(nbPas):
            self.incrementeLuciole()
            if self.energie >= 50:
                self.afficheLuciole(True)
                self.energie = 0
            self.afficheLuciole(False)