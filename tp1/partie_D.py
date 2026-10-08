#Partie D du TP1

import os
import random

ERREURS_MAX = 7

FICHIER_MOTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mots.txt")

MOTS_PAR_DEFAUT = ["python", "ordinateur", "programme", "variable", "fonction",
                   "boucle", "dictionnaire", "clavier", "ecran", "souris"]


# input() qui renvoie None si le programme n'a plus d'entrée a lire
def entree(message):
    try:
        return input(message).strip()
    except EOFError:
        print()
        return None


# Mots d'un fichier (un par ligne), ou la liste par defaut s'il n'est pas présent
def charger_liste_de_mots(chemin=FICHIER_MOTS):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            mots = [ligne.strip() for ligne in f if ligne.strip() != ""]
    except OSError:
        return list(MOTS_PAR_DEFAUT)
    return mots if mots != [] else list(MOTS_PAR_DEFAUT)


# Renvoie un mot de la liste en majuscules, ou "" si la liste est vide
def choisir_mot(liste):
    return random.choice(liste).upper() if liste != [] else ""


# Masque : liste de "_" de meme longueur que le mot, lettres trouvées revélées
def masque(mot, lettres_trouvees=""):
    trouvees = lettres_trouvees.upper()
    return [lettre if lettre in trouvees else "_" for lettre in mot.upper()]


# Demande une lettre valide et non encore proposee.
def demander_une_lettre(deja_proposees):
    while True:
        saisie = input("Votre lettre : ").strip().upper()
        if len(saisie) != 1 or saisie not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Il faut une seule lettre de l'alphabet.")
        elif saisie in deja_proposees:
            print("Lettre deja proposee :", saisie, "- pas d'erreur en plus.")
        else:
            return saisie

# Joue une partie avec le mot donne. Renvoie True si le mot est trouve.
def jouer_une_partie(mot):
    mot = mot.upper()
    cache, proposees, erreurs = " ".join(masque(mot)), [], 0

    while True:
        print("\nMot      :", cache)
        print("Erreurs  :", erreurs, "/", ERREURS_MAX)
        print("Proposees:", " ".join(proposees) if proposees else "(aucune)")

        lettre = demander_une_lettre(proposees)
        if lettre is None:
            print("Abandon. Le mot etait", mot)
            return False

        proposees.append(lettre)
        if lettre in mot:
            cache = " ".join(masque(mot, "".join(proposees)))
            print("Bien joue,", lettre, "est dans le mot !")
        else:
            erreurs = erreurs + 1
            print("Non,", lettre, "n'est pas dans le mot.")

        # la victoire est testée avant la défaite , si la dernière lettre trouvée complete le mot, le joueur a gagné meme a 7 erreurs
        if "_" not in cache:
            print("Gagne ! Le mot etait bien", mot)
            return True
        if erreurs >= ERREURS_MAX:
            print("Perdu ! Le mot etait", mot)
            return False


# Choisit un mot au hasard puis joue une partie.
def jouer_au_pendu():
    jouer_une_partie(choisir_mot(charger_liste_de_mots()))


if __name__ == "__main__":
    jouer_au_pendu()