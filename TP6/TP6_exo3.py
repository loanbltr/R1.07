# déclaration de la fonction ajouter_elt(lst=[0, 1, 2], elt=3)
def ajouter_elt(lst=[0,1,2], elt=3):
       lst.append(elt)
       print (f"fonction : id liste = {id(lst)}, id elt = {id(elt)}")
       return lst


liste=ajouter_elt()
print(f"La liste créée {liste}, id = {id(liste)}")

ajouter_elt(liste)
print(f"Second appel {liste} id ={id(liste)}")

ajouter_elt(liste,5)
print(f"troisième appel {liste}")

def ajout_carac(ch="abc", elt="d"):
    ch=ch+elt
    print (f"id elt = {id(elt)} id ch = {id(ch)}")
    return ch

chaine=ajout_carac()
print(f"chaine = {chaine}")

print(f"chaine = {ajout_carac()}")