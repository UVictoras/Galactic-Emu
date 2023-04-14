import sys
import pygame
sys.path.append("/Mini-studio/Class")
from Class.enemy import Enemy

def firstPattern(Enemy):
    
    if Enemy.x <= 0:
        Enemy.facing = "right"
    elif Enemy.x >= 1920 - Enemy.size:
        Enemy.facing = "left"
        Enemy.patternStep = 1

    if Enemy.x == 0 and Enemy.facing == "right":
        Enemy.x += 1
        Enemy.y += 1
    elif Enemy.patternStep%6 == 0 and Enemy.facing == "right" and Enemy.patternStep < (1920 - Enemy.size)//2:
        Enemy.x += 1
    elif Enemy.facing == "right" and Enemy.patternStep < (1920 - Enemy.size)//2:
        Enemy.x += 1
        Enemy.y += 1
    
    if Enemy.patternStep >= (1920 - Enemy.size)//2 and Enemy.facing == "right" and Enemy.patternStep%6 == 0:
        Enemy.x += 1
    elif Enemy.facing == "right" and Enemy.patternStep >= (1920 - Enemy.size)//2:
        Enemy.x += 1
        Enemy.y -= 1

    if Enemy.patternStep == (1920 - Enemy.size) and Enemy.facing == "left":
        Enemy.x -= 1
        Enemy.y += 1
    elif Enemy.patternStep%6 == 0 and Enemy.facing == "left" and Enemy.patternStep < (1920 - Enemy.size)//2:
        Enemy.x -= 1
    elif Enemy.facing == "left" and Enemy.patternStep < (1920 - Enemy.size)//2:
        Enemy.x -= 1
        Enemy.y += 1
    
    if Enemy.patternStep >= (1920 - Enemy.size)//2 and Enemy.facing == "left" and Enemy.patternStep%6 == 0:
        Enemy.x -= 1
    elif Enemy.facing == "right" and Enemy.patternStep >= (1920 - Enemy.size)//2:
        Enemy.x -= 1
        Enemy.y -=1

    Enemy.patternStep += 1
