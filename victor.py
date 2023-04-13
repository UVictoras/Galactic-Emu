# Init
print("Hello Today I'm Gonna Teach You")
import pygame
import math
import pygame.time
from projectile import Projectile
pygame.init()
clock = pygame.time.Clock()

# Create Window
displayHeight = 1080
displayWidth = 1920
backgroundColor = (200,200,200)
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Endless Scroll")


# Import Player1
player1x = 0
player1y = 0
player1yVelocity = 0
player1xVelocity = 0
player1size = 100
playersSpeed = 10
img_player1 = pygame.image.load("img/emeu.jpg").convert()
img_player1 = pygame.transform.scale(img_player1, (100, 100))

#
bg = pygame.image.load("img/back.png").convert()
bg = pygame.transform.scale(bg, (1920, 1080))
bg_width = bg.get_width()

#
missile = pygame.image.load("img/missile.png")
missile = pygame.transform.scale(missile, (100, 100))
missile_width = missile.get_width()

scroll = 0 
tiles = math.ceil(displayWidth / bg_width) + 1

#Bullets & CD
bullets = []
start_time = 0

# Main Loop
running = True
while running:
    # run the game at a constant 60fps
    clock.tick(60)
    #Did the user clicked the close button ?
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running=False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                running=False
    
    #draw scrolling background 
    for i in range(0, tiles):
      screen.blit(bg,(i * bg_width + scroll, 0))

    #scroll background
    scroll -= 5

    #reset scroll
    if abs (scroll) > bg_width:
        scroll = 0


    pressed = pygame.key.get_pressed()
    #PLAYER 1 Y
    if pressed[pygame.K_z]:
        player1yVelocity = -playersSpeed
    elif pressed[pygame.K_s]:
        player1yVelocity = playersSpeed
    else :
        player1yVelocity = 0
    # PLAYER 1 X
    if pressed[pygame.K_d]:
        player1xVelocity = playersSpeed
    elif pressed[pygame.K_q]:
        player1xVelocity = -playersSpeed
    else :
        player1xVelocity = 0

    #Apply player 1 movement
    player1x = player1x + player1xVelocity
    player1y = player1y + player1yVelocity

    # BOUNDING BOX
    # Player 1
    if player1x > displayWidth - player1size:
        player1x = displayWidth - player1size
    elif player1x < 0 :
        player1x = 0
    if player1y > displayHeight - player1size:
        player1y = displayHeight - player1size
    elif player1y < 0 :
        player1y = 0

    #Projectiles
    for bullet in bullets:
        bullet.y -= bullet.velocity
    
    if pressed[pygame.K_p]:
        if pygame.time.get_ticks() - start_time >= 500:
            bullets.append(Projectile(player1x, player1y, missile_width, missile))
            start_time = pygame.time.get_ticks()
        
    #Draw 
    #P1
    screen.blit(img_player1,(player1x, player1y))
    for bullet in bullets:
        if bullet.y > 0 & bullet.y < 1920:
            screen.blit(bullet.image, (bullet.x, bullet.y))
        else:
            bullets.pop(bullets.index(bullet))

    pygame.display.update()
pygame.quit()