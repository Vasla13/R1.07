import random

nombre_mystere = random.randint(0, 100)

compteur_tours = 0

print("Bienvenue dans le jeu du nombre mystère !")

while True:
    guess = int(input("Devinez le nombre entre 0 et 100 : "))

    compteur_tours += 1

    if guess < nombre_mystere:
        print("Le nombre mystère est plus grand. Essayez à nouveau.")
    elif guess > nombre_mystere:
        print("Le nombre mystère est plus petit. Essayez à nouveau.")
    else:
        print(f"Félicitations ! Vous avez trouvé le nombre mystère {nombre_mystere} en {compteur_tours} tours.")
        break