import pygame
from comet import Comet

#creer une classe pour gerer cet evenement
class CometFallEvent:

    #lors du chargement on creer un compteur pour
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 33
        self.game = game
        self.fall_mode = False

        #definir un groupe de sprite pour stocker nos cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def meteor_fall(self):
        #boucle pour faire apparaitre plusieurs cometes
        for i in range(1, 10):
            self.all_comets.add(Comet(self))

    def reset_percent(self):
        self.percent = 0

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True #activer l'evenement fall

    def is_full_loaded(self):
        return self.percent >= 100

    def update_bar(self, surface):

        #ajouter du pourcentage a la barre
        self.add_percent()

        #barre noire en arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #axe des x
            surface.get_height() - 20, # axe des y
            surface.get_width(), #largeur de la barre
            10 # epaisseur de la barre
        ])
        #barre rouge de la jauge d'evenement
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height() - 20,  # axe des y
            (surface.get_width() / 100) * self.percent,  # largeur de la barre
            10  # epaisseur de la barre
        ])
