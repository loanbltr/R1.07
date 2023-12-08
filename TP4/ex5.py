a = input("Entrez une date sous la forme xxxxxxxx : ")

jour = int(a[0]) * 10 + int(a[1])
mois = int(a[2]) * 10 + int(a[3])
annee = int(a[4]) * 1000 + int(a[5]) * 100 + int(a[6]) * 10 + int(a[7])
vrai = 0

if (annee > 0) or (annee <= 9999):
    if 1 <= mois or mois <= 12:
        if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
            if 1 <= jour or jour <=31:
                print(a, "(correcte)")
                vrai = 1
        elif mois ==2:
            if (annee % 4 == 0 and annee % 100 !=0) or annee % 400 == 0:
                if 1<= jour and jour <=29:
                    print(a, "(correcte)")
                    vrai = 1
            else:
                if 1<= jour and jour <=28:
                    print(a, "(correcte)")
                    vrai = 1
        elif 1<=jour <= 30:
            print(a, "(correcte)")
            vrai = 1
if vrai == 0:
    print(a, "(incorrecte)")