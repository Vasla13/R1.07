import unicodedata

def nettoyer_texte(texte):
    # Retire les caractères spéciaux, espaces et ponctuations
    caracteres_permis = (c for c in texte if c.isalnum() or c.isspace())
    return ''.join(caracteres_permis)

def supprimer_accents(texte):
    # Remplace les caractères accentués par leur équivalent de base
    texte = unicodedata.normalize('NFD', texte)
    return ''.join(c for c in texte if not unicodedata.combining(c))

def est_palindrome(texte):
    texte_nettoye = nettoyer_texte(texte.lower())  # Convertit en minuscules pour la comparaison
    texte_sans_accents = supprimer_accents(texte_nettoye)
    return texte_sans_accents == texte_sans_accents[::-1]

# Demander à l'utilisateur d'entrer un mot ou une phrase
mot_phrase = input("Entrez un mot ou une phrase : ")

# Vérifier s'il s'agit d'un palindrome
if est_palindrome(mot_phrase):
    print("C'est un palindrome!")
else:
    print("Ce n'est pas un palindrome.")
