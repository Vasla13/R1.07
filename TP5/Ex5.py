def calcul_salaire(nombre_heures, salaire_horaire):
    if nombre_heures <= 160:
        # Pas de majoration
        salaire_total = nombre_heures * salaire_horaire
    elif 160 < nombre_heures <= 200:
        # Majoration de 25% pour les heures entre 161 et 200
        salaire_total = 160 * salaire_horaire + (nombre_heures - 160) * salaire_horaire * 1.25
    else:
        # Majoration de 25% pour les heures entre 161 et 200, et 50% pour les heures au-delà de 200
        salaire_total = 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (nombre_heures - 200) * salaire_horaire * 1.5

    return salaire_total

# Demande à l'utilisateur d'entrer le nombre d'heures travaillées et le salaire horaire
nombre_heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

# Appel de la fonction pour calculer le salaire
salaire = calcul_salaire(nombre_heures_travaillees, salaire_horaire)

# Affichage du résultat
print(f"Le salaire total est : {salaire} euros.")
