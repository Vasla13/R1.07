def est_palindrome(chaine):
    # Retire les caractères non alphabétiques et convertit en minuscules
    chaine_epuree = ''.join(c.lower() for c in chaine if c.isalpha())

    # Teste si la chaîne épurée est un palindrome
    if chaine_epuree == chaine_epuree[::-1]:
        return True
    else:
        return False

# Demande à l'utilisateur d'entrer une chaîne de caractères
entree_utilisateur = input("Entrez un mot ou une phrase : ")

# Vérifie si la chaîne est un palindrome et affiche le résultat
if est_palindrome(entree_utilisateur):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
