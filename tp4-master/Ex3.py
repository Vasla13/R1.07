nMax = 5

v1 = []
v2 = []

n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? "))

while n < 1 or n > nMax:
    print("La taille des vecteurs doit être entre 1 et 3. Réessayez.")
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? "))

print("Saisie du premier vecteur:")
for i in range(n):
    v1.append(float(input(f"v1[{i}] = ")))

print("Saisie du second vecteur:")
for i in range(n):
    v2.append(float(input(f"v2[{i}] = ")))

produit_scalaire = sum(v1[i] * v2[i] for i in range(n))

print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}")
