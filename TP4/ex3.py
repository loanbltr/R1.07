nMax=4

v1 = []
v1C = 0
v2 = []
v2C = 0
produitS = 0

n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

if 1>n or nMax<n:
     while 1>n or nMax<n:
         n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

print("")
print("Saisie du premier vecteur :")
for i in range(n):
    v1C = int(input("v1[{}] = ".format(i)))
    v1.append(v1C)

print("")
print("Saisie du second vecteur :")
for i in range(n):
    v2C = int(input("v2[{}] = ".format(i)))
    v2.append(v2C)

print("")
for i in range(n):
    produitS += v1[i]*v2[i]
print("Le produit scalaire de v1 par v2 vaut {}".format(produitS.__round__(1)))