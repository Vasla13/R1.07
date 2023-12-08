def decomposition_monnaie(somme):
    # Décomposition en billets de 100
    billet_100 = somme // 100
    somme %= 100

    # Décomposition en billets de 50
    billet_50 = somme // 50
    somme %= 50

    # Décomposition en billets de 10
    billet_10 = somme // 10
    somme %= 10

    # Décomposition en pièces de 2
    piece_2 = somme // 2
    somme %= 2

    # Ce qui reste sont les pièces de 1
    piece_1 = somme

    # Affichage du résultat
    print(f"{somme} euros, c'est donc {billet_100} billets de 100, {billet_50} de 50, {billet_10} de 10, {piece_2} pièces de 2 et {piece_1} pièce 1.")

# Demande à l'utilisateur d'entrer une somme d'argent
somme_entree = int(input("Entrez une somme d'argent en euros : "))

# Appel de la fonction pour afficher la décomposition
decomposition_monnaie(somme_entree)
