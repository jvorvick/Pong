from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, display_surface, pos, groups):
        super().__init__(groups)
        self.rect = pygame.draw.rect(display_surface, 'red', (pos, (200, 400)))