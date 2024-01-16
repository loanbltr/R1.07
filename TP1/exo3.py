jour=int(input("Entrez la date: "))
heure=int(input("Entrez l'heure: "))
minute=int(input("Entrez les minutes: "))


time=(jour*24 + heure)*60 + minute
print("Il s'est écoulé", time, "minutes depuis le début du mois.")

