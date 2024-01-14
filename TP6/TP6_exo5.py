import unidecode

def sansAccent(chaine):
    chaine2 = ''
    for i in range(len(chaine)):
        if chaine[i]=='é' or chaine[i]=='è' or chaine[i]=='ê' or chaine[i]=='ë':
            print (chaine[i])
            chaine2 += 'e'
        elif chaine[i] == 'à' or chaine[i]=='â' or chaine[i]=='ä':
            chaine2+='a'
        elif chaine[i]=='ô' or chaine[i]=='ö':
            chaine2+='o'
        elif chaine[i]=='ü':
            chaine2+= 'u'
        elif chaine[i] =='ï' or chaine[i]=='î':
            chaine2+='i'
        elif chaine[i]=='ç':
            chaine2+='c'
        else:
            chaine2+=chaine[i]
    return chaine2

def sansespace(chaine):
    chaine2=''
    for i in range(len(chaine)):
        if chaine[i].isalpha():
            chaine2 += chaine[i]
    return chaine2

def palindrome(chaine):
    res = False
    i = 0
    chaine = str.lower(chaine)
    print(chaine)
    while i < len(chaine)/2 and chaine[i] == chaine[len(chaine)-1-i]:
         i+=1
    if i>len(chaine)/2-1:
        res = True
    return res

def sansAccents2(mot):
    tablo = {'éèêẽ': 'e'
        , 'ç': 'c'
        , 'àâã': 'a'
        , 'ù': 'u'
             }

    mot_sans_accents = ''
    for i in mot:
        for k in tablo:
            if i in k:
                i = tablo[k]
                break
        mot_sans_accents += i
    return mot_sans_accents

chaine = input("saisir la chaine à tester : ")
print(chaine)
chaine = sansAccent(chaine)
print(f"chaine sans accent {chaine}")
chaine = str(sansespace(chaine))
print(f"chaine sans espaace {chaine}")

if (palindrome(chaine)):
    print("c'est un palindrome")
else:
    print("ce n'est pas un palindrome")



