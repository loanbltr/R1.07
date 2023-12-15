import datetime
import os.path
from os.path import *

file1Name = str(input("Entrez le nom d'un fichier (précisez l'extension): "))
file2Name = str(input("Entrez le nom d'un  (précisez l'extension: "))

if os.path.isfile(file1Name):
    print(f"{file1Name} est un fichier existant")
    print(datetime.datetime.fromtimestamp(os.path.getmtime(file1Name)))
else:
    print("Le fichier n'existe pas, vous avez peute être oublié d'indiquer l'extension...")

if os.path.isfile(file2Name):
    print(f"{file2Name} est un fichier existant")
    print(datetime.datetime.fromtimestamp(os.path.getmtime(file1Name)))
else:
    print("Le fichier n'existe pas, vous avez peute être oublié d'indiquer l'extension...")