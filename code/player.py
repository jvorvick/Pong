



# from settings import *

# class Player(pygame.sprite.Sprite):
#     def __init__(self, groups):
#         super().__init__(groups)
#         self.image = pygame.Surface(SIZE['paddle'])
#         self.image.fill(COLORS['paddle'])
#         self.rect = self.image.get_frect(center = POS['player'])
#         self.direction = pygame.Vector2()
#         self.speed = SPEED['player']

#     def input(self):
#         keys = pygame.key.get_pressed()
#         self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])

#     def move(self, dt):
#         if (
#             self.rect.top > 0 and self.direction.y == -1 or
#             self.rect.bottom < WINDOW_HEIGHT and self.direction.y == 1
#         ):
#             self.rect.y += self.direction.y * self.speed * dt

#     def update(self, dt):
#         self.input()
#         self.move(dt)