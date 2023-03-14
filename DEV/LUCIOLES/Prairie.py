#import du module random pour créer des valeurs aléatoires
import random

#définition du SEUIL à 50 en variable globales pour pouvoir le modifier 
SEUIL = 50

#création de la fonction créer lucioles
def creerLuciole():
    niveauEnergie = random.randint(0, 100) 
    LucioleDeltaEnergie = random.uniform(0, 1)            
    return [niveauEnergie, LucioleDeltaEnergie]          

#création de la fonction incremente luciole
def incrementeLuciole(Luciole):             
    Luciole[0] = Luciole[0]+Luciole[1]      
    if Luciole[0] < 0:                      
        Luciole[0] = 0                      
    elif Luciole[0] > 100:                  
        Luciole[0] = 100                    

#création de la fonction créer population
def creerPopulation(nbLucioles):
    Population = []
    for i in range(nbLucioles):
        Population.append(creerLuciole())
    return Population

#création de la fonction prairie vide
def prairieVide(nbLignes, nbColonnes):
    Prairie = []
    for i in range(nbLignes):
        ligne = []
        for j in range(nbColonnes):
            ligne.append(None)
        Prairie.append(ligne)
    return Prairie

#affiche une prairie en fonction de la prairie et de la population
def affichePrairie(Prairie, Population):
    nb_lignes = len(Prairie)
    nb_colonnes = len(Prairie[0])
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if i == 0 or i == nb_lignes-1 or j == 0 or j == nb_colonnes-1:
                print("#", end="")
            elif Prairie[i][j] is None:
                print(" ", end="")
            else:
                Luciole = Population[Prairie[i][j]]
                if Luciole[0] > SEUIL :
                    print("*", end="")
                else:
                    print(".", end="")
        print()

#Création d'une prairie vide et placement aléatoire des lucioles
def PrairieLucioles(nbLignes, nbColonnes, Population):
    Prairie = prairieVide(nbLignes, nbColonnes)
    for i in range(len(Population)):
        x = random.randint(1, len(Prairie)-2)
        y = random.randint(1, len(Prairie[0])-2)
        while Prairie[x][y] is not None:
            x = random.randint(1, len(Prairie)-2)
            y = random.randint(1, len(Prairie[0])-2)
        Prairie[x][y] = i
    return Prairie

#simulation prairie
def simulationPrairie(nbPas, Population):
    Prairie = PrairieLucioles(10,10, Population)
    for i in range(nbPas):
        for i in range(len(Population)):
            incrementeLuciole(Population[i])
    affichePrairie(Prairie, Population)

#création de la fonction main
def main():
    Population = creerPopulation(10)
    simulationPrairie(2, Population)
   
#appel de la fonction main
main()