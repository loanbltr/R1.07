T = [5, 2, 4, 8, 1, 3]

for i in range(len(T)):
    for j in range(len(T)):
        if T[i] > T[j]:
            T[i], T[j] = T[j], T[i]
            print(T)
print("")
print(sorted(T))
print("")
T.sort()
print(T)
