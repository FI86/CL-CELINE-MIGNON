# Fichier d'exemples pour les collections

# LISTES
# Déclarer une liste avec la possibilité de modifier son contenu
from re import M


maliste = [0, 1, 1, 2, 2, 3, 5, 8, 13]
print(maliste)

# J'accède au 7e élément de la liste (les index commencent à 0)
print(maliste[6])

# Je retire le 5e élément de la liste et retourne l'element supprimé
print(maliste.pop(4))
print(maliste)

# J'ajoute un élément à la fin
maliste.append(21)
print(maliste)
# Ou
maliste += [12]
print(maliste)

# Ajouter un element a un index spécifique
maliste.insert(8, 15)
print(maliste)

# J'extrais les éléments de la position 3 jusqu'à la fin de la liste
print(maliste[2:])

# J'extrais les deux premiers éléments
print(maliste[:2])

# J'extrais du 4eme éléments au 6eme inclus (les index commencent à 0)
print(maliste[3:6])

# J'extrais du 4eme éléments au 6eme inclus de 2 en 2 (les index commencent à 0)
print(maliste[3:6:2])

# J'extrais le dernier élément de la liste
print(maliste[-1])

# Quelle est la longueur de ma liste ?
print(len(maliste))

# Je modifie un élément (celui qui est en 3e position)
maliste[2] = 8
print(maliste)

# SERIE DE FONCTION SUR LES LISTES
# Supprime le premier élément trouvé avec la valeur indiquée dans les ()
print(maliste.remove(1))
print(maliste)

# Suppression par index de la liste mais ne retourne pas la valeur supprimée
del maliste[0]
print(maliste)

# Nombre d'occurences correspondantes dans la liste.
print(maliste.count(8))

# Retourne l’index d’une valeur 
print(maliste.index(12))

# Inverse la liste
maliste.reverse()
print(maliste)

# Type d'une liste
print(type(maliste))

# Listes imbriquées
ma_liste_imbrique = [1, [5, 6, 7], 2, 3]
print(ma_liste_imbrique)
print(ma_liste_imbrique[1][2])

# COPIER UNE LISTE
# Copie par référence (agit comme un alias de la première liste)
y = [1, 2, 3]
x = y
y[0] = 4
print(x)

# Copie par valeur
x = [1, 2, 3]
y = x[:]
x[0] = 15
# Ou
y = x.copy()
x[0] = 45
y[0] = 44
print(x, y)

# Transformation String en liste
ma_chaine = "Xavier:Tabuteau:Poitiers"
print(ma_chaine.split(":"))

# Transformation liste en string
ma_liste = ['Xavier', 'Tabuteau', 'Poitiers']
print(" - ".join(ma_liste))

# Extension de liste
ma_liste = ['Xavier', 'Tabuteau']
ma_liste2 = ['Ici', "Poitiers"]
ma_liste.extend(ma_liste2)
print(ma_liste)
# Ou
ma_liste3 = ['Xavier', 'Tabuteau']
ma_liste3 += ma_liste2
print(ma_liste3)

# TUPLES
# Déclarer un tuple sans la possibilité de modifier son contenu
monTuple = (0, 1, 1, 2, 2, 3, 5, 8, 13)
unTuple = 1, 2, 3
print(monTuple, unTuple)

# J'accède au 7e élément de la liste (les index commencent à 0)
print(monTuple[6])

# On ne peut pas modifié un tuple
# monTuple.append(5)
# monTuple.pop(4)
# monTuple.remove("coucou")

# SET (ensemble non ordonné sans doublons)
# Agit comme un dictionnaire n'ayant que des valeurs
# Liste avec doublon
mon_set = ['pascal', 'pierre', 'paul', 'pierre']

# Affichage en set
print(set(mon_set))

# Reconverti en liste sans doublon
print(list(set(mon_set)))
print(mon_set)

# Affectation d'un set
mon_set = {'pascal', 'pierre', 'paul', 'pierre'}
set2 = {"toto", "titi"}
print(mon_set, set2)

# Ajouter une valeur
mon_set.add("toto")
print("mon set =", mon_set)

# Supprimer une valeur
mon_set.remove("toto")
print("mon set =", mon_set)

# Ajouter un autre set
mon_set.update(set2)
print("mon set =", mon_set)

# DICTIONNAIRES
# Construire un dictionnaire vide
dico = {}
print(type(dico))

# Ajouter des éléments
dico['Computer'] = 'Ordinateur'
dico['Mouse'] = "Souris"
dico["Keyboard"] = "Clavier"
print(dico)

# Ajouter un dictionnaire à un autre
dico.update({'Printer' : "Imprimante"})
print(dico)

# Un autre dictionnaire créer directement
berti = {
    "Nom": "Bertignac",
    "Prenom": "Louis",
    "Instruments": ["Guitare", "Chant"]}

print(berti)

# Accéder à la valeur rattaché à la clé Nom
print(berti["Nom"])
print(berti.get("Nom"))

# Accéder à un élément d'une liste dans un dictionnaire
print(berti["Instruments"][0])

# Enregistrer un nouvel ensemble clé valeur
berti["Groupes"] = ["Higelin, Telephone", "Bertignac et les visiteurs"]
print(berti)

# Effacer une clé et la valeur qui lui est associée
del berti["Instruments"]
print(berti)

# Récupérer la liste des clés
print(dico.keys())
print(berti.keys())

# Récupérer la liste des valeurs
print(dico.values())

# Récupérer la liste des clés/valeurs
print(dico.items())

# Copier un dictionnaire par référence
dico_ref = dico

# Copier un dictionnaire par valeur
dico_copy = dico.copy()
