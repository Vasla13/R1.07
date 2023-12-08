def decomposition_monnaie(somme):
    billet_100 = somme // 100
    somme %= 100

    billet_50 = somme // 50
    somme %= 50

    billet_10 = somme // 10
    somme %= 10

    piece_2 = somme // 2
    somme %= 2

    piece_1 = somme

    print(f"{somme} euros, c'est donc {billet_100} billets de 100, {billet_50} de 50, {billet_10} de 10, {piece_2} pièces de 2 et {piece_1} pièce 1.")

somme_entree = int(input("Entrez une somme d'argent en euros : "))

decomposition_monnaie(somme_entree)
