from ordonnancement import *
from points_entree_sortie import *
from calcul_rang_circuit import calcul_rang


def afficher_matrice(matrice):
    # On affiche les sommets en ligne
    for sommet in range(len(matrice)):
        if sommet == 0:
            print('  |', sommet, end='')
        else:
            print('|', sommet, end='')

    # On affiche les sommets en colonne + les valeurs des arcs
    for i in range(len(matrice)):
        print()
        print(i, '|', end='')
        for j in range(len(matrice)):
            if matrice[i][j] is None:
                print('   ', end='')
            else:
                print('', matrice[i][j], '', end='')

    # Retour à la ligne
    print("")


def creer_matrice(chemin_fichier):
    with open(chemin_fichier, 'r') as fic:
        fichier = fic.read().splitlines()

        # Par défaut, split() prend en séparateur un espace
        for i in range(len(fichier)):
            fichier[i] = str(fichier[i]).split()
        vide = None

        nb_sommets = int(fichier[0][0])

        nb_arcs = int(fichier[1][0])

        # On déclare une matrice et on la remplit par défaut avec 'vide'
        matrice = [[vide for _ in range(nb_sommets)]
                   for _ in range(nb_sommets)]

        # On change les valeurs de la matrice avec les valuations
        for ligne in range(2, len(fichier)):
            matrice[int(fichier[ligne][0])][int(
                fichier[ligne][1])] = int(fichier[ligne][2])

        return matrice


def demo_graphe(chemin):
    matrice = creer_matrice(chemin)
    # On affiche la matrice
    print("\nMatrice d'adjacence. Une case vide indique une absence d'arc et un nombre indique la valeur de l'arc :")
    afficher_matrice(matrice)
    tableau_rangs = calcul_rang(matrice)
    if tableau_rangs is not None:
        print("\nCalcul des rangs [n° sommet, rang] :\n")
        print(*tableau_rangs, sep='\n')
    es_uniques = get_es_uniques(matrice)
    print()

    # 0 : entrée unique (le cas échéant)
    # 1 : sortie unique (le cas échéant)
    if es_uniques[0] is not None:
        print("Point d'entrée unique : ", es_uniques[0])
    else:
        print("Pas de point d'entrée unique.")
    if es_uniques[1] is not None:
        print("Point de sortie unique : ", es_uniques[1])
    else:
        print("Pas de point de sortie unique.")

    if es_uniques[0] is not None and \
            es_uniques[1] is not None and\
            tableau_rangs is not None:
        sommet_entree = str(es_uniques[0])
        sommet_sortie = str(es_uniques[1])

        date_tot = calendrier_date_tot(matrice, sommet_entree)
        date_tot_final = date_tot_maximum(date_tot)
        print("Date au plus tôt de fin de projet : ", date_tot_final)
        date_tard = calendrier_date_tard(
            matrice, sommet_sortie, date_tot_final)

        print("Sommet | Date au + tôt | Date au + tard")
        for i in range(len(matrice)):
            sommet = str(i)
            print(sommet, "       ",
                  date_tot[sommet], "             ", date_tard[sommet])
    else:
        print("Les conditions ne sont pas réunies pour calculer le calendrier des dates au plus tôt et au plus tard.")


def main():
    while True:
        # try/except pour gérer l'exception levée par int() qui ne sait pas convertir des lettres en chiffres
        try:
            reponse = input(
                "\nEntrez le numéro du graphe de test à analyser (entre 1 et 5) ou 'q' pour quitter : ")
            if reponse == "q":
                return
            elif 0 < int(reponse) < 6:
                demo_graphe('./test/graphe' + reponse + '.txt')
        except ValueError:
            print(
                "Veuillez saisir un chiffre entre 1 et 5 ou 'q' pour quitter le programme.")


main()
