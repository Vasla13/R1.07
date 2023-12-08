# Exercice 1a
N = int(input("Entrez la valeur de N : "))
somme_naturels = sum(range(N + 1))
print("La somme des N entiers naturels est :", somme_naturels)

# Exercice 1b
valeur_utilisateur = 0
while valeur_utilisateur != 100:
    valeur_utilisateur = int(input("Entrez une valeur (entre 0 et 100) : "))
print("Vous avez entré la valeur 100. La boucle d'attente se termine.")

# Exercice 1c
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
print("Nombre de valeurs entre 10 et 15 :", sup_10_inf_15)
print("Nombre de valeurs supérieures ou égales à 15 :", sup_15)

# Exercice 1d
X = int(input("Entrez la valeur de X (supérieure à 1) : "))
N = 0
somme = 0

while somme <= X:
    N += 1
    somme += N

print("Le plus grand nombre N tel que la somme soit inférieure ou égale à", X, "est :", N - 1)
