import pygame

def firstPattern(ownX, speed):
    
    while ownX > 0:
        ownX -= speed
    while ownX < 1920:
        ownX += speed
    return ownX
