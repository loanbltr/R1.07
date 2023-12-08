BASE=4
fromage=800
eau=2
ail=2
pain=400

nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
nouvelleQuantiteFromage= fromage*nbConvives/BASE
nouvelleQuantiteEau= eau*nbConvives/BASE
nouvelleQuantiteAil= ail*nbConvives/BASE
nouvelleQuantitePain= pain*nbConvives/BASE

print("Pour faire une fondue fribourgeoise pour", nbConvives, " personnes, il vous faut : \n -", nouvelleQuantiteFromage, " gr de fromage \n -", nouvelleQuantiteEau, " dl d'eau \n -", nouvelleQuantiteAil, " gousse(s) d'ail \n -", nouvelleQuantitePain, " gr de pain")
