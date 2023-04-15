import pygame
import math
import pygame
class Projectile():
<<<<<<< HEAD
    def __init__(self, x, y, width, image, velocity, damage, isHoming, displayWidth, displayHeight, projectileList, speed, player=False, enemyList = [], playerPos = (0,0)):
=======
    def __init__(self, x, y, width, image, velocity, damage, isHoming, displayWidth, displayHeight, projectileList, player=False, enemyList = [], playerPos = (0,0)):
>>>>>>> b1e51fd8cf0ef78ceee913807d0509652e959c2e
        self.isPlayer = player
        self.x = x
        self.y = y
        self.velocity = velocity
        self.damage = damage

        self.width = width
        self.image = image
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight

        self.isHoming = isHoming
<<<<<<< HEAD
        self.speed = speed
=======
>>>>>>> b1e51fd8cf0ef78ceee913807d0509652e959c2e
        self.enemyList = enemyList
        self.playerPos = playerPos
        self.rotationSpeed = 10

        projectileList.append(self)
        self.pos = pygame.math.Vector2(self.x, self.y)
<<<<<<< HEAD
        
        
    def update(self, enemyList):
        self.enemyList = enemyList
        if(self.isHoming):
            self.chase()
        else:
            self.x += self.velocity[0] * self.speed
            self.y += self.velocity[1] * self.speed

        '''The bullet is destroyed when exiting the screen'''
        #del(self) doesnt actually delete the instance for some reason
        if self.x < 0 - self.width:
            del(self)
            return True
        elif self.x > self.displayWidth + self.width:
            del(self)
            return True
        if self.y < 0 - self.width:
            del(self)
            return True
        elif self.y > self.displayHeight + self.width:
            del(self)
            return True

    def chase(self):
        if(self.isPlayer):
            distance = 10000
            target = pygame.Vector2(self.x, -1000)
            for enemy in self.enemyList:
                if distance > pygame.math.Vector2.distance_to(pygame.math.Vector2(enemy.x, enemy.y), pygame.math.Vector2(self.x, self.y)):
                    distance = pygame.math.Vector2.distance_to(pygame.math.Vector2(enemy.x, enemy.y), pygame.math.Vector2(self.x, self.y))
                    target = pygame.Vector2(enemy.x, enemy.y)
                    
            dx = target.x - self.x
            dy = target.y - self.y
            distance = math.sqrt((dx ** 2) + (dy ** 2))
            # Déplacer le missile vers la cible avec une vitesse constante
            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed
            # Calculer l'angle de rotation nécessaire pour pointer vers l'ennemi
            angle_radians = math.atan2(dy, dx)
            angle_degrees = math.degrees(angle_radians)
            # Faire pivoter l'image du missile de l'angle calculé
            '''Casse tout !!!'''
            rotated_image = pygame.transform.rotate(self.image, -angle_degrees - 90)

        else:
            pass

    def rotateToTarget(self, target):
        targetPos = pygame.math.Vector2(target.x, target.y)
        
=======


    def update(self):
        if(self.isHoming):
           self.chase()
        else:
            self.x = self.x + self.velocity.x
            self.y = self.y + self.velocity.y

        '''The bullet is destroyed when exiting the screen'''
        if self.x < 0 - self.width:
            del(self)
        elif self.x > self.displayWidth + self.width:
            del(self)
        if self.y < 0 - self.width:
            del(self)
        elif self.y > self.displayHeight + self.width:
            del(self)

    def chase(self):
        pos = pygame.math.Vector2(self.x, self.y)
        target = pos
        if(self.isPlayer):
            min_dist = 9999
            for e in self.enemyList:
                ePos = pygame.math.Vector2(e.x, e.y)
                self.pos.distance_to(ePos)
                print(str(distance))
                if distance < min_dist:
                    print("Found closest ennemy")
                    distance = min_dist
                    target = e
            #Le missile doit trouver l'enemi le + proche
            '''radians = math.atan2(self.y - target.y, self.x - target.x)
            destX = math.cos(radians)
            destY = math.sin(radians)
            self.x += destX
            self.y += destY'''
        else:
            #le missile doit aller vers le joueur
            pass
        pass

    def rotateToTarget(self, target):
        targetPos = pygame.math.Vector2(target.x, target.y)

>>>>>>> b1e51fd8cf0ef78ceee913807d0509652e959c2e
        direction = (targetPos - self.pos)
        angleTo = self.pos.angle_to(targetPos)
        self.pos.rotate(angleTo * min(self.rotationSpeed, abs(angleTo)))
