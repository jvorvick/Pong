



# from settings import *

# class Ball(pygame.sprite.Sprite):
#     def __init__(self, groups):
#         super().__init__(groups)
#         self.image = pygame.Surface(SIZE['ball'])
#         self.image.fill(COLORS['ball'])
#         self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
#         self.direction = pygame.Vector2(1,-1)
#         self.speed = SPEED['ball']

#     def move(self, dt):
#         self.rect.center += self.direction * self.speed * dt
#         if self.rect.top <= 0: 
#             self.direction.reflect_ip(pygame.Vector2(0,-1))
#         if self.rect.bottom >= WINDOW_HEIGHT: 
#             self.direction.reflect_ip(pygame.Vector2(0,1))
#         if self.rect.left <= 0: 
#             self.direction.reflect_ip(pygame.Vector2(1,0))
#         if self.rect.right >= WINDOW_WIDTH: 
#             self.direction.reflect_ip(pygame.Vector2(-1,0))
#         self.direction = self.direction.normalize()

#     def update(self, dt):
#         self.move(dt)