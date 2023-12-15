good = True
chaineWO = ""
chaine = str(input("Entrez une chaîne de caractères : "))
chaine = chaine.lower()

for caractere in chaine:
    if caractere.isalpha():
        chaineWO += caractere

longueur = len(chaineWO)
for i in range(longueur // 2):
    if chaineWO[i] != chaineWO[longueur - 1 - i]:
        good = False
        break

if good == True:
    print("La chaîne de caractère est un palyndrome.")
else:
    print("Ce n'est pas un palyndrome")