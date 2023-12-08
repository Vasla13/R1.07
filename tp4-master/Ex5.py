def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

date_str = input("Entrez une date sous la forme jjmmaaaa : ")

if len(date_str) != 8:
    print("La date n'est pas au bon format. Assurez-vous qu'elle soit de la forme jjmmaaaa.")
else:
    day = int(date_str[:2])
    month = int(date_str[2:4])
    year = int(date_str[4:])

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12:
        print("Mois invalide. Veuillez saisir un mois entre 01 et 12.")
    else:
        if is_leap_year(year):
            days_in_month[2] = 29

        if day < 1 or day > days_in_month[month]:
            print("Jour invalide pour le mois donné.")
        else:
            print("La date est valide.")
