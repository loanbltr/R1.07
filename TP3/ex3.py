from random import *

x = int(input("Entrez une valeur: "))
r = randint(0, 100)

print(r)

while x != r:
    if x < r:
        print("Votre valeur est trop petite")
        x = int(input("Entrez une valeur: "))
    if x > r:
        print("Votre valeur est trop grande")
        x = int(input("Entrez une valeur: "))
print("Bravo vous avez trouvé la valeur", r)