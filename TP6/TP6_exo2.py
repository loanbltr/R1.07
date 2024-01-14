# déclaration de la fonction ajouter_elt(liste, elt):

def ajouter_elt(lst, elt):
       lst.append(elt)
       return lst

liste = [1,2,4]
liste2=[]
print(liste)
for i in range (5):
    val = int(input("saisir une valeur entière"))
    liste2=ajouter_elt(liste,val)

print(f"liste 1 {liste} id {id(liste)}")

print (f"liste 2 {liste2} id {id(liste2)}")

""" c'est le même identifiant entre la liste et la liste2 donc entre celle passée et celle qui est renvoyée."""