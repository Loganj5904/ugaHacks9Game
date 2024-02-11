import pygame
import player
import enemy
import core
import random

screenWidth = 800
screenHeight = 600

backGroundColor = (70, 182, 30)

screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

clock = pygame.time.Clock() 

player1 = player.Player(100, 100, (255, 0, 0))
player2 = player.Player(screenWidth - 100, screenHeight - 100, (0, 0, 255))
mainCore = core.Core(int(screenWidth / 2), int(screenHeight / 2), 5)




enemies = pygame.sprite.Group()

# what is
def blit(group):
    for sprite in group:
        screen.blit(sprite.surf, sprite.rect)


def updateScreen(*groups):
    screen.fill(backGroundColor)
    for group in groups:
        blit(group)
    pygame.display.flip()

def makeEnemy():
    print("spawn")
    xOry = random.randint(0, 1)
    nOrp = random.randint(0, 1)
    
    spawnX = 0
    spawnY = 0

    offset = 40
    
    if xOry == 0:
        spawnX = random.randint(0 - offset, screenWidth + offset)
        if nOrp == 0:
            spawnY = offset + screenHeight
        else:
            spawnY = -offset
    else:
        spawnY = random.randint(0 - offset, screenHeight + offset)
        if nOrp == 0:
            spawnX = offset + screenWidth
        else:
            spawnX = -offset

    newEnemy = enemy.Enemy(spawnX, spawnY, 3, (128, 0, 128))
    enemies.add(newEnemy)
