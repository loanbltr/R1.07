x = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
T=[]

for i in range(10):
    T.append(x*i)
for j in range(10):
    print(x, "*", j, "=", T[j].__round__(1))