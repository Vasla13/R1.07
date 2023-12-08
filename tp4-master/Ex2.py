
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    note = float(input(f"Note etudiant {i} : "))
    while note < 0 or note > 20:  # Vérifier si la note est valide
        print("La note doit être comprise entre 0 et 20. Réessayez.")
        note = float(input(f"Note etudiant {i} : "))

    notes.append(note)
    moyenne += note

moyenne /= nombreEtudiants

print(f"Moyenne de classe : {moyenne}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart}")

