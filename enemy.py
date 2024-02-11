import pygame
import math

scoreNum = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, color):
        super(Enemy, self).__init__()

        self.x = x
        self.y = y

        self.surf = pygame.surface.Surface((30, 30))
        pygame.draw.circle(self.surf, color, (15, 15), 15)
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()

        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 3

        self.hp = 1

        self.dead = False


    def update(self, core):
        try:
            targetX = core.rect.centerx
            targetY = core.rect.centery

            angle = math.atan2((targetY - self.rect.centery), (targetX - self.rect.centerx))
            speed = self.speed

            self.moveEnemy(angle, speed)
        except:
            pass

    def moveEnemy(self, angle, speed):
        dx = math.cos(angle)
        dy = math.sin(angle)

        self.x += dx * speed
        self.y += dy * speed

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def detectCollision(enemies):
        pass

    def takeDamage(self):
        self.hp -= 1
        if self.hp <= 0:
            self.dead = True
            self.kill()