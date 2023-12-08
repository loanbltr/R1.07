import random

piece= random.randint(1,3)
print(piece)

if piece<3:
    print("Pile !")
else:
    print("Face !")