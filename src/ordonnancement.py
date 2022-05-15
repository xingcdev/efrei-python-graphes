from math import inf
# Nous utilisons UNIQUEMENT la valeur "infini", pour Bellman seulement


def get_valeur_arc(sommet_depart, sommet_arrive, matrice):
    """Donne la valeur de l arc entre un sommet de départ et un sommet d'arrivée

    Args:
        sommet_depart (str): sommet de départ
        sommet_arrive (str): sommet d'arrivée
        matrice (list): matrice d'adjacence du graphe

    Returns:
        int: valeur de l'arc
    """
    return matrice[int(sommet_depart)][int(sommet_arrive)]


def date_tot_maximum(calendrier):
    """
    Renvoie la date au plus tôt la plus grande
    Args:
        calendrier: dates au plus tôt de chaque sommet

    Returns:
        int : valeur de la date au plus tôt la plus grande
    """
    return max(list(calendrier.values()))


def calendrier_date_tot(matrice, sommet_source):
    """
    Calcule les dates au plus tôt de chaque sommet en utilisant l'algorithme de Bellman-Ford.

    Args:
        matrice (list): la matrice adjacence du graphe
        sommet_source (str): sommet de départ du graphe

    Returns:
        list: dates au plus tôt de chaque sommet
    """
    date_tot = {}

    # Fixer la date au + tôt de tous les sommets à -∞ excepté le sommet source
    for index in range(len(matrice)):
        sommet = str(index)
        date_tot[sommet] = -inf  # -∞
    date_tot[sommet_source] = 0

    for i in range(len(matrice) - 1):
        for ligne in range(len(matrice)):
            for col in range(len(matrice)):
                sommet_depart = str(ligne)
                sommet_arrive = str(col)
                valeur_arc = get_valeur_arc(
                    sommet_depart, sommet_arrive, matrice)

                # On détermine la date au + tôt du sommet en prenant la plus grande valeur de date de ses prédécesseurs
                # La valeur se calcule ainsi : date au + tôt du prédécesseur + valeur d'arc
                if valeur_arc is not None:
                    if date_tot[sommet_depart] + valeur_arc > date_tot[sommet_arrive]:
                        date_tot[sommet_arrive] = date_tot[sommet_depart] + \
                                                  valeur_arc
    return date_tot


def calendrier_date_tard(matrice, sommet_final, date_tot_final):
    """
    Calcule les dates au plus tard de chaque sommet en utilisant l'algorithme de Bellman-Ford.

    Args:
        matrice (list): la matrice d'adjacence du graphe
        sommet_final (str): le sommet final du graphe
        date_tot_final (int): la date au plus tard du sommet final

    Returns:
        list: dates au plus tard de chaque sommet
    """
    date_tard = {}

    # Fixer la date au + tard de tous les sommets à +∞ excepté le sommet final
    for index in range(len(matrice)):
        sommet = str(index)
        date_tard[sommet] = inf  # +∞
    date_tard[sommet_final] = date_tot_final

    for i in range(len(matrice) - 1):
        for ligne in range(len(matrice)):
            for col in range(len(matrice)):
                sommet_depart = str(ligne)
                sommet_arrive = str(col)
                valeur_arc = get_valeur_arc(
                    sommet_depart, sommet_arrive, matrice)

                # On détermine la date au + tard du sommet en prenant la plus petite valeur de ses successeurs.
                # La valeur se calcule ainsi : date au + tard du successeur - valeur d'arc
                if valeur_arc is not None:
                    if date_tard[sommet_arrive] - valeur_arc < date_tard[sommet_depart]:
                        date_tard[sommet_depart] = date_tard[sommet_arrive] - \
                                                   valeur_arc
    return date_tard
