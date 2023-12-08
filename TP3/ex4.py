x = int(input("Entrez 1 pour une boucle while, sinon entrez 2 pour une boucle for: "))
n = int(input("Entrez une valeur: "))
a = 1

if x==1:
    while n!=1:
        a = a*n
        n -= 1
    print(a)
if x==2:
    for i in range(1, n+1):
        a = a*i
    print(a)
