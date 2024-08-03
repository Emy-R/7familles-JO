
import pygame
from pygame.locals import *
from random import shuffle
from methodes import *

# Définition des constantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
BOUTON_WIDTH = 130
BOUTON_HEIGHT = 130
CARD_WIDTH = 100
CARD_HEIGHT = 150
PILE_OFFSET_X = 50
PILE_OFFSET_Y = 300
PICK_OFFSET_X = 50
PICK_OFFSET_Y = 50
CARD_SPACING = 45
VERTICAL_OFFSET = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



# Définition de la classe Carte
class Carte:
    def __init__(self, famille, valeur):
        self.famille = famille
        self.valeur = valeur
        self.selected = False
        self.x = 0
        self.y = 0


# Définition de la classe Pile
class Pile:
    def __init__(self, x, y):
        self.cartes = []
        self.x = x
        self.y = y

    def ajouter_carte(self, carte):
        self.cartes.append(carte)

    def retirer_carte(self):
        if len(self.cartes) > 0:
            return self.cartes.pop(0)
        else:
            return None


# Définition de la classe Jeu
class Jeu:
    def __init__(self):
        self.piles = {}
        self.joueur1 = Pile(PILE_OFFSET_X, PILE_OFFSET_Y)
        self.joueur2 = Pile(PILE_OFFSET_X, PILE_OFFSET_Y - CARD_HEIGHT - CARD_SPACING)
        self.pioche = Pile(PICK_OFFSET_X, PICK_OFFSET_Y)
        self.jeu_principal = Pile(PICK_OFFSET_X + CARD_WIDTH + CARD_SPACING, PICK_OFFSET_Y)
        self.tour_joueur = 1

    def initialiser(self):
        familles = ['Athlétisme', 'Escrime', 'Gymnastique', 'Badminton', 'Judo', "Tir à l'arc", 'Natation']
        valeurs = ['Espoir', 'Médaillé', 'Novice', 'Vétéran', 'Recordman', 'Paralympique']
        cartes = [Carte(famille, valeur) for famille in familles for valeur in valeurs]
        shuffle(cartes)
        self.pioche.cartes = cartes

    def distribuer_cartes(self):
        for _ in range(7):
            self.joueur1.ajouter_carte(self.pioche.retirer_carte())
            self.joueur2.ajouter_carte(self.pioche.retirer_carte())

    def initialiser_piles(self):
        self.piles['joueur1'] = self.joueur1
        self.piles['joueur2'] = self.joueur2
        self.piles['pioche'] = self.pioche
        self.piles['jeu_principal'] = self.jeu_principal

    def joueur_actuel(self):
        return self.joueur1 if self.tour_joueur == 1 else self.joueur2

    def passer_tour(self):
        self.tour_joueur = 1 if self.tour_joueur == 2 else 2

    def afficher(self):
        for joueur, pile in self.piles.items():
            if isinstance(pile, Pile):
                print(f"Joueur {joueur}:", [(carte.valeur, carte.famille) for carte in pile.cartes])

    def verifier_famille_complete(self, pile):
        familles = {}
        for carte in pile.cartes:
            if carte.famille not in familles:
                familles[carte.famille] = 1
            else:
                familles[carte.famille] += 1

        for famille, count in familles.items():
            if count >= 6:
                return famille

        return None

    def retirer_famille_complete(self, famille):
        for pile in [self.joueur1, self.joueur2]:
            cartes_famille_complete = [carte for carte in pile.cartes if carte.famille == famille]
            for carte in cartes_famille_complete:
                pile.cartes.remove(carte)



# Initialisation de Pygame

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Jeu des 7 familles")

# Plateau
plateau = pygame.image.load('Images/plateau.png').convert_alpha()
plateau = pygame.transform.scale(plateau, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Cartes de jeux
# Athlétisme
athletisme_espoir = pygame.image.load('Images/athletisme_espoir.png').convert_alpha()
athletisme_espoir = pygame.transform.scale(athletisme_espoir, (CARD_WIDTH*2, CARD_HEIGHT*2))

athletisme_médaillé = pygame.image.load('Images/athletisme_medaille.png').convert_alpha()
athletisme_médaillé = pygame.transform.scale(athletisme_médaillé, (CARD_WIDTH*2, CARD_HEIGHT*2))

athletisme_novice = pygame.image.load('Images/athletisme_novice.png').convert_alpha()
athletisme_novice = pygame.transform.scale(athletisme_novice, (CARD_WIDTH*2, CARD_HEIGHT*2))

athletisme_vétéran = pygame.image.load('Images/athletisme_veteran.png').convert_alpha()
athletisme_vétéran = pygame.transform.scale(athletisme_vétéran, (CARD_WIDTH*2, CARD_HEIGHT*2))

athletisme_recordman = pygame.image.load('Images/athletisme_recordman.png').convert_alpha()
athletisme_recordman = pygame.transform.scale(athletisme_recordman, (CARD_WIDTH*2, CARD_HEIGHT*2))

athletisme_paralympique = pygame.image.load('Images/athletisme_paralympique.png').convert_alpha()
athletisme_paralympique = pygame.transform.scale(athletisme_paralympique, (CARD_WIDTH*2, CARD_HEIGHT*2))


# Escrime
escrime_espoir = pygame.image.load('Images/escrime_espoir.png').convert_alpha()
escrime_espoir = pygame.transform.scale(escrime_espoir, (CARD_WIDTH*2, CARD_HEIGHT*2))

escrime_médaillé = pygame.image.load('Images/escrime_medaille.png').convert_alpha()
escrime_médaillé = pygame.transform.scale(escrime_médaillé, (CARD_WIDTH*2, CARD_HEIGHT*2))

escrime_novice = pygame.image.load('Images/escrime_novice.png').convert_alpha()
escrime_novice = pygame.transform.scale(escrime_novice, (CARD_WIDTH*2, CARD_HEIGHT*2))

escrime_vétéran = pygame.image.load('Images/escrime_veteran.png').convert_alpha()
escrime_vétéran = pygame.transform.scale(escrime_vétéran, (CARD_WIDTH*2, CARD_HEIGHT*2))

escrime_recordman = pygame.image.load('Images/escrime_recordman.png').convert_alpha()
escrime_recordman = pygame.transform.scale(escrime_recordman, (CARD_WIDTH*2, CARD_HEIGHT*2))

escrime_paralympique = pygame.image.load('Images/escrime_paralympique.png').convert_alpha()
escrime_paralympique = pygame.transform.scale(escrime_paralympique, (CARD_WIDTH*2, CARD_HEIGHT*2))


# Gymnastique
gymnastique_espoir = pygame.image.load('Images/gymnastique_espoir.png').convert_alpha()
gymnastique_espoir = pygame.transform.scale(gymnastique_espoir, (CARD_WIDTH*2, CARD_HEIGHT*2))

gymnastique_médaillé = pygame.image.load('Images/gymnastique_medaille.png').convert_alpha()
gymnastique_médaillé = pygame.transform.scale(gymnastique_médaillé, (CARD_WIDTH*2, CARD_HEIGHT*2))

gymnastique_novice = pygame.image.load('Images/gymnastique_novice.png').convert_alpha()
gymnastique_novice = pygame.transform.scale(gymnastique_novice, (CARD_WIDTH*2, CARD_HEIGHT*2))

gymnastique_vétéran = pygame.image.load('Images/gymnastique_veteran.png').convert_alpha()
gymnastique_vétéran = pygame.transform.scale(gymnastique_vétéran, (CARD_WIDTH*2, CARD_HEIGHT*2))

gymnastique_recordman = pygame.image.load('Images/gymnastique_recordman.png').convert_alpha()
gymnastique_recordman = pygame.transform.scale(gymnastique_recordman, (CARD_WIDTH*2, CARD_HEIGHT*2))

gymnastique_paralympique = pygame.image.load('Images/gymnastique_paralympique.png').convert_alpha()
gymnastique_paralympique = pygame.transform.scale(gymnastique_paralympique, (CARD_WIDTH*2, CARD_HEIGHT*2))

# Badminton
badminton_espoir = pygame.image.load('Images/badminton_espoir.png').convert_alpha()
badminton_espoir = pygame.transform.scale(badminton_espoir, (CARD_WIDTH*2, CARD_HEIGHT*2))

badminton_médaillé = pygame.image.load('Images/badminton_medaille.png').convert_alpha()
badminton_médaillé = pygame.transform.scale(badminton_médaillé, (CARD_WIDTH*2, CARD_HEIGHT*2))

badminton_novice = pygame.image.load('Images/badminton_novice.png').convert_alpha()
badminton_novice = pygame.transform.scale(badminton_novice, (CARD_WIDTH*2, CARD_HEIGHT*2))

badminton_vétéran = pygame.image.load('Images/badminton_veteran.png').convert_alpha()
badminton_vétéran = pygame.transform.scale(badminton_vétéran, (CARD_WIDTH*2, CARD_HEIGHT*2))

badminton_recordman = pygame.image.load('Images/badminton_recordman.png').convert_alpha()
badminton_recordman = pygame.transform.scale(badminton_recordman, (CARD_WIDTH*2, CARD_HEIGHT*2))

badminton_paralympique = pygame.image.load('Images/badminton_paralympique.png').convert_alpha()
badminton_paralympique = pygame.transform.scale(badminton_paralympique, (CARD_WIDTH*2, CARD_HEIGHT*2))


# Judo
judo_espoir = pygame.image.load('Images/judo_espoir.png').convert_alpha()
judo_espoir = pygame.transform.scale(judo_espoir, (CARD_WIDTH*2, CARD_HEIGHT*2))

judo_médaillé = pygame.image.load('Images/judo_medaille.png').convert_alpha()
judo_médaillé = pygame.transform.scale(judo_médaillé, (CARD_WIDTH*2, CARD_HEIGHT*2))

judo_novice = pygame.image.load('Images/judo_novice.png').convert_alpha()
judo_novice = pygame.transform.scale(judo_novice, (CARD_WIDTH*2, CARD_HEIGHT*2))

judo_vétéran = pygame.image.load('Images/judo_veteran.png').convert_alpha()
judo_vétéran = pygame.transform.scale(judo_vétéran, (CARD_WIDTH*2, CARD_HEIGHT*2))

judo_recordman = pygame.image.load('Images/judo_recordman.png').convert_alpha()
judo_recordman = pygame.transform.scale(judo_recordman, (CARD_WIDTH*2, CARD_HEIGHT*2))

judo_paralympique = pygame.image.load('Images/judo_paralympique.png').convert_alpha()
judo_paralympique = pygame.transform.scale(judo_paralympique, (CARD_WIDTH*2, CARD_HEIGHT*2))


# Tir à l'arc
tir_a_l_arc_espoir = pygame.image.load('Images/tiralarc_espoir.png').convert_alpha()
tir_a_l_arc_espoir = pygame.transform.scale(tir_a_l_arc_espoir, (CARD_WIDTH*2, CARD_HEIGHT*2))

tir_a_l_arc_médaillé = pygame.image.load('Images/tiralarc_medaille.png').convert_alpha()
tir_a_l_arc_médaillé = pygame.transform.scale(tir_a_l_arc_médaillé, (CARD_WIDTH*2, CARD_HEIGHT*2))

tir_a_l_arc_novice = pygame.image.load('Images/tiralarc_novice.png').convert_alpha()
tir_a_l_arc_novice = pygame.transform.scale(tir_a_l_arc_novice, (CARD_WIDTH*2, CARD_HEIGHT*2))

tir_a_l_arc_vétéran = pygame.image.load('Images/tiralarc_veteran.png').convert_alpha()
tir_a_l_arc_vétéran = pygame.transform.scale(tir_a_l_arc_vétéran, (CARD_WIDTH*2, CARD_HEIGHT*2))

tir_a_l_arc_recordman = pygame.image.load('Images/tiralarc_recordman.png').convert_alpha()
tir_a_l_arc_recordman = pygame.transform.scale(tir_a_l_arc_recordman, (CARD_WIDTH*2, CARD_HEIGHT*2))

tir_a_l_arc_paralympique = pygame.image.load('Images/tiralarc_paralympique.png').convert_alpha()
tir_a_l_arc_paralympique = pygame.transform.scale(tir_a_l_arc_paralympique, (CARD_WIDTH*2, CARD_HEIGHT*2))


# Natation
natation_espoir = pygame.image.load('Images/natation_espoir.png').convert_alpha()
natation_espoir = pygame.transform.scale(natation_espoir, (CARD_WIDTH*2, CARD_HEIGHT*2))

natation_médaillé = pygame.image.load('Images/natation_medaille.png').convert_alpha()
natation_médaillé = pygame.transform.scale(natation_médaillé, (CARD_WIDTH*2, CARD_HEIGHT*2))

natation_novice = pygame.image.load('Images/natation_novice.png').convert_alpha()
natation_novice = pygame.transform.scale(natation_novice, (CARD_WIDTH*2, CARD_HEIGHT*2))

natation_vétéran = pygame.image.load('Images/natation_veteran.png').convert_alpha()
natation_vétéran = pygame.transform.scale(natation_vétéran, (CARD_WIDTH*2, CARD_HEIGHT*2))

natation_recordman = pygame.image.load('Images/natation_recordman.png').convert_alpha()
natation_recordman = pygame.transform.scale(natation_recordman, (CARD_WIDTH*2, CARD_HEIGHT*2))

natation_paralympique = pygame.image.load('Images/natation_paralympique.png').convert_alpha()
natation_paralympique = pygame.transform.scale(natation_paralympique, (CARD_WIDTH*2, CARD_HEIGHT*2))


#boutons roles
# paralympique
paralympique = pygame.image.load('Images/bouton_paralympique.png').convert_alpha()
paralympique = pygame.transform.scale(paralympique, (BOUTON_WIDTH*2, BOUTON_HEIGHT*2))

# recordman
recordman = pygame.image.load('Images/bouton_recordman.png').convert_alpha()
recordman = pygame.transform.scale(recordman, (BOUTON_WIDTH*2, BOUTON_HEIGHT*2))

# novice
novice = pygame.image.load('Images/bouton_novice.png').convert_alpha()
novice = pygame.transform.scale(novice, (BOUTON_WIDTH*2, BOUTON_HEIGHT*2))

# vétéran
veteran = pygame.image.load('Images/bouton_veteran.png').convert_alpha()
veteran = pygame.transform.scale(veteran, (BOUTON_WIDTH*2, BOUTON_HEIGHT*2))

# médaillé
medaille = pygame.image.load('Images/bouton_medaille.png').convert_alpha()
medaille = pygame.transform.scale(medaille, (BOUTON_WIDTH*2, BOUTON_HEIGHT*2))

# espoir
espoir = pygame.image.load('Images/bouton_espoir.png').convert_alpha()
espoir = pygame.transform.scale(espoir, (BOUTON_WIDTH*2, BOUTON_HEIGHT*2))

stack_gym = pygame.image.load("Images/stack_pink.png").convert_alpha()
stack_gym = pygame.transform.scale(stack_gym, (125, 115))

stack_natation = pygame.image.load("Images/stack_blue.png").convert_alpha()
stack_natation = pygame.transform.scale(stack_natation, (130, 110))

stack_judo = pygame.image.load("Images/stack_brown.png").convert_alpha()
stack_judo = pygame.transform.scale(stack_judo, (115, 110))

stack_escrime = pygame.image.load("Images/stack_grey.png").convert_alpha()
stack_escrime = pygame.transform.scale(stack_escrime, (105, 105))

stack_bad = pygame.image.load("Images/stack_yellow.png").convert_alpha()
stack_bad = pygame.transform.scale(stack_bad, (120, 100))

stack_athletisme = pygame.image.load("Images/stack_orange.png").convert_alpha()
stack_athletisme = pygame.transform.scale(stack_athletisme, (120, 105))

stack_tiralarc = pygame.image.load("Images/stack_green.png").convert_alpha()
stack_tiralarc = pygame.transform.scale(stack_tiralarc, (120, 110))


# Initialisation du jeu
jeu = Jeu()
jeu.initialiser()
jeu.distribuer_cartes()
jeu.initialiser_piles()
jeu.afficher()

font = pygame.font.SysFont(None, 36)

def musique():
    #Inistialisation de la musique
    pygame.mixer.music.load('Music/music_3.mp3')
    #Volume de la musique
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

musique()

# fonction pour lever les cartes d'une même famille
def lever_cartes_famille(carte):
    # Variable pour stocker l'état de sélection de la famille sélectionnée
    selected_state = carte.selected

    for pile in [jeu.joueur1, jeu.joueur2]:
        for c in pile.cartes:
            if c.famille == carte.famille:
                if selected_state:  # Garder l'état de sélection inchangé si la famille a été sélectionnée
                    c.y += VERTICAL_OFFSET if c.selected else 0
                else:
                    if c.selected:
                        c.y += VERTICAL_OFFSET  # Revenir à la position initiale si déjà levée
                    else:
                        c.y -= VERTICAL_OFFSET  # Lever la carte
                c.selected = selected_state  # Garder l'état de sélection inchangé


def set_cartes_positions(pile):
    # Nombre total de cartes dans la pile
    total_cartes = len(pile.cartes)

    # Nombre de cartes par ligne
    cartes_par_ligne = 7

    # Calcul de la position x initiale pour centrer les cartes sur la largeur de l'écran avec une bordure de 30 pixels
    total_width = cartes_par_ligne * (CARD_WIDTH * 0.75) + (cartes_par_ligne - 1) * (CARD_WIDTH * 0.25) + CARD_SPACING
    x_offset = (SCREEN_WIDTH - total_width) / 9

    # Position y initiale pour la première ligne
    y_offset = SCREEN_HEIGHT - CARD_HEIGHT - PILE_OFFSET_Y + 30

    # Compteur de cartes dans la première ligne
    nb_cartes_first_row = 0

    # Parcourir les cartes pour la première ligne
    for i, carte in enumerate(pile.cartes):
        if i < cartes_par_ligne:  # Vérifier si la carte appartient à la première ligne
            # Limiter les cartes pour qu'elles ne sortent pas de la fenêtre
            carte.x = max(30, min(x_offset, SCREEN_WIDTH - 30 - CARD_WIDTH))
            carte.y = max(30, min(y_offset, SCREEN_HEIGHT - 30 - CARD_HEIGHT))
            x_offset += CARD_WIDTH * 0.75 + CARD_SPACING  # Décalage pour superposer légèrement les cartes
            nb_cartes_first_row += 1

    # Si la première ligne est pleine, réinitialiser l'offset horizontal pour la deuxième ligne
    if nb_cartes_first_row == cartes_par_ligne:
        x_offset = (SCREEN_WIDTH - total_width) / 6

    # Position y initiale pour la deuxième ligne
    y_offset += CARD_HEIGHT + CARD_SPACING - 75

    # Parcourir les cartes pour la deuxième ligne
    for i, carte in enumerate(pile.cartes):
        if i >= cartes_par_ligne:  # Vérifier si la carte appartient à la deuxième ligne
            # Limiter les cartes pour qu'elles ne sortent pas de la fenêtre
            carte.x = max(30, min(x_offset, SCREEN_WIDTH - 30 - CARD_WIDTH))
            carte.y = max(30, min(y_offset, SCREEN_HEIGHT - 30 - CARD_HEIGHT))
            x_offset += CARD_WIDTH * 0.75 + CARD_SPACING  # Décalage pour superposer légèrement les cartes

    # Position y initiale pour la troisième ligne
    x_offset = (SCREEN_WIDTH - total_width) / 3
    y_offset += CARD_HEIGHT + CARD_SPACING - 75

    # Parcourir les cartes pour la troisième ligne
    for i, carte in enumerate(pile.cartes):
        if 2 * cartes_par_ligne <= i < total_cartes:  # Vérifier si la carte appartient à la troisième ligne
            # Limiter les cartes pour qu'elles ne sortent pas de la fenêtre
            carte.x = max(30, min(x_offset, SCREEN_WIDTH - 30 - CARD_WIDTH))
            carte.y = max(30, min(y_offset, SCREEN_HEIGHT - 30 - CARD_HEIGHT))
            x_offset += CARD_WIDTH * 0.75 + CARD_SPACING  # Décalage pour superposer légèrement les cartes

        if carte.selected:
            lever_cartes_famille(carte)


set_cartes_positions(jeu.joueur1)
set_cartes_positions(jeu.joueur2)

def demand_card(jeu, famille_demandee, membre_famille):
    # Vérifier si la famille demandée est présente dans le paquet de l'autre joueur
    adversaire = jeu.joueur2 if jeu.tour_joueur == 1 else jeu.joueur1
    for carte in adversaire.cartes:
        if carte.famille == famille_demandee:
            # Si la famille est présente, retirer la carte du paquet de l'adversaire et l'ajouter au paquet du joueur actuel
            adversaire.cartes.remove(carte)
            jeu.joueur_actuel().ajouter_carte(carte)
            set_cartes_positions(jeu.joueur1)
            set_cartes_positions(jeu.joueur2)
            jeu.afficher()
            return

    # Si la famille n'est pas présente dans le paquet de l'adversaire, le joueur actuel pioche une carte
    carte_piochee = jeu.pioche.retirer_carte()
    if carte_piochee:
        jeu.joueur_actuel().ajouter_carte(carte_piochee)
        set_cartes_positions(jeu.joueur_actuel())
        jeu.afficher()


# Fonction pour afficher le contenu de chaque pile dans la console
def afficher_piles(piles):
    for nom_pile, pile in piles.items():
        print(f"Pile {nom_pile}: {[carte.valeur for carte in pile]}")

# Fonction pour vérifier si toutes les piles sont complètes
def toutes_piles_complete(piles_familles):
    return all(taille(pile) == 6 for pile in piles_familles.values())


# Définition des boutons représentant les membres de la famille
buttons = {
    "Espoir": pygame.Rect(770, 0, BOUTON_WIDTH*2, BOUTON_HEIGHT*2),
    "Médaillé": pygame.Rect(770, 75, BOUTON_WIDTH*2, BOUTON_HEIGHT*2),
    "Novice": pygame.Rect(600, 75, BOUTON_WIDTH*2, BOUTON_HEIGHT*2),
    "Vétéran": pygame.Rect(600, -75, BOUTON_WIDTH*2, BOUTON_HEIGHT*2),
    "Recordman": pygame.Rect(600, 0, BOUTON_WIDTH*2, BOUTON_HEIGHT*2),
    "Paralympique": pygame.Rect(770, -75, BOUTON_WIDTH*2, BOUTON_HEIGHT*2)
}

current_player = 1
# Création d'un dictionnaire pour stocker les piles de chaque famille
familles = ['Athlétisme', 'Escrime', 'Gymnastique', 'Badminton', 'Judo', "Tir à l'arc", 'Natation']



jeu.initialiser_piles()

# Création des piles pour chaque famille
piles_familles = {famille: vide() for famille in familles}

# Boucle principale
running = True
selected_family = None  # Variable pour stocker la famille sélectionnée par le joueur
game_over = False  # Variable pour indiquer si la partie est terminée

while running:
    screen.blit(plateau, (0, 0))
    screen.blit(paralympique, (770, -75))
    screen.blit(espoir, (770, 0))
    screen.blit(medaille, (770, 75))
    screen.blit(veteran, (600, -75))
    screen.blit(recordman, (600, 0))
    screen.blit(novice, (600, 75))


    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False  # Condition de sortie de la boucle principale
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_player == 1:  # Vérifier si c'est le tour du joueur 1
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Vérifier si le joueur clique sur une carte de son paquet
                for carte in jeu.joueur1.cartes:
                    if carte.x < mouse_x < carte.x + CARD_WIDTH * 1.5 and carte.y < mouse_y < carte.y + CARD_HEIGHT:
                        selected_family = carte.famille
                        lever_cartes_famille(carte)  # Appel à la fonction pour lever les cartes de la famille
                        break
                # Vérifier si le joueur clique sur l'un des boutons représentant les membres de la famille
                for member, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        if selected_family:
                            demand_card(jeu, selected_family, member)
                            selected_family = None
                            current_player = 2  # Passer au tour du joueur 2
                        break

    # Passer au tour de l'ordinateur
    if current_player == 2:
        # Vérifier si l'ordinateur possède une carte de la même famille
        possede_carte_meme_famille = any(carte.famille == selected_family for carte in jeu.joueur2.cartes)

        if possede_carte_meme_famille:
            # Retirer la carte de la famille demandée du paquet 2 et l'ajouter au paquet 1
            for carte in jeu.joueur2.cartes[:]:  # Utilisation de [:] pour itérer sur une copie de la liste
                if carte.famille == selected_family:
                    jeu.joueur2.cartes.remove(carte)
                    jeu.joueur1.ajouter_carte(carte)
                    set_cartes_positions(jeu.joueur1)
                    set_cartes_positions(jeu.joueur2)
                    jeu.afficher()

            # Vérifier si la famille complète est dans le paquet 1
            if jeu.verifier_famille_complete(jeu.joueur1):
                famille_complete = jeu.joueur1.obtenir_famille_complete(selected_family)
                jeu.joueur1.cartes.extend(famille_complete)
                jeu.joueur1.cartes = []
                set_cartes_positions(jeu.joueur1)
                set_cartes_positions(jeu.joueur2)
                jeu.afficher()
                current_player = 1  # Passer au tour du joueur 1

        else:
            # L'ordinateur pioche une carte
            carte_piochee = jeu.pioche.retirer_carte()
            if carte_piochee:
                jeu.joueur2.ajouter_carte(carte_piochee)
                set_cartes_positions(jeu.joueur2)
                jeu.afficher()

        current_player = 1  # Passer au tour du joueur 1
        # Vérifier si une famille est complète pour le joueur 1
        famille_complete_joueur1 = jeu.verifier_famille_complete(jeu.joueur1)
        if famille_complete_joueur1:
            cartes_famille_complete_joueur1 = [carte for carte in jeu.joueur1.cartes if
                                               carte.famille == famille_complete_joueur1]
            jeu.retirer_famille_complete(famille_complete_joueur1)  # Retirer la famille complète des piles des joueurs
            piles_familles[famille_complete_joueur1].extend(
                cartes_famille_complete_joueur1)  # Ajouter les cartes à la pile correspondante
            set_cartes_positions(jeu.joueur1)  # Réorganiser les cartes dans la pile du joueur 1
            set_cartes_positions(jeu.joueur2)  # Réorganiser les cartes dans la pile du joueur 2

        # Vérifier si une famille est complète pour le joueur 2 (si nécessaire)
        famille_complete_joueur2 = jeu.verifier_famille_complete(jeu.joueur2)
        if famille_complete_joueur2:
            cartes_famille_complete_joueur2 = [carte for carte in jeu.joueur2.cartes if
                                               carte.famille == famille_complete_joueur2]
            jeu.retirer_famille_complete(famille_complete_joueur2)  # Retirer la famille complète des piles des joueurs
            piles_familles[famille_complete_joueur2].extend(
                cartes_famille_complete_joueur2)  # Ajouter les cartes à la pile correspondante
            set_cartes_positions(jeu.joueur1)  # Réorganiser les cartes dans la pile du joueur 1
            set_cartes_positions(jeu.joueur2)  # Réorganiser les cartes dans la pile du joueur 2

        afficher_piles(piles_familles)
    # Affichage des cartes du joueur 1
    for carte in jeu.joueur1.cartes:
        color = BLACK if not carte.selected else (0, 255, 0)  # Mettre en vert si la carte est sélectionnée
        if "Athlétisme" in carte.famille:
            if "Espoir" in carte.valeur:
                screen.blit(athletisme_espoir, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Médaillé" in carte.valeur:
                screen.blit(athletisme_médaillé, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Novice" in carte.valeur:
                screen.blit(athletisme_novice, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Vétéran" in carte.valeur:
                screen.blit(athletisme_vétéran, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Recordman" in carte.valeur:
                screen.blit(athletisme_recordman, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Paralympique" in carte.valeur:
                screen.blit(athletisme_paralympique, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))

        if "Escrime" in carte.famille:
            if "Espoir" in carte.valeur:
                screen.blit(escrime_espoir, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Médaillé" in carte.valeur:
                screen.blit(escrime_médaillé, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Novice" in carte.valeur:
                screen.blit(escrime_novice, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Vétéran" in carte.valeur:
                screen.blit(escrime_vétéran, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Recordman" in carte.valeur:
                screen.blit(escrime_recordman, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Paralympique" in carte.valeur:
                screen.blit(escrime_paralympique, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))

        if "Gymnastique" in carte.famille:
            if "Espoir" in carte.valeur:
                screen.blit(gymnastique_espoir, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Médaillé" in carte.valeur:
                screen.blit(gymnastique_médaillé, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Novice" in carte.valeur:
                screen.blit(gymnastique_novice, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Vétéran" in carte.valeur:
                screen.blit(gymnastique_vétéran, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Recordman" in carte.valeur:
                screen.blit(gymnastique_recordman, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Paralympique" in carte.valeur:
                screen.blit(gymnastique_paralympique, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))

        if "Badminton" in carte.famille:
            if "Espoir" in carte.valeur:
                screen.blit(badminton_espoir, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Médaillé" in carte.valeur:
                screen.blit(badminton_médaillé, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Novice" in carte.valeur:
                screen.blit(badminton_novice, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Vétéran" in carte.valeur:
                screen.blit(badminton_vétéran, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Recordman" in carte.valeur:
                screen.blit(badminton_recordman, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Paralympique" in carte.valeur:
                screen.blit(badminton_paralympique, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))

        if "Judo" in carte.famille:
            if "Espoir" in carte.valeur:
                screen.blit(judo_espoir, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Médaillé" in carte.valeur:
                screen.blit(judo_médaillé, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Novice" in carte.valeur:
                screen.blit(judo_novice, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Vétéran" in carte.valeur:
                screen.blit(judo_vétéran, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Recordman" in carte.valeur:
                screen.blit(judo_recordman, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Paralympique" in carte.valeur:
                screen.blit(judo_paralympique, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))

        if "Tir à l'arc" in carte.famille:
            if "Espoir" in carte.valeur:
                screen.blit(tir_a_l_arc_espoir, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Médaillé" in carte.valeur:
                screen.blit(tir_a_l_arc_médaillé, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Novice" in carte.valeur:
                screen.blit(tir_a_l_arc_novice, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Vétéran" in carte.valeur:
                screen.blit(tir_a_l_arc_vétéran, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Recordman" in carte.valeur:
                screen.blit(tir_a_l_arc_recordman, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Paralympique" in carte.valeur:
                screen.blit(tir_a_l_arc_paralympique, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))

        if "Natation" in carte.famille:
            if "Espoir" in carte.valeur:
                screen.blit(natation_espoir, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Médaillé" in carte.valeur:
                screen.blit(natation_médaillé, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Novice" in carte.valeur:
                screen.blit(natation_novice, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Vétéran" in carte.valeur:
                screen.blit(natation_vétéran, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Recordman" in carte.valeur:
                screen.blit(natation_recordman, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))
            elif "Paralympique" in carte.valeur:
                screen.blit(natation_paralympique, (carte.x, carte.y, CARD_WIDTH, CARD_HEIGHT))


        # Affichage des images des piles seulement si la taille de la pile correspondante est de 6 éléments
        if taille(piles_familles["Tir à l'arc"]) == 6:
            screen.blit(stack_tiralarc, (200, 60))
        if taille(piles_familles["Badminton"]) == 6:
            screen.blit(stack_bad, (350, 65))
        if taille(piles_familles["Gymnastique"]) == 6:
            screen.blit(stack_gym, (500, 58))
        # ---------
        if taille(piles_familles["Natation"]) == 6:
            screen.blit(stack_natation, (170, 183))
        if taille(piles_familles["Judo"]) == 6:
            screen.blit(stack_judo, (295, 180))
        if taille(piles_familles["Escrime"]) == 6:
            screen.blit(stack_escrime, (425, 183))
        if taille(piles_familles["Athlétisme"]) == 6:
            screen.blit(stack_athletisme, (533, 185))

    # Affichage des cartes de la pioche
    # pygame.draw.rect(screen, BLACK, (jeu.pioche.x, jeu.pioche.y, CARD_WIDTH, CARD_HEIGHT), 2)

    text = font.render("Pioche", True, BLACK)
    pioche_img = pygame.image.load('Images/pioche.png').convert_alpha()
    pioche_img = pygame.transform.scale(pioche_img, (CARD_WIDTH*2, CARD_HEIGHT*2))
    screen.blit(pioche_img,(jeu.pioche.x-40, jeu.pioche.y-50, CARD_WIDTH, CARD_HEIGHT))
    #screen.blit(text, (jeu.pioche.x + 10, jeu.pioche.y + 10))

    pygame.display.flip()
    clock.tick(60)

    # Vérifier si toutes les piles sont complètes
    if toutes_piles_complete(piles_familles):
        # Déterminer le nombre de familles rassemblées par chaque joueur
        nb_familles_joueur1 = sum(1 for taille_pile in piles_familles.values() if taille_pile == 6)
        nb_familles_joueur2 = 7 - nb_familles_joueur1
        # Déterminer le gagnant en fonction du nombre de familles rassemblées
        if nb_familles_joueur1 > nb_familles_joueur2:
            winner_name = "Phryge"
        elif nb_familles_joueur2 > nb_familles_joueur1:
            winner_name = "à toi"
        else:
            winner_name = "Égalité"
        # Afficher l'image de victoire avec le nom du gagnant
        victory_image = pygame.image.load("Images/ecran_win.png").convert_alpha()
        screen.blit(victory_image, (0, 0))
        text = font.render(f"Bien joué {winner_name}, tu as gagné !", True, BLACK)
        screen.blit(text, ((SCREEN_WIDTH - text.get_width()) / 2, (SCREEN_HEIGHT - text.get_height()) / 2))
        pygame.display.flip()
        pygame.time.wait(5000)  # Attendre quelques secondes avant de quitter
        running = False  # Sortir de la boucle principale pour terminer le jeu

pygame.quit()







