jour = int(input("Veuillez saisir un jour entre 0 et 31 :"))
heure = int(input("Veuillez saisir une heure entre 0 et 24 :"))
minute = int(input("Veuillez saisir une minute entre 0 et 60 :"))

Tempsjour = jour * 24 * 60
heure = heure * 60
total = Tempsjour + heure + minute
print(total)
