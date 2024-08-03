import pygame
import pygame.freetype
from pygame.locals import *


# POUR PASSER L'HISTOIRE ET JOUER APPUYER SUR ECHAP, UNE FOIS L'HISTOIRE TERMINEE, APPUYER SUR ECHAP

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
ecran = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Histoire")

# Données du jeu
nom_personnage = "Les Phryges"

dico_histoire = {
    "introduction": [
        "Oh, salut ! Tiens, tu sais ce que sont les Jeux Olympiques ?",
        "Laisse nous t'éclairer !",
        "Il y a très longtemps, dans un pays lointain appelé la Grèce antique,",
        "les gens adoraient leurs dieux et déesses à travers toutes sortes de",
        "célébrations. Mais les Jeux Olympiques, c'était la crème de la crème !",
        "C'était comme la plus grosse fête sportive de l'année !",
        "Imaginez-vous, les Grecs se réunissaient à Olympie, une petite ville",
        "tranquille, pour des jeux incroyables en l'honneur de Zeus, le roi",
        "des dieux. Ils voulaient montrer à Zeus qu'ils étaient en super forme",
        "et qu'ils savaient faire des trucs dingues comme courir super vite ou",
        "lancer des trucs super loin ! À l'époque, les Jeux Olympiques étaient",
        "un peu comme un mélange de compétition sportive et de festival de la",
        "bonne humeur. Tout le monde laissait de côté les disputes et les",
        "histoires de familles pour venir s'amuser ensemble.",
        "Hé, Phryge, tu te souviens de la course de stadion ?",
        "C'était la première course des Jeux, et les mecs couraient comme des",
        "dingues sur une distance qui correspondait à un stade. D'où le nom,",
        "\"stadion\" ! Ça devait être trop cool à voir !",
        "Ouais, Phryge, et tu te rappelles de Philippidès ?",
        "Ce gars-là, il était une vraie légende ! Il a couru",
        "le Marathon à Athènes, soit plus de 40 kilomètres, pour annoncer la",
        "victoire des Grecs. Imagine le cardio qu'il devait avoir !",
        "Au fil du temps, les Jeux Olympiques ont traversé des hauts et des bas",
        "mais ils ont toujours gardé cet esprit de fair-play et d'unité entre",
        "les peuples. En 1896, un super-héros appelé Pierre de Coubertin a",
        "ramené les Jeux Olympiques à la vie à Athènes, et depuis, c'est devenu",
        "le rendez-vous incontournable de tous les sportifs du monde !",
        "Et voilà comment les Jeux Olympiques sont devenus cette méga-fête",
        "sportive qu'on connaît aujourd'hui !",
        "   ",
        "   ",
        "   ",
        "Eh d'alleurs ! tu sais quoi, cette année ils ont préparés un truc de dingue !",
        "Parce que les JO c'est aussi pour rencontrer un max de gens et bah là ils",
        "ont préparés une édition spéciale du jeu des 7 familles comme ça on peut",
        "rencontrer pleins de gens ! On pourra aussi en apprendre plus sur les Jeux",
        "tout en s'amusant c'est pas trop cool !? Tiens prends ce paquet de cartes.",
        "Pas besoin de t'inquiéter les règles sont super simples ! Une carte a un",
        "rôle et une famille et ton but c'est de réunir tous les membres d'une",
        "famille. Tu demandes une carte à ton ami et s'il ne l'a pas tu pioches.",
        "C'est facile nan, ahah, pour gagner tu doit réunir le max de familles.",
        "Y'en a 7 et chacune a 6 membres. Fastoche ! Sur ce on te laisse nous",
        "on a du boulot. J'espère que tu vas t'amuser, à bientôt!",
        "   ",
        "Paris 2024 est prêt à accueillir la prochaine édition,",
        "et on a hâte de vous y voir !"
    ]
}

fond_ecran_intro = "Images/fond_grece.png"
fond_ecran_jeu_chap = "Images/fond_grece.png"

# Police par défaut de Pygame
police_ecriture = pygame.font.SysFont('comicsansms',25)
police_nom_perso = pygame.font.SysFont('mvboli', 35)

clock = pygame.time.Clock()

def story(chap):
    if chap == 1:
        menu_fond = pygame.image.load(fond_ecran_intro).convert()
    else:
        menu_fond = pygame.image.load(fond_ecran_jeu_chap).convert()
    menu_fond = pygame.transform.scale(menu_fond, (1000,700))
    ecran.blit(menu_fond, (0, 0))
    pygame.display.flip()

    longueur = 0
    text_number = 0

    continuer = True  # Variable pour contrôler la boucle principale
    while continuer:
        ecran.blit(menu_fond, (0, 0))
        clock.tick(20)
        rect_nom = police_nom_perso.render(nom_personnage, True, (231,157,112))
        ecran.blit(rect_nom, (45, 510))
        if text_number == 0:
            text_surface0 = police_ecriture.render(dico_histoire["introduction"][text_number][0:longueur], True, (250,229,184))
            ecran.blit(text_surface0, (75, 560))
            longueur += 1
        if longueur >= len(dico_histoire["introduction"][text_number]) and text_number < len(dico_histoire["introduction"]) - 1:
            text_number += 1
            longueur = 0
        if text_number >= 1:
            text_surface0 = police_ecriture.render(dico_histoire["introduction"][text_number - 1], True, (250,229,184))
            text_surface1 = police_ecriture.render(dico_histoire["introduction"][text_number][0:longueur], True, (250,229,184))
            ecran.blit(text_surface0, (75, 560))
            ecran.blit(text_surface1, (75, 595))
            longueur += 1

        pygame.display.flip()
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                continuer = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
                pygame.quit()

    # Après la fin de l'histoire
    import cartes
    pygame.quit()  # Quitter Pygame


def musique():
    #Inistialisation de la musique
    pygame.mixer.music.load('Music/music_2.mp3')
    #Volume de la musique
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1)

musique()
story(1)
