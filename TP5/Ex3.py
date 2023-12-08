import math

# Les notes des 5 étudiants
notes = [11.8, 2.8, 3, 2.2, 4.7]

# Calcul de la moyenne
moyenne = sum(notes) / len(notes)

# Calcul de la somme des carrés des écarts par rapport à la moyenne
somme_carres_ecarts = sum((x - moyenne) ** 2 for x in notes)

# Calcul de la variance
variance = somme_carres_ecarts / len(notes)

# Calcul de l'écart type en prenant la racine carrée de la variance
ecart_type = math.sqrt(variance)

print(f"L'écart type est : {ecart_type}")

