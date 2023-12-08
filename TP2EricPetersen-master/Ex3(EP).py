a = input("Entrez la première valeur : ")
b = input("Entrez la deuxième valeur : ")
c = input("Entrez la troisième valeur : ")

print("Les valeurs entrées sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")

temp = a
a = b
b = c
c = temp

print("Les valeurs permutées sont : a = " + a + ", b = " + b + " et c = " + c)
48