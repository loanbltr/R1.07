dico = {}
dico["firstname"] = "Beltran"
dico["name"] = "Loan"
dico["promo"] = 29
dico["group"] = 111

#print(f"Votre nom est {dico["firstname"]}, prénom est {dico["name"]}, vous faites partie de la promo {dico["promo"]} et votre groupe est RT {dico["group"]}")

#print("\nLes clés du dictionnaire sont :")
#for key in dico.keys():
    #print(f"- {key}")


#print("\nLes valeurs du dictionnaire sont :")
#for value in dico.values():
    #print(f"- {value}")

#print("\nLes tuplets du dictionnaire sont :")
#for item in dico.items():
    #print(f"- {item}")

dico2 = {}
dico2["firstname"] = "Runser"
dico2["name"] = "Greg"
dico2["promo"] = 29
dico2["group"] = 111

binome = {1: dico,2:dico2}
for item in binome.items():
    print(f"- {item}")