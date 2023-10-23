jour = int(input("Jour(s):"))
heure = int(input("heure(s):"))
minute = int(input("minute(s):"))

minutes_ecoulees = (jour-1) * 24 * 60 + heure * 60 + minute
print(f"Depuis le début du mois, il s'est écoulé {minutes_ecoulees} minutes.")

