import os.path
import datetime

def afficher_info_fichier(nom_fichier):
    chemin_fichier = os.path.join(os.path.dirname(__file__), nom_fichier)
    
    if os.path.isfile(chemin_fichier):
        taille_octets = os.path.getsize(chemin_fichier)
        print(f"Taille du fichier {chemin_fichier} : {taille_octets} octets")

        date_modification_timestamp = os.path.getmtime(chemin_fichier)
        date_modification = datetime.datetime.fromtimestamp(date_modification_timestamp)
        print(f"Dernière modification du fichier {chemin_fichier} : {date_modification}")
    else:
        print(f"Le fichier {chemin_fichier} n'existe pas.")

fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")

afficher_info_fichier(fichier1)
afficher_info_fichier(fichier2)
