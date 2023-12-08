def taille_chaine(chaine):
    taille = 0
    for char in chaine:
        if char == '\0':
            break
        taille += 1
    return taille

def pourcentage_voyelles(chaine):
    taille = taille_chaine(chaine)
    voyelles = "aeiouAEIOU"
    nombre_voyelles = sum(1 for char in chaine if char in voyelles)
    pourcentage = (nombre_voyelles / taille) * 100 if taille > 0 else 0
    return pourcentage

def est_sous_chaine(chaine, sous_chaine):
    taille_chaine = taille_chaine(chaine)
    taille_sous_chaine = taille_chaine(sous_chaine)

    for i in range(taille_chaine - taille_sous_chaine + 1):
        if chaine[i:i + taille_sous_chaine] == sous_chaine:
            return True, i

    return False, -1

def nombre_occurrences(chaine, sous_chaine):
    nombre = 0
    taille_chaine = taille_chaine(chaine)
    taille_sous_chaine = taille_chaine(sous_chaine)

    for i in range(taille_chaine - taille_sous_chaine + 1):
        if chaine[i:i + taille_sous_chaine] == sous_chaine:
            nombre += 1

    return nombre

chaine_utilisateur = input("Entrez une chaîne de caractères : ")

phrases = [
    "Le wagon bleu est rapide.",
    "Un petit wagon roule vite.",
    "Le ciel est bleu, comme un wagon.",
    "Wagon après wagon, le train avance.",
    "Il y a cinq wagons dans le train.",
    "La locomotive tire les wagons.",
    "Wagon, wagon, wagon, ciel bleu.",
    "Le train avance avec ses wagons.",
    "Un wagon rouge file à toute vitesse.",
    "Le wagon jaune transporte des marchandises."
]

for phrase in phrases:
    print(f"\nAnalyse de la phrase : '{phrase}'")
    print(f"Taille de la chaîne : {taille_chaine(phrase)} caractères")
    print(f"Pourcentage de voyelles : {pourcentage_voyelles(phrase):.2f}%")
    
    sous_chaine = "wagon"
    est_presente, debut_occurrence = est_sous_chaine(phrase, sous_chaine)
    if est_presente:
        print(f"'{sous_chaine}' est une sous-chaîne, début de la première occurrence : {debut_occurrence}")
        print(f"Nombre d'occurrences de '{sous_chaine}' : {nombre_occurrences(phrase, sous_chaine)}")
    else:
        print(f"'{sous_chaine}' n'est pas une sous-chaîne dans la phrase.")

