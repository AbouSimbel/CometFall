import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager

# Creaction d'une classe qui va representer notre jeu
class Game:

    def __init__(self):
        # definir si le jeu a commencé
        self.is_playing = False
        # Generer notre joueur quand une partie est creee
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generer l'event comete
        self.comet_event = CometFallEvent(self)
        #gerer le son
        self.sound_manager = SoundManager()
        #groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.font = pygame.font.Font("assets/myfont.ttf", 36)
        #creer le score et le mettre a zero
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        #remettre le jeu a neuf (1 - retirer les monstres, 2 - remettre le joueur a 100 vie et 3 - remettre en attente)
        self.all_monsters = pygame.sprite.Group() #on ecrase le groupe de monstres par un groupe vide
        self.comet_event.all_comets = pygame.sprite.Group() # on ecrase le groupe de cometes
        self.comet_event.reset_percent() # on remet aussi la jauge d'event cometes a zero
        self.player.health = self.player.max_health
        self.is_playing = False
        #on remet le score a 0
        self.score = 0
        #jouer le son game over
        self.sound_manager.play('game_over')

    def update(self, screen):
        #afficher le score sur l'ecran
        score_text = self.font.render(f"Score: {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))


        # appliquer l'image du player
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        #actualiser l'animation du joueur
        self.player.update_animation()

        # recuperer les projectiles du player
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuprer l'ensemble des cometes du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images du groupe de monstres
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images du groupe projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur veut aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -30:
            self.player.move_left()

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

