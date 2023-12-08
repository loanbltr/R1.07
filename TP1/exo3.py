print("Entrez la date")
jour=int(input())
print("Entrez l'heure")
heure=int(input())
print("Entrez les minute")
minute=int(input())


time=(jour*24 + heure)*60 + minute
print("Il s'est écoulé", time, "minutes depuis le début du mois.")

