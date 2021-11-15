import pygame

#definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    #definir les choses a mettre a la creation de l'entite
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 #pour commencer l'animation a zero
        self.images = animation.get(sprite_name)
        self.animation = False

    #definir une methode pour demarrer l'aniation
    def start_animaton(self):
        self.animation = True

    #definir une methode pour animer le sprite
    def animate(self, loop=False):

        if self.animation:
            #passer a l'image suivante
            self.current_image += 1

            #verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                #remettre l'animation a zero
                self.current_image = 0

                #verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    #desactivation de l'animation
                    self.animation = False

            #modifier l'image de l'animation precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


#definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite
    images = []
    #recuprer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque fichier chaque image
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append( pygame.image.load(image_path))

    #renvoyer la liste d'images
    return images


#definir un dictionnaire contenant les images chargees de chaque sprite.
animation = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}