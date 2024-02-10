import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super(Player, self).__init__()

        self.x = x
        self.y = y

        self.speed = 10

        self.surf = pygame.surface.Surface((50, 50))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, keys):
        self.move(keys)

    
    def move(self, keys):
        if keys[0]:
            self.y -= self.speed
        if keys[1]: 
            self.y += self.speed            
        if keys[2]:
            self.x -= self.speed 
        if keys[3]:
            self.x += self.speed 

        self.rect.x = self.x
        self.rect.y = self.y

    def attack(self, otherPlayer, enemies):
        for enemy in enemies:
            if enemy.rect.clipline(self.rect.centerx ,otherPlayer.rect.centerx, self.rect.centery, otherPlayer.rect.centery):
                enemy.takeDamage()