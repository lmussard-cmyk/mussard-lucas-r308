#Partie B du TP1

import random

ESSAIS = 10


def choisir_nombre_secret(borne_min=1, borne_max=100):
    # Renvoie un entier au hasard entre borne_min et borne_max inclus
    if borne_min > borne_max:
        borne_min, borne_max = borne_max, borne_min
    return random.randint(borne_min, borne_max)


def comparer(secret, proposition):
    # Renvoie -1 si trop petit, 1 si trop grand et 0 si on gagne
    if proposition < secret:
        return -1
    if proposition > secret:
        return 1
    return 0


def jouer_une_partie(borne_min=1, borne_max=100, essais=ESSAIS):
    # Joue une partie complete. Renvoie True si le joueur a gagné
    secret = choisir_nombre_secret(borne_min, borne_max)
    print("Nombre secret entre", borne_min, "et", borne_max, "-", essais, "essais")

    for numero in range(1, essais + 1):
        saisie = input("Essai " + str(numero) + "/" + str(essais) + " : ").strip()

        try:
            proposition = int(saisie)
        except ValueError:
            print("Entier attendu, essai perdu.")
            continue

        resultat = comparer(secret, proposition)

        if resultat == 0:
            print("Gagne !")
            return True
        print("Trop petit" if resultat == -1 else "Trop grand")

    print("Perdu ! Le nombre secret etait", secret)
    return False


def demander_les_bornes():
    # Demande les bornes (Entree = 1 et 100). Renvoie (borne_min, borne_max).
    minimum, maximum = 1, 100
    try:
        saisie = input("Borne minimale [1] : ").strip()
        if saisie:
            minimum = int(saisie)
        saisie = input("Borne maximale [100] : ").strip()
        if saisie:
            maximum = int(saisie)

    except ValueError:
        print("Valeur invalide, on garde 1 et 100")
        minimum, maximum = 1, 100

    if minimum >= maximum:
        print("Bornes incorrectes, on garde 1 et 100")
        minimum, maximum = 1, 100

    return minimum, maximum


def jeu_principal():
    #Enchaine les parties tant que le joueur repond oui a Rejouer
    while True:
        borne_min, borne_max = demander_les_bornes()
        jouer_une_partie(borne_min, borne_max)
        reponse = input("Rejouer ? (o/n) ").strip().lower()

        if reponse not in ("o", "oui", "y"):
            print("A bientot !")
            return


if __name__ == "__main__":
    jeu_principal()