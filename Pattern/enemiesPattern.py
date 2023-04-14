from Class.enemy import Enemy

def firstPattern(Enemy):
    
    while Enemy.x > 0:
        Enemy.x -= Enemy.speed
    while Enemy.x < 1920:
        Enemy.x += Enemy.speed
    return Enemy.x
