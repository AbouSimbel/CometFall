import pygame
pygame.init()
from game import Game
import math

#definir une clock
clock = pygame.time.Clock()
FPS = 120

# generer la fenetre du jeu - 1 on defini le titre de la fenetre "Comet fall game", 2-on defini la taille de l'ecran
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

#importer notre banniere
banner = pygame.image.load('assets/banner.png')
#redimensionner l'image de banniere car elle est trop grande
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2 - banner.get_width() / 2)

#importer notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
#redimensionner l'image de button car elle est trop grande
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = banner.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2 - play_button.get_width() / 2)
play_button_rect.y = math.ceil(screen.get_height() / 2 + 100)

#importer et charger l'arriere plan du jeu
background = pygame.image.load("assets/bg.jpg")

# charger notre jeu
game = Game()

# creation de la variable qui va nous permettre de maintenir la fenetre ouvert tant qu'elle est True
running = True

# boucle qui va etre effectuee tant que le jeu est en train de tourner
while running:

    # appliquer le background a la fenetre du jeu
    screen.blit(background, (0, -200))

    #verifier si notre jeu a commence ou non
    if game.is_playing:
        # declancher les insctrucion de la partie
        game.update(screen)
    #verifier si notre jeu n'a pas commencé
    else:
        #ajouter l'ecran d'accueil
        screen.blit(banner, banner_rect)
        #ajouter l'image
        screen.blit(play_button, play_button_rect)

    #mettre a jour la fenetre
    pygame.display.flip()

    # on verifie si le joueur ferme la fenetre
    # on peut recuperer la liste des evenements que le joueur emet (click, etc) grace au composant event du module pygame
    for event in pygame.event.get():
        # pour chaque evenement, on verifie si l'evenement est "fermeture de fenetre". Si oui, on stop la boucle while et on ferme le jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
        #detecter les events touches du clavier
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True

           #detecter si la touche espace est activée
           if event.key == pygame.K_SPACE:
               if game.is_playing:
                game.player.launch_projectile()
               else:
                   # lancer le jeu
                   game.start()
                   # jouer le son de start-game
                   game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification  pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #lancer le jeu
                game.start()
                #jouer le son de start-game
                game.sound_manager.play('click')

    # fixer le nombre de fps sur la clock
    clock.tick(FPS)



