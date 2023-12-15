# Déclaration de la fonction ajouter_elt(liste, elt):
def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

# a) Créer la liste lst1 initialisée avec les valeurs [0, 1, 2].
lst1 = [0, 1, 2]

# b) Créer une seconde liste lst2 initialisée par la fonction ajouter_elt avec comme argument la liste lst1 et sa longueur.
lst2 = ajouter_elt(lst1.copy(), len(lst1))

# c) Afficher le contenu, le type et l'identifiant de chaque liste.

# Pour lst1
print("Contenu de lst1:", lst1)
print("Type de lst1:", type(lst1))
print("Identifiant de lst1:", id(lst1))

# Pour lst2
print("\nContenu de lst2:", lst2)
print("Type de lst2:", type(lst2))
print("Identifiant de lst2:", id(lst2))
