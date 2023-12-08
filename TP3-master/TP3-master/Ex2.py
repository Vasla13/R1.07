import time

def compte_a_rebours(n, boucle='for'):
    if boucle == 'for':
        for i in range(n, -1, -1):
            print(i)
            time.sleep(1)
    elif boucle == 'while':
        while n >= 0:
            print(n)
            n -= 1
            time.sleep(1)
    else:
        print("Type de boucle non reconnu. Utilisez 'for' ou 'while'.")

nombre_entier = int(input("saisir un nombre entier positif : "))
type_boucle = input("saisir le type de boucle ('for' ou 'while') : ")

compte_a_rebours(nombre_entier, type_boucle)