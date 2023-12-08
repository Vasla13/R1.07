def saisie_personne():
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    return nom, prenom


def afficher_resultat(nom, prenom):
    nom_majuscules = nom.upper()
    prenom_capitalized = prenom.capitalize()

    print(f"{prenom_capitalized} {nom_majuscules}")


# Saisie des informations pour la première personne
nom1, prenom1 = saisie_personne()

# Saisie des informations pour la deuxième personne
nom2, prenom2 = saisie_personne()

# Comparaison et affichage dans l'ordre alphabétique
if nom1.lower() == nom2.lower():
    if prenom1.lower() <= prenom2.lower():
        afficher_resultat(nom1, prenom1)
        afficher_resultat(nom2, prenom2)
    else:
        afficher_resultat(nom2, prenom2)
        afficher_resultat(nom1, prenom1)
else:
    if nom1.lower() <= nom2.lower():
        afficher_resultat(nom1, prenom1)
        afficher_resultat(nom2, prenom2)
    else:
        afficher_resultat(nom2, prenom2)
        afficher_resultat(nom1, prenom1)