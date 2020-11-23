import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000,650))

# Background
background = pygame.image.load('Sprites/back.jpg')

# Sound

# Caption and Icon
pygame.display.set_caption("SKOOL")
icon = pygame.image.load('Sprites/character.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Sprites/character.png')
playerX = 200
playerY = 200
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            if event.key == pygame.K_DOWN:
                playerY_change = 1.5
            if event.key == pygame.K_UP:
                playerY_change = -1.5    
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0    

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

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
    # show_score(textX, testY)
    pygame.display.update()
