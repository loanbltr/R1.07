from re import X


print("Vous devez louer votre vélo sur la même journée")
      
s = int(input("Donnez l'heure de début de location (entier): "))
if s < 0 or s > 24:
    while s < 0 or s > 24:
        print("Les heures doivent être comprises entre 0 et 24 ! \n")
        s = int(input("Donnez l'heure de début de location (entier): "))

e = int(input("Donnez l'heure de fin de location (entier): "))
if e < 0 or e > 24:
    while e < 0 or e > 24:
        print("Les heures doivent être comprises entre 0 et 24 ! \n")
        e = int(input("Donnez l'heure de fin de location (entier): "))

if s == e:
    while s==e:
        print("Attention ! l’heure de fin est identique à l’heure de début.")
        s = int(input("Donnez l'heure de début de location (entier): "))
        e = int(input("Donnez l'heure de fin de location (entier): "))
if s > e:
    while s > e:
        print("Attention ! le début de la location est après la fin ... \n")
        s = int(input("Donnez l'heure de début de location (entier): "))
        e = int(input("Donnez l'heure de fin de location (entier): "))

a=s
nbHeureTarif1=0
tempsTarif1=0
nbHeureTarif2=0
tempsTarif2=0
onlyTarif1 = False
onlyTarif2 = False

while a!=e:
    if 0 <= a < 7 or 17 <= a <24:
        nbHeureTarif1 +=1
        tempsTarif1 += 1
        onlyTarif1 = True
    if 7 <= a < 17:
        nbHeureTarif2 += 1
        tempsTarif2 += 1
        onlyTarif2 = True
    a += 1

montantTotal = nbHeureTarif1 + nbHeureTarif2*2

if onlyTarif1 == True and onlyTarif2 == False:
    print("Vous avez loué votre vélo pendant \n", tempsTarif1, "heure(s) au tarif horaire de 1.0 euro(s) \n Le montant total a payer est de", montantTotal, "euro(s)")
if onlyTarif1 == False and onlyTarif2 == True:
    print("Vous avez loué votre vélo pendant \n", tempsTarif2, "heure(s) au tarif horaire de 2.0 euro(s) \n Le montant total a payer est de", montantTotal, "euro(s)")
else:
    print("Vous avez loué votre vélo pendant \n", tempsTarif1, "heure(s) au tarif horaire de 1.0 euro(s) \n", tempsTarif2, "heure(s) au tarif horaire de 2.0 euro(s) \n Le montant total a payer est de", montantTotal, "euro(s)")