n = int(input("Entrez un nombre: "))
a=0

for i in range(1, n+1):
    a += i
print("La somme des entiers positifs infèrieurs à", n, "est", a)