def calculer_salaire(heures_travaillees, salaire_horaire):
    salaire_total = 0

    if heures_travaillees <= 160:
        salaire_total = heures_travaillees * salaire_horaire
    else:
        salaire_total = 160 * salaire_horaire

        if heures_travaillees <= 200:
            heures_supplementaires = heures_travaillees - 160
            salaire_total += heures_supplementaires * salaire_horaire * 1.25
        else:
            heures_supplementaires_1 = 40
            heures_supplementaires_2 = heures_travaillees - 200
            salaire_total += heures_supplementaires_1 * salaire_horaire * 1.25
            salaire_total += heures_supplementaires_2 * salaire_horaire * 1.5

    return salaire_total

heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire_final = calculer_salaire(heures_travaillees, salaire_horaire)
print(f"Le salaire total est de : {salaire_final} euros.")
