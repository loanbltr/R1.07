L1 = [0]*3
print(f"la liste {L1} le type {type(L1)} et l'id {id(L1)}")

for i in L1:
    print(f"la liste {i} le type {type(i)} et l'id {id(i)}")

L1[1] += 1
print ("aprés la modif")

print(f"la liste {L1} le type {type(L1)} et l'id {id(L1)}")
for i in L1:
    print(f"la liste {i} le type {type(i)} et l'id {id(i)}")

""" 
les élements de la liste sont mutables 
on voit que les valeurs ont le même type et la même référence
quand on change une valeur dans la liste, on voit que la référence change, alors que celle de la liste ne change pas.

si on re-exécute le script, on voit que les références changent, même pour la valeur unique 0 et 1
"""
