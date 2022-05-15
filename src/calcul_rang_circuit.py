import copy

from points_entree_sortie import get_entrees


# Calcule le rang et détecte la présence de circuit(s)
def calcul_rang(mat_adj):
    # Copie en profondeur pour éviter un effet de bord lors de la modification de la matrice locale
    mat_adj_local = copy.deepcopy(mat_adj)

    sommets_supprimes = []
    sommet_rangs = []
    rang = 1

    # Tq le nombre de points d'entrée éliminés != du nb de sommets du graphe
    while len(sommets_supprimes) != len(mat_adj_local):
        entrees_actuelles = get_entrees(mat_adj_local)
        # Si aucun nouveau(x) point d'entrée à cette étape, on a un circuit
        if nb_nouv_entrees(entrees_actuelles, sommets_supprimes) == 0:
            print("Circuit détecté, calcul des rangs impossible.")
            return
        for entree in entrees_actuelles:
            if entree not in sommets_supprimes:
                sommet_rangs.append([entree, rang])
                sommets_supprimes.append(entree)
                vider_ligne(entree, mat_adj_local)
        rang += 1
    return sommet_rangs


# Remplit la ligne avec le caractère vide (ici None)
# Ligne vide dans une matrice d'adjacence
def vider_ligne(index, m):
    for i in range(0, len(m)):
        m[index][i] = None


# Donne le nombre de nouvelles entrées
def nb_nouv_entrees(liste_actuelle, liste_totale):
    nb = 0
    for sommet in liste_actuelle:
        if sommet not in liste_totale:
            nb += 1
    return nb
