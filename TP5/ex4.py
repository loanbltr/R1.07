argent = int(input("Entrez une somme d'argent: "))
billet100 = 0
billet50 = 0
billet10 = 0
piece2 = 0
piece1 = 0
sommeI = argent

if argent >= 100:
    while argent >= 100:
        argent -= 100
        billet100 += 1
if argent >= 50:
    while argent >= 50:
        argent -= 50
        billet50 += 1
if argent >= 10:
    while argent >= 10:
        argent -= 10
        billet10 += 1
if argent >= 2:
    while argent >= 2:
        argent -= 2
        piece2 += 1
if argent >= 1:
    while argent >= 1:
        argent -= 1
        piece1 += 1
print(f"La sommes {sommeI} peut être décomposé en {billet100} billets de 100, {billet50} billet de 50, {billet10} billet de 10, {piece2} pièce de 2 et {piece1} pièce de1.")