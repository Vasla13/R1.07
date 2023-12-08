def calcul_salaire(nombre_heures, salaire_horaire):
    if nombre_heures <= 160:
        salaire_total = nombre_heures * salaire_horaire
    elif 160 < nombre_heures <= 200:
        salaire_total = 160 * salaire_horaire + (nombre_heures - 160) * salaire_horaire * 1.25
    else:
        salaire_total = 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (nombre_heures - 200) * salaire_horaire * 1.5

    return salaire_total
    
nombre_heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire = calcul_salaire(nombre_heures_travaillees, salaire_horaire)

print(f"Le salaire total est : {salaire} euros.")
