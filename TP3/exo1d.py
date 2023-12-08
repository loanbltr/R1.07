x=int(input("Entrez une valeur superieur à 1: "))
if x <=1:
    x = int(input("entrez une valeur supérieur à 1: "))
n=0
a=0

for i in range(0, x+1):
    while a < x:
        n += 1
        a += i
        i += 1

n -= 1
print("La valeur recherché est :", n)