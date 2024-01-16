import os
import sys

def aide():
    print("Usage: python find2.py <chemin_dossier>")
    print("Exemple: python find2.py /chemin/vers/dossier")

def recherche(dossier):
    listeFichiers = []
    listeDossiers = []

    try:
        with os.scandir(dossier) as entries:
            for entry in entries:
                if entry.is_file():
                    listeFichiers.append(entry.name)
                elif entry.is_dir():
                    listeDossiers.append(entry.name)
                    # Appeler récursivement la fonction recherche pour les sous-dossiers
                    sous_dossier = os.path.join(dossier, entry.name)
                    sous_listeFichiers, sous_listeDossiers = recherche(sous_dossier)
                    listeFichiers.extend(sous_listeFichiers)
                    listeDossiers.extend(sous_listeDossiers)
    except OSError as e:
        print(f"Erreur lors de l'accès au dossier : {e}")

    return listeFichiers, listeDossiers

def main():
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 2:
        print("Erreur : un argument (chemin du dossier) est requis.")
        aide()
        return

    # Récupérer le chemin du dossier depuis les arguments de la ligne de commande
    chemin_dossier = sys.argv[1]

    # Vérifier si le dossier existe
    if not os.path.exists(chemin_dossier) or not os.path.isdir(chemin_dossier):
        print(f"Erreur : '{chemin_dossier}' n'est pas un dossier existant.")
        aide()
        return

    # Appeler la fonction recherche pour obtenir la liste des fichiers et des dossiers
    fichiers, dossiers = recherche(chemin_dossier)

    # Afficher la liste des fichiers
    print("Liste des fichiers :")
    for fichier in fichiers:
        print(f"- {fichier}")

    # Afficher la liste des dossiers
    print("\nListe des dossiers :")
    for dossier in dossiers:
        print(f"- {dossier}")

if __name__ == "__main__":
    main()
