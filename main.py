import pygame
from universal import *
from pygame.locals import (RLEACCEL, K_ESCAPE, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d, K_SPACE, K_RSHIFT)
import effects

pygame.init()

def main():
    
    gameLoop = True
    sprites = pygame.sprite.Group()

    enemySpawnRate = 100
    enemySpawnTime = 0

    sprites.add(player1)
    sprites.add(player2)
    sprites.add(mainCore)

    while gameLoop:

        effectGroup = pygame.sprite.Group()

        keys = pygame.key.get_pressed()

        enemySpawnTime += 1
        if enemySpawnTime == enemySpawnRate:
            enemySpawnTime = 0
            makeEnemy()

        player1.update((keys[K_w], keys[K_s], keys[K_a], keys[K_d]))
        player2.update((keys[K_UP], keys[K_DOWN], keys[K_LEFT], keys[K_RIGHT]))

        if keys[K_SPACE]:
            lineEffect = effects.Effect(pygame.surface.Surface((screenWidth, screenHeight)), 0, 0, 2)
            lineEffect.surf = pygame.surface.Surface((screenWidth, screenHeight))
            lineEffect.surf.set_colorkey((0, 0, 0))
            pygame.draw.line(lineEffect.surf, (255, 128, 255), (player1.rect.centerx, player1.rect.centery), (player2.rect.centerx, player2.rect.centery))
            player1.attack(player2, enemies)
            effectGroup.add(lineEffect)

        for effect in effectGroup:
            effect.update()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        for enemy in enemies:
            enemy.update(mainCore)

        mainCore.detectCollision(enemies)

        updateScreen(sprites, enemies, effectGroup)



        clock.tick(30)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

 # I'm back
main()

pygame.quit()