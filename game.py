import math
import random

import pygame
from pygame import mixer


pygame.init()


screen = pygame.display.set_mode((1000,650))


background = pygame.image.load('Sprites/back.jpg')




pygame.display.set_caption("SKOOL")
icon = pygame.image.load('Sprites/character.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('Sprites/character.png')
playerX = 200
playerY = 200
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True
while running:

    
    screen.fill((0, 0, 0))
    
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            if event.key == pygame.K_DOWN:
                playerY_change = 1.5
            if event.key == pygame.K_UP:
                playerY_change = -1.5    
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0    


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 736:
        playerY = 736    

  
    player(playerX, playerY)
    
    pygame.display.update()
