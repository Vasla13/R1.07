import time

def compte_a_rebours_for(n):
    print("Compte à rebours avec la boucle 'for':")
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)

def compte_a_rebours_while(n):
    print("Compte à rebours avec la boucle 'while':")
    while n >= 0:
        print(n)
        n -= 1
        time.sleep(1)

n = int(input("Entrez un nombre entier positif : "))

compte_a_rebours_for(n)

n = int(input("Entrez un nombre entier positif : "))

compte_a_rebours_while(n)

