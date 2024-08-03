
# méthodes piles
def vide():
    return []


def est_vide(p):
    return p == []


def taille(p):
    return len(p)


def empiler(x, p):
    p.append(x)


def depiler(p):
    if est_vide(p)==False:
        return p.pop()


def sommet(p):
    return p[0]
