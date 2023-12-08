a=0
sup10=0
sup15=0
inf10=0

while a != 10:
    a+=1
    x = int(input("entrez une nouvelle valeur:"))
    if x > 20 or x < 0:
        print("votre valeur doit etre comprise entre 0 et 20")
        x = int(input("entrez votre valeur"))
    if x >= 15:
        sup15 += 1
    if 10 <= x < 15:
        sup10 += 1
    if x <10:
        inf10 += 1
print("")
print("nombre compris entre 10 et 15:", sup10)
print("nombre supperieur à 15:", sup15)
print("nombre inferieur à 10:", inf10)