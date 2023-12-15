import random

def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):
    return sum(1 for valeur in table if valeur < vseuil)

def programme_interactif():
    nbr = int(input("Entrez le nombre de valeurs à générer : "))
    vmin = int(input("Entrez la valeur minimale : "))
    vmax = int(input("Entrez la valeur maximale : "))
    
    seuil_specifie = input("Voulez-vous préciser le seuil ? (Oui/Non) : ").lower()
    if seuil_specifie == 'oui' or seuil_specifie == 'o':
        vseuil = int(input("Entrez le seuil : "))
    else:
        vseuil = 30

    print(f"Générer {nbr} nombres entiers entre {vmin} et {vmax}")
    tab = generer(nbr, vmin, vmax)
    tab.sort()
    print(tab)
    total = combienInferieur(tab, vseuil)
    print(f"Il y en a {total} inférieurs à {vseuil}")

# Appeler la fonction pour exécuter le programme interactif
programme_interactif()
