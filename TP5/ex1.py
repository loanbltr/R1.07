nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

personnes = [(nom1, prenom1), (nom2, prenom2)]

personnes_tri = sorted(personnes, key=lambda x: (x[0].upper(), x[1].capitalize()))

print("\nRésultats triés alphabétiquement :")
for nom, prenom in personnes_tri:
    nom_majuscules = nom.upper()
    prenom_formate = prenom.capitalize()
    print(f"{prenom_formate} {nom_majuscules}")