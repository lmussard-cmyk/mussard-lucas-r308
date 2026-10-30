import random


class JoueurHumain:

    def __init__(self, nom="Humain"):
        self.nom = nom

    def prochain_coup(self, grille, symbole):
        #Demander au joueur de saisir la ligne et la colonne au clavier.
        while True:
            try:
                print("Tour de {self.nom} ({symbole}) :")
                x = int(input("  -> Ligne (0, 1 ou 2) : "))
                y = int(input("  -> Colonne (0, 1 ou 2) : "))
                return (x, y)
            except ValueError:
                print("Veuillez saisir des nombres entiers valides (0, 1 ou 2).")


class JoueurIA:

    def __init__(self, nom="Robot"):
        self.nom = nom

    def prochain_coup(self, grille, symbole):
        #Choisit une case libre au hasard parmi celles disponibles.
        # Récuperer le tableau 2D 
        tab = grille.grille if hasattr(grille, "grille") else grille

        cases_libres = [
            (x, y)
            for x in range(3)
            for y in range(3)
            if tab[x][y] == " "
        ]

        if cases_libres:
            coup = random.choice(cases_libres)
            print("Tour de {self.nom} ({symbole}) -> Joue en {coup}")
            return coup
        return None