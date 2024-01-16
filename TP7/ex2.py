import os
import sys

def aide():
    print("Usage: python find1.py <chemin_dossier>")
    print("Exemple: python find1.py /chemin/vers/dossier")

def affiche(chemin_dossier):
    try:
        with os.scandir(chemin_dossier) as entries:
            for entry in entries:
                print(entry.name)
    except OSError as e:
        print(f"Erreur lors de l'accès au dossier : {e}")

def main():
    if len(sys.argv) != 2:
        print("Erreur : un argument (chemin du dossier) est requis.")
        aide()
        return

    chemin_dossier = sys.argv[1]

    if not os.path.exists(chemin_dossier) or not os.path.isdir(chemin_dossier):
        print(f"Erreur : '{chemin_dossier}' n'est pas un dossier existant.")
        aide()
        return

    affiche(chemin_dossier)

if __name__ == "__main__":
    main()
