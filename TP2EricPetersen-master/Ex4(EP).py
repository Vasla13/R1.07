BASE = 4

fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

nouvelleQuantiteFromage = fromage * nbConvives / BASE
nouvelleQuantiteEau = eau * nbConvives / BASE
nouvelleQuantiteAil = ail * nbConvives / BASE
nouvelleQuantitePain = pain * nbConvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personne(s), il vous faut :")
print(f"- {nouvelleQuantiteFromage} gr de fromage")
print(f"- {nouvelleQuantiteEau} dl d'eau")
print(f"- {nouvelleQuantiteAil} gousse(s) d'ail")
print(f"- {nouvelleQuantitePain} gr de pain")
