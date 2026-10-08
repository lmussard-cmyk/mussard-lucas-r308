#Partie C du TP1

import os
import random

FICHIER_MOTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mots.txt")

MOTS_PAR_DEFAUT = ["python", "ordinateur", "programme", "variable", "fonction",
                   "boucle", "dictionnaire", "clavier", "ecran", "souris"]


def charger_liste_de_mots(chemin=FICHIER_MOTS):
    # Renvoie la liste des mots d'un fichier (un mot par ligne).
    # Si le fichier absent ou vide , on renvoie la liste par defaut
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            mots = [ligne.strip() for ligne in f if ligne.strip() != ""]

    except OSError:
        print("Fichier de mots absent :", os.path.basename(chemin), "(liste par defaut)")
        return list(MOTS_PAR_DEFAUT)

    return mots if mots != [] else list(MOTS_PAR_DEFAUT)


def choisir_mot(liste):
    #Renvoie un mot de la liste en MAJUSCULES, ou "" si la liste est vide."""
    if liste == []:
        return ""
    return random.choice(liste).upper()


def masque(mot, lettres_trouvees=""):
    #Construit le masque du mot : une liste de "_" de meme longueur.
    
    trouvees = lettres_trouvees.upper()
    return [lettre if lettre in trouvees else "_" for lettre in mot.upper()]


def masque_en_texte(mot, lettres_trouvees=""):
    """Meme masque, en chaine lisible : "_ _ T _ _ _"

    >>> masque_en_texte("PYTHON")
    '_ _ _ _ _ _'
    """
    return " ".join(masque(mot, lettres_trouvees))


def menu():
    # Tire un mot au hasard et affiche son masque
    mots = charger_liste_de_mots()
    while True:
        choix = input("\n1 - Tirer un mot   2 - Voir les mots : ").strip().lower()

        if choix == "1":
            mot = choisir_mot(mots)
            print("Mot :", mot, "->", masque_en_texte(mot))
        elif choix == "2":
            print(mots)


if __name__ == "__main__":
    # jeu d'essai du sujet
    print('masque("PYTHON")       ->', masque("PYTHON"))
    print('masque("PYTHON", "PT") ->', masque("PYTHON", "PT"))
    print('masque_en_texte(...)   ->', masque_en_texte("PYTHON", "PY"))
    print("liste vide             -> choisir_mot([]) =", repr(choisir_mot([])))

    # le fichier de mots est cree ici s'il n'existe pas encore
    if not os.path.exists(FICHIER_MOTS):
        with open(FICHIER_MOTS, "w", encoding="utf-8") as f:
            f.write("\n".join(MOTS_PAR_DEFAUT) + "\n")
        print("mots.txt cree avec", len(MOTS_PAR_DEFAUT), "mots")

    print("mots charges :", len(charger_liste_de_mots()))
    menu()