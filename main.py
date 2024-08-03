import pygame
from pygame.locals import *
pygame.init()


largeur = 1000
hauteur = 700
menu = "Images/menu_1.png"
taille_image = (1000,700)
titre_fenetre = "Les 7 Tribus de Phryge"

def creation_fenetre(largeur,hauteur):
    """ création d'une fenêtre de taille largeur x hauteur"""
    global fenetre
    #création d'une fenêtre de taille largeur x hauteur
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption(titre_fenetre)
    menu_background = pygame.image.load(menu).convert()
    #Affiche le fond "menu"
    menu_redi = pygame.transform.scale(menu_background, taille_image)
    fenetre.blit(menu_redi, (0,0))
    pygame.display.flip()

def musique():
    #Inistialisation de la musique
    pygame.mixer.music.load('Music/music.mp3')
    #Volume de la musique
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)



creation_fenetre(largeur,hauteur)
musique()

#Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
        elif event.type == KEYDOWN and event.key == K_ESCAPE :
                running = False # Quitter la boucle principale si l'utilisateur appuie sur échap
        if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Vérifier le clic de souris
            # Récupérer les coordonnées du clic
            x, y = event.pos
            x2, y2 = event.pos
            # Vérifier si le clic est dans la zone du texte "Exit"

            if (412 <= x <= 588) and (576 <= y <= 634):
                running = False  # Quitter la boucle principale si l'utilisateur a cliqué sur "Exit"
            if (412<= x <= 588) and (477 <= y <= 539):
                running = False  # Quitter la boucle principale si l'utilisateur a cliqué sur "Play"
                import histoire #Importation du jeu si le joueur appuie sur "play"'''

pygame.quit()