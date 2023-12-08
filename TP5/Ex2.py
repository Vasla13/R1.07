def saisie_notes():
    notes = []
    coefficients = []

    for i in range(5):
        entry = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant (séparés par un espace) : ")
        values = entry.split()

        note = float(values[0])
        coefficient = int(values[1])

        notes.append(note)
        coefficients.append(coefficient)

    return notes, coefficients

def calcul_moyenne(notes, coefficients):
    somme = 0
    total_coefficient = 0

    for i in range(5):
        somme += notes[i] * coefficients[i]
        total_coefficient += coefficients[i]

    moyenne = somme / total_coefficient
    return moyenne

def est_admis(moyenne, notes):
    return moyenne > 10 and all(note >= 8 for note in notes)

notes, coefficients = saisie_notes()

moyenne_generale = calcul_moyenne(notes, coefficients)

if est_admis(moyenne_generale, notes):
    print(f"L'étudiant est admis avec une moyenne générale de {moyenne_generale:.2f}.")
else:
    print(f"L'étudiant n'est pas admis avec une moyenne générale de {moyenne_generale:.2f}.")
