import pygame

class Effect(pygame.sprite.Sprite):
    def __init__(self, surf, x, y, time):
        super(Effect, self).__init__()

        self.x = x
        self.y = y
        self.time = time

        self.surf = surf
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.time -= 1
        if self.time == 0:
            self.kill()