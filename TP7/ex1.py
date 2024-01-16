import sys

def main():
    num_arguments = len(sys.argv) - 1  # Ignorer le nom du script lui-même

    if num_arguments == 1:
        print(f"Pas assez d'arguments pour le script '{sys.argv[0]}'")
    elif num_arguments > 1:
        print("Arguments du script :")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")

if __name__ == "__main__":
    main()
