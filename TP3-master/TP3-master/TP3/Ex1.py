def somme_entiers_naturels():
    N = int(input("Entrez la valeur de N : "))
    somme = 0

    for i in range(N + 1):
        somme += i

    print("La somme des N entiers naturels est :", somme)

def boucle_attente():
    valeur_utilisateur = 0

    while valeur_utilisateur != 100:
        valeur_utilisateur = int(input("Entrez une valeur (entrez 100 pour terminer) : "))

    print("Boucle terminée.")

def lecture_valeurs_reelles():
    inf_10 = 0
    sup_10_inf_15 = 0
    sup_15 = 0

    for _ in range(10):
        valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))
        
        if 0 <= valeur < 10:
            inf_10 += 1
        elif 10 <= valeur < 15:
            sup_10_inf_15 += 1
        elif valeur >= 15:
            sup_15 += 1

    print("Nombre de valeurs inférieures à 10 :", inf_10)
    print("Nombre de valeurs entre 10 (inclus) et 15 (non inclus) :", sup_10_inf_15)
    print("Nombre de valeurs supérieures ou égales à 15 :", sup_15)

def plus_grand_N():
    X = float(input("Entrez la valeur de X (supérieure à 1) : "))
    somme = 0
    N = 0

    while somme <= X:
        N += 1
        somme += N

    print("Le plus grand nombre N tel que la somme des entiers jusqu'à N est inférieure ou égale à", X, "est :", N - 1)

somme_entiers_naturels()
boucle_attente()
lecture_valeurs_reelles()
plus_grand_N()

