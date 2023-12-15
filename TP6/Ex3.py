# Déclaration de la fonction ajouter_elt
def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

# a) Résultat de print(ajouter_elt())
resultat_a = ajouter_elt()
print(resultat_a)

# b) Répéter l'instruction, utiliser id() pour afficher l'ID de 'lst'
resultat_b1 = ajouter_elt()
resultat_b2 = ajouter_elt()
print(resultat_b1)
print(resultat_b2)
print("ID de lst après le premier appel:", id(resultat_b1))
print("ID de lst après le deuxième appel:", id(resultat_b2))

# Déclaration de la fonction ajouter_carac
def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

# d) Résultat de print(ajouter_carac())
resultat_d = ajouter_carac()
print(resultat_d)

# e) Répéter l'instruction, utiliser id() pour afficher l'ID de 'ch'
resultat_e1 = ajouter_carac()
resultat_e2 = ajouter_carac()
print(resultat_e1)
print(resultat_e2)
print("ID de ch après le premier appel:", id(resultat_e1))
print("ID de ch après le deuxième appel:", id(resultat_e2))
