# a) Initialisez une liste ne comprenant que trois zéros
L1 = [0] * 3
print("a) Liste initiale:", L1)
print("   Type de la liste:", type(L1))
print("   ID de la liste:", id(L1))
print()

# b) Affichez la valeur, le type et l'identifiant de chaque élément de la liste
for element in L1:
    print("b) Valeur:", element)
    print("   Type:", type(element))
    print("   ID:", id(element))
    print()

# c) Modifiez l'élément en deuxième position
L1[1] += 1
print("c) Liste après modification:", L1)
print("   Type de la liste:", type(L1))
print("   Nouvel ID de la liste:", id(L1))
print()

# d) Revérifiez les identifiants après la modification
for element in L1:
    print("d) Valeur:", element)
    print("   Type:", type(element))
    print("   ID:", id(element))
    print()

# e) Déclarez une variable avec la chaîne "machaine" et effectuez le même test
ma_chaine = "machaine"
print("e) ID de la variable:", id(ma_chaine))
for char in ma_chaine:
    print("   Caractère:", char)
    print("   Type:", type(char))
    print("   ID:", id(char))
    print()

