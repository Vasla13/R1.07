import random

# Génération d'un nombre aléatoire entre 0 et 1 (0 inclus, 1 exclu)
resultat = random.random()

# Probabilité de Pile (ajustez selon les spécifications)
probabilite_pile = 2 / 3

# Vérification du résultat
if resultat < probabilite_pile:
    resultat_final = "Pile !"
else:
    resultat_final = "Face !"

# Affichage du résultat
print(resultat_final)
