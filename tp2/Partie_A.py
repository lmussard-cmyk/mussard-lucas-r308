class Grille:
    def __init__(self):
        # Création de la grille 3x3 
        self.grille = [[" " for _ in range(3)] for _ in range(3)]

    def afficher(self):
        #Afficher la grille
        for i, ligne in enumerate(self.grille):
            print(" " + " | ".join(ligne) + " ")
            if i < 2:
                print("---|---|---")

    def jouer(self, x, y, joueur):
        #Place un symbole si la case est valide et libre
        # Vérification des limites de la grille
        if not (0 <= x < 3 and 0 <= y < 3):
            print("Coup ({x}, {y}) refusé : hors grille.")
            return False

        # Vérifier si la case est occupée
        if self.grille[x][y] != " ":
            print("Coup ({x}, {y}) refusé : case occupée.")
            return False

        self.grille[x][y] = joueur
        return True

    def est_gagnant(self, j):
        #Vérifie si le joueur j a aligné 3 symboles (lignes, colonnes, diagonales).
        # Vérification des lignes
        for x in range(3):
            if all(self.grille[x][y] == j for y in range(3)):
                return True

        # Vérification des colonnes
        for y in range(3):
            if all(self.grille[x][y] == j for x in range(3)):
                return True

        # Diagonale principale (top-left -> bottom-right)
        if all(self.grille[i][i] == j for i in range(3)):
            return True

        # Diagonale secondaire (top-right -> bottom-left)
        if all(self.grille[i][2 - i] == j for i in range(3)):
            return True

        return False 

    def est_plein(self):
        #True si aucune case est libre
        return all(self.grille[x][y] != " " for x in range(3) for y in range(3))
