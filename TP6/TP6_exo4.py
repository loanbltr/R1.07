import random
## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr' valeurs
## comprises entre 'vmin' et 'vmax'
def generer(nbr, vmin, vmax):
    liste=[]
    for i in range(nbr):
        val = random.randint(vmin,vmax)
        liste.append(val)
    return liste

## Fonction combienInferieur(table, vseuil) pour compter le nombre de valeurs
## d'un tableau 'table' inférieures à la valeur 'vseuil'
def combienInferieur(tab, val=30):
    count = 0
    for i in tab:
        if i<val:
            count+=1
    return count

nb = int(input("saisir le nombre de valeurs du tableau: "))
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
print(tab)

choix = input("voulez vous saisir le seuil de décompte: ")
if choix == "O" or choix == "o":
    seuil = int(input("saisie le seuil: "))
    total = combienInferieur(tab, seuil)
    print(f"Il y en a {total} inférieurs à {seuil}")
else :
    total = combienInferieur(tab)
    print(f"Il y en a {total} inférieurs à 30")