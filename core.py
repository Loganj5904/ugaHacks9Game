import pygame


class Core(pygame.sprite.Sprite):
    def __init__(self, x, y, hp):
        super(Core, self).__init__()

        self.surf = pygame.surface.Surface((100, 100))
        pygame.draw.circle(self.surf, (255, 255, 255), (int(self.surf.get_width() / 2), int(self.surf.get_height() / 2)), int(self.surf.get_width() / 2))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.hp = hp

        self.dead = False

    def detectCollision(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect) and not enemy.dead:
                selfMask = pygame.mask.from_surface(self.surf)
                enemyMask = pygame.mask.from_surface(enemy.surf)
                if (selfMask.overlap_area(enemyMask, (enemy.rect.x - self.rect.x, enemy.rect.y - self.rect.y)) != 0):
                    enemy.takeDamage()
                    self.takeDamage()



    def takeDamage(self):
        self.hp -= 1
        if self.hp <= 0:
            self.dead = True
            self.kill()