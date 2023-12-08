def factorielle_for(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
        print(f"Étape {i}: {resultat}")
    return resultat

def factorielle_while(n):
    resultat = 1
    i = 1
    while i <= n:
        resultat *= i
        print(f"Étape {i}: {resultat}")
        i += 1
    return resultat

def main():
    nombre_entier = int(input("Veuillez saisir un nombre entier : "))
    type_boucle = input("Veuillez saisir le type de boucle ('for' ou 'while') : ")

    if type_boucle == 'for':
        resultat_final = factorielle_for(nombre_entier)
    elif type_boucle == 'while':
        resultat_final = factorielle_while(nombre_entier)
    else:
        print("Type de boucle non reconnu. Utilisez 'for' ou 'while'.")
        return

    print(f"\nLa factorielle de {nombre_entier} est : {resultat_final}")

if __name__ == "__main__":
    main()