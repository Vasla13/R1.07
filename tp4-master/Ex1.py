def table(nombre):
    resultat_table = []
    for i in range(10):
        resultat = nombre * i
        resultat_table.append(resultat)

    return resultat_table

def afficher_table(resultat, nombre):
    print(f"Vous cherchez la table de multiplication de quel nombre ? {nombre}")
    for i, resultat in enumerate(resultat):
        print(f"{nombre} * {i} = {resultat:.1f}")


if __name__ == "__main__":
    nombre_reel = float(input("Entrez le nombre réel pour la table de multiplication : "))

    table_resultats = table(nombre_reel)

    afficher_table(table_resultats, nombre_reel)



