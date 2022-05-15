CAR_VIDE = None


def get_entree_unique(mat_adj):
    entree = None

    # Recherche de sommets sans prédécesseurs
    for sommet in range(0, len(mat_adj)):
        if ([col[sommet] for col in mat_adj].count(CAR_VIDE)) == len(mat_adj):
            # si une entrée a déjà été trouvée : pas d'unicité
            if entree is not None:
                return None
            # sinon, on la stocke
            entree = sommet
    return entree


def get_sortie_unique(mat_adj):
    sortie = None

    # Recherche de sommets sans successeurs
    for sommet in range(0, len(mat_adj)):
        if mat_adj[sommet].count(CAR_VIDE) == len(mat_adj):
            # si une sortie a déjà été trouvée : pas d'unicité
            if sortie is not None:
                return None
            # sinon, on la stocke
            sortie = sommet
    return sortie


def get_es_uniques(mat_adj):
    # 0 : entrée unique (le cas échéant)
    # 1 : sortie unique (le cas échéant)
    e_s_uniques = [None, None]

    # Recherche de sommets sans prédécesseurs
    for sommet in range(0, len(mat_adj)):
        if ([col[sommet] for col in mat_adj].count(CAR_VIDE)) == len(mat_adj):
            # si une entrée a déjà été trouvée : pas d'unicité
            if e_s_uniques[0] is not None:
                e_s_uniques[0] = None
                break
            # sinon, on la stocke
            e_s_uniques[0] = sommet

    # Recherche de sommets sans successeurs
    for sommet in range(0, len(mat_adj)):
        if mat_adj[sommet].count(CAR_VIDE) == len(mat_adj):
            # si une sortie a déjà été trouvée : pas d'unicité
            if e_s_uniques[1] is not None:
                e_s_uniques[1] = None
                break
            # sinon, on la stocke
            e_s_uniques[1] = sommet
    return e_s_uniques


# Compte le nombre d'entr�es
def count_entrees(mat_adj):
    nb_entrees = 0

    for sommet in range(0, len(mat_adj)):
        if ([col[sommet] for col in mat_adj].count(CAR_VIDE)) == len(mat_adj):
            nb_entrees += 1
    return nb_entrees


# Compte le nombre de sorties
def count_sorties(mat_adj):
    nb_sorties = 0

    for sommet in range(0, len(mat_adj)):
        if mat_adj[sommet].count(CAR_VIDE) == len(mat_adj):
            nb_sorties += 1
    return nb_sorties


# Donne les valeurs qui sont en entr�es
def get_entrees(mat_adj):
    entrees = []

    for sommet in range(0, len(mat_adj)):
        if ([col[sommet] for col in mat_adj].count(CAR_VIDE)) == len(mat_adj):
            entrees.append(sommet)
    return entrees


# Donne les valeurs qui sont en sorties
def get_sorties(mat_adj):
    sorties = []

    for sommet in range(0, len(mat_adj)):
        if mat_adj[sommet].count(CAR_VIDE) == len(mat_adj):
            sorties.append(sommet)
    return sorties
