#import du module random pour créer des valeurs aléatoires
import random

#définition du SEUIL à 50 en variable globales pour pouvoir le modifier 
SEUIL = 50

#création de la fonction symbolise luciole
def symboliseLuciole(niveauEnergie: float):
    if niveauEnergie >= SEUIL:
        return '*'
    else:
        return '.'

#création de la fonction affiche luciole
def afficheLuciole(niveauEnergie: float, verbeux: bool):
    symbol = symboliseLuciole(niveauEnergie)
    print(symbol, end=' ')
    if verbeux:
        print("(niveau d'énergie: {})".format(niveauEnergie))
    print()
    
#création de la fonction incremente luciole
def incrementeLuciole(niveauEnergie: float, deltaEnergie: float):
    return (niveauEnergie + deltaEnergie)

#création de la fonction simulation du niveau d'énergie à une nombre de pas définit
def simuleLucioleNbPas(nbPas: int,lucioleEnergie: float,lucioleDeltaEnergie: float):
    for i in range(nbPas):
        lucioleEnergie = incrementeLuciole(lucioleEnergie, lucioleDeltaEnergie)
        if lucioleEnergie >= 50:
            afficheLuciole(lucioleEnergie, True)
            lucioleEnergie = 0
        afficheLuciole(lucioleEnergie, False)
    
#création de la focntion Flash
def simuleLucioleNbFlashs(lucioleEnergie: float,lucioleDeltaEnergie: float):
    flash_count = 0
    while flash_count < 3:
        lucioleEnergie = incrementeLuciole(lucioleEnergie, lucioleDeltaEnergie)
        if lucioleEnergie >= 50:
            afficheLuciole(lucioleEnergie, True)
            lucioleEnergie = 0
            flash_count += 1
        else :
            afficheLuciole(lucioleEnergie, False)

#création de la fonction main
def main():
    lucioleEnergie = random.uniform(0, 100)
    lucioleDeltaEnergie = random.uniform(0, 1)
    simuleLucioleNbFlashs(lucioleEnergie,lucioleDeltaEnergie)

#appel de la fonction main
main()