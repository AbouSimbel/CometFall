import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son de comete qui touche le sol
        self.comet_event.game.sound_manager.play("meteorite")
        #verifier si le no;bre de cometes est de 0
        if len(self.comet_event.all_comets) == 0:
            #remettre la barre a 0
            self.comet_event.reset_percent()
            #faire apparaitre deux nouveaux monstres
            self.comet_event.game.start()


    def fall(self):
        self.rect.y += self.velocity

        #detecter si la comete arrive en bas de l'ecran (sol)
        if self.rect.y >= 500:
            # on supprime la comete
            self.remove()

        #si il n'y a plus de boules de feu
        if len(self.comet_event.all_comets) == 0:
            #remettre la jauge au depart
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False

        #verifier si la comete entre en colission avec le player
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            #on damage le player
            self.comet_event.game.player.damage(10)
            # on supprime la comete
            self.remove()



