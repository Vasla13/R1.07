def est_palindrome(chaine):
    chaine_epuree = ''.join(c.lower() for c in chaine if c.isalpha())

    if chaine_epuree == chaine_epuree[::-1]:
        return True
    else:
        return False

entree_utilisateur = input("Entrez un mot ou une phrase : ")

if est_palindrome(entree_utilisateur):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
