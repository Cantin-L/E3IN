#Importation du module random pour la création de valeur random dans nos arbres
import random

#Création de la classe ABR
class ABR:
    def __init__(self, racine=0, gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    #Création des getter de la classe ABR
    def get_droite(self):
        return self.droite
    def get_gauche(self):
        return self.gauche
    def get_racine(self):
        return self.racine
    
    #Création des setter de la classe ABR
    def set_gauche(self, gauche):
        self.gauche = gauche
    def set_droite(self, droite):
        self.droite = droite
    def set_racine(self, racine):
        self.racine = racine

    #Création de la fonction qui détermine si l'arbre est vide
    def estvide(self):
        if self.racine == 0:
         return True 
        else:
            return False 

    #Création de la fonction qui détermine le prefixe de l'arbre
    def prefixe(self):
        if (self.estvide()):
            return ""
        else:
            if self.gauche == None and self.droite == None:
                return str(self.racine)
            elif self.gauche == None:
                return str(self.racine) +" " +self.droite.prefixe()
            elif self.droite == None:
                return str(self.racine) + " "+self.gauche.prefixe()

            else :
                return str(self.racine) + " "+self.gauche.prefixe()+" " +self.droite.prefixe()
            
    #Création de la fonction qui détermine le infixe de l'arbre
    def infixe(self):
        if(self.estvide()):
            return ""
        else:
            if self.gauche == None and self.droite == None:
                return str(self.racine)
            elif self.gauche == None:
                return str(self.racine) +" " + self.droite.infixe()
            elif self.droite == None:
                return self.gauche.infixe()+" "+ str(self.racine) 
            else :
                return self.gauche.infixe()+" " +str(self.racine)+" " +self.droite.infixe()
            
    #Création de la fonction qui détermine le postfixe de l'arbre
    def postfixe(self):
        if(self.estvide()):
            return ""
        else:
            if self.gauche == None and self.droite == None:
                return str(self.racine)
            elif self.gauche == None:
                return self.droite.postfixe()+" " + str(self.racine)
            elif self.droite == None:
                return str(self.racine) + " "+self.gauche.postfixe()
            else :
                return self.gauche.postfixe()+" " +self.droite.postfixe()+" " +str(self.racine)
                
    #Création de la fonction qui détermine la taille de l'arbre
    def taille(self):
        if(self.estvide()):
            return 0
        else:
            if self.gauche == None and self.droite == None:
                return 1
            elif self.gauche == None:
                return 1+self.droite.taille()
            elif self.droite == None:
                return 1+self.gauche.taille()
            else:
                return 1+self.gauche.taille()+self.droite.taille()

    #Création de la fonction qui détermine la hauteur de l'arbre
    def hauteur(self):
        if(self.estvide()):
            return -1 
        else:
            if self.gauche == None and self.droite == None:
                return 0
            elif self.gauche == None:
                return 1 + self.droite.hauteur()
            elif self.droite == None:
                return 1+ self.gauche.hauteur()
            
            else:
                if self.droite.hauteur() > self.gauche.hauteur():
                    return 1+ self.droite.hauteur()

                else:
                    return 1 + self.gauche.hauteur()


#Création des valeurs aléatoires de l'arbre
a = random.randint(1,20)
b = random.randint(1,20)
c = random.randint(1,20)
d = random.randint(1,20)

#création des différents arbres
Arbre1 = ABR(a,None,None)
Arbre2 = ABR(b,None,None)
Arbre3 = ABR(c,Arbre1,Arbre2)
Arbre4 = ABR(d,Arbre3,Arbre3)

#Application des fonctions sur l'arbre 
print(Arbre4.prefixe())
print(Arbre4.postfixe())
print(Arbre4.infixe())
print(Arbre4.taille())
print(Arbre4.hauteur())