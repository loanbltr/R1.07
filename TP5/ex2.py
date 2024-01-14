inf8 = False
mG = False
moyenne = 0.0
fullNotes = 0.0
fullCoef = 0.0

for i in range(5):
    module = str(input("Veuillez entrer la note du module 1 et le coefficient correspondant (sous la forme: 'note coef') :"))
    split = module.split(" ")
    note = float(split[0])
    coef = float(split[1])
    if note < 8:
        inf8 = True
    fullNotes += note*coef
    fullCoef += coef
moyenne = fullNotes / fullCoef
if moyenne >= 10:
    mG = True
if mG == True and inf8 == False:
    print("L'élève peut passer")
else:
    print("L'élève ne peut pas passer")