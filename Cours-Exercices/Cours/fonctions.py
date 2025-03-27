# Fichier d'exemples pour les fonctions

# Ecrire une fonction basique
from unittest import result


def fonction1():
    print("je suis une fonction")

# Variables locales et variables globales
varg = 5

def uneFonction():
    varg = 10
    print(varg)

uneFonction()
print(varg)

# Fonction qui prend plusieurs arguments
def fonction2(arg1, arg2):
    print(arg1, arg2)

# Fonction qui retourne une valeur
def cube(x):
    return x ** 3

# Fonction avec une valeur par défaut dans ses arguments
# (arguments nommés permet aussi d'envoyer dans le désordre)
def puissance(num, x=1):
    resultat = num

    for _ in range(1, x):
        resultat *= num
    
    return resultat

# Fonction avec un nombre variable d'arguments
def argsMultiple(*args):
    resultat = 0

    for x in args:
        resultat += x
    
    return resultat

# Argument nommé obligatoire
def uneFonctionSup(num=1, x=1, *_, valide=True):
    # Test si valide est booléen
    if isinstance(valide, bool) == False:
        print("valide n'est pas un booléen !")
        return -1
    
    if valide == True:
        return num + x
    else:
        return 0

def fonction3(*liste, **dico):
    pass


# Fonction principale
def main():
    fonction1()
    fonction2(15, 48)
    print(cube(5))
    print(puissance(2, 15))
    print(puissance(x=15, num=2))
    print(argsMultiple(5, 2, 7, 8, 10, 15))
    print(uneFonctionSup(1, 2, valide=True))
    print(fonction3(1, 2, 3, 5, 78, "toto", num=5, toto=18, fifi="fifi"))



# Appel fonction principale
if __name__ == "__main__":
    main()