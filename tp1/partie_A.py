#Partie A du TP1

import os

FICHIER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "classe.txt")


def creer_classe():
    """Renvoie un dictionnaire vide."""
    return {}


def ajouter_etudiant(d, nom, note):
    #Ajoute ou met a jour un etudiant. Leve une ValueError si le nom ou la note est invalide.
    nom = nom.strip()
    if nom == "":
        raise ValueError("nom vide")
    try:
        d[nom] = float(note)
    except (TypeError, ValueError):
        raise ValueError("note invalide : " + repr(note))
    return d


def moyenne_classe(d):
    #Moyenne des notes, 0.0 si la classe est vide
    return sum(d.values()) / len(d) if d != {} else 0.0


def meilleur_etudiant(d):
    #(nom, note) du meilleur eleve ou rien/(None, 0.0) si la classe est vide
    if d == {}:
        return (None, 0.0)
    nom = max(d, key=d.get)
    return (nom, d[nom])


def sauvegarder(d, chemin):
    #Ecrit une ligne "nom:note" par etudiant. Renvoie False si l'ecriture echoue.
    try:
        with open(chemin, "w", encoding="utf-8") as f:
            for nom in sorted(d):
                f.write(nom + ":" + str(d[nom]) + "\n")
        return True
    except OSError as e:
        print("Ecriture impossible de", os.path.basename(chemin), ":", e)
        return False


def charger(chemin):
    #Relit un fichier "nom:note" , les lignes mal formees sont ignorées
    classe = {}
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except OSError:
        print("Fichier absent ou illisible :", os.path.basename(chemin))
        return classe

    for numero, ligne in enumerate(lignes, 1):
        morceaux = ligne.strip().split(":")
        if len(morceaux) != 2:
            print("Ligne", numero, "ignoree :", ligne.strip())
            continue
        try:
            ajouter_etudiant(classe, morceaux[0], morceaux[1])
        except ValueError as e:
            print("Ligne", numero, "ignoree :", e)
    return classe


if __name__ == "__main__":
    
    d = creer_classe()
    ajouter_etudiant(d, "Alice", 12)
    ajouter_etudiant(d, "Bob", 15)
    ajouter_etudiant(d, "Claire", 9.5)
    print("moyenne_classe(d)    ->", round(moyenne_classe(d), 2))
    print("meilleur_etudiant(d) ->", meilleur_etudiant(d))
    print("sauvegarde + relecture :", sauvegarder(d, FICHIER), charger(FICHIER))

    # cas limites du sujet : aucune erreur ne doit arreter le programme (c'est juste pour de la sécurité)
    print("classe vide :", meilleur_etudiant({}), moyenne_classe({}))
    print("fichier absent :", charger(os.path.join(os.path.dirname(FICHIER), "absent.txt")))
    mauvais = os.path.join(os.path.dirname(FICHIER), "mauvais.txt")
    with open(mauvais, "w", encoding="utf-8") as f:
        f.write("Alice:12\nBob:quinze\nligne cassee\n")
    print("lignes mal formees :", charger(mauvais))
    print("Bob mis a 18 :", ajouter_etudiant(d, "Bob", 18), "->", meilleur_etudiant(d))