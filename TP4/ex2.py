nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
ecartType = 0.0

notes = []

print("")
for i in range(nombreEtudiants):
    x = float(input("Note étudiant {} : ".format(i)))
    if x>20 or 0>x:
        while x > 20 or 0 > x:
            x = float(input("Note étudiant {} : ".format(i)))
    notes.append(x)
    moyenne += x

moyenne = moyenne/nombreEtudiants

print("\nMoyenne de classe: {} \n".format(moyenne) )
for i in range(nombreEtudiants):
    ecartType = notes[i] - moyenne
    print("{} | {} | {}".format(i, notes[i], ecartType))
