import time

x = int(input("Entrez une valeur positive: "))

if x < 0:
    x = int(input("Entrez une valeur positive: "))

for i in range(0, x):
    x -= 1
    print (x)
    time.sleep(1)

while x > -1:
    print(x)
    x = x -1
    time.sleep(1)
