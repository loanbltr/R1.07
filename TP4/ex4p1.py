L1 = [2, 7, 5, 6, 7, 1, 2, 1, 7, 7, 6, 6, 6, 7]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
a1=1
nbr=0
most=0

L1.sort()
print(L1)
for i in range(len(L1)):
    if i == len(L1)-1 and L1[i-1] == L1[i]:
        if a1 > nbr:
            most = L1[i]
            nbr = a1
    else:
        if L1[i] == L1[i+1]:
            a1 +=1
        else:
            if a1 > nbr:
                most = L1[i]
                nbr = a1
            a1=1
print(most, nbr)


"""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
