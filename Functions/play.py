import pygame, sys
import math
import pygame.time
import random

from Class.projectile import Projectile
from Class.player import Player
from Class.enemy import Enemy
from Class.score import Score
from Class.button import Button

def play(missileA, classicBulletA, projectileListA, playerA):
    #Init the pygame & clock
    pygame.init()
    clock = pygame.time.Clock()

    # Create Window
    displayHeight = 1080
    displayWidth = 1920
    backgroundColor = (200,200,200)
    screen = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption("Bullet Hell")

    #Import background model
    backGround = pygame.image.load("img/back.png").convert()
    backGround = pygame.transform.scale(backGround, (100, 100))
    backGroundHeight = backGround.get_height()
    backgroundWidth = backGround.get_width()

    #Pre-requisite for the screen scrolling
    trueScroll = 0 
    tilesHeight = math.ceil(displayHeight / backGroundHeight) + 1
    tilesWidth = math.ceil(displayWidth / backgroundWidth) + 1

    #Import missile model
    missile = missileA
    missileWidth = missile.get_width()

    #Import bullets 
    classicBullet = classicBulletA

    #Import special shoot
    bigBall = pygame.image.load("img/grosse_boule.png")
    bigBall = pygame.transform.scale(bigBall, (50, 50))

    #Import ultimate
    ultimateShoot = pygame.image.load("img/grosse_boule.png")
    ultimateShoot = pygame.transform.scale(ultimateShoot, (100, 100))
    ultimateShootWidth = ultimateShoot.get_width()

    ultimateSound = pygame.mixer.Sound("sound/seismic_charge.mp3")
    ultimateSound.set_volume(0.2)

    #Import Music
    bulletHellSound = pygame.mixer.Sound("sound/Bullet_Hell.mp3")
    bulletHellSound.set_volume(0.2)

    #projectileList & CD
    projectileList = projectileListA
    missileCooldown = 0
    bulletCoolDown = 0
    ultimateCooldown = 0
    scoreTime = 0

    particleList = []
    shaking = False
    screenShake = 40

    #Create Player
    imgPlayer = pygame.image.load("img/player.png")
    imgPlayer = pygame.transform.scale(imgPlayer, (50, 50))

    player = playerA


    #Create Enemy
    imgRailgun = pygame.image.load("img/railgun.png")
    imgRailgun = pygame.transform.scale(imgRailgun, (50, 50))
    imgEnemy = pygame.image.load("img/bozo.png")
    imgEnemy = pygame.transform.scale(imgEnemy, (50, 50))

    enemyDelayList = [[0, 0, 50], [0, 0, 100], [0, 0, 50], [0, 0, 100], [0, 0, 100]]
    enemy1 = Enemy(True, 50, 2, 300, 0, 50, displayWidth, displayHeight, 100, imgRailgun, bigBall, 4, 10, 5, projectileList, 1, "left")
    enemy2 = Enemy(True,50, 2, 1200, 0, 50, displayWidth, displayHeight, 100, imgEnemy, bigBall, 10, 3, 10, projectileList, 1, "left")
    enemy3 = Enemy(True,50, 2, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy, bigBall, 10, 3, 10, projectileList, 1, "left")
    enemy4 = Enemy(True, 50, 1, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy, classicBullet, 4, 4, 30, projectileList, 1, "left", 0, 10, 1, 0, 2, bigBall)
    enemy5 = Enemy(False, 50, 0.5, 500, 0, 50, displayWidth, displayHeight, 100, imgEnemy, classicBullet, 1, 4, 90, projectileList, 0.5, "left", 3, 1, 1, 0, 3, bigBall)

    enemyList = [enemy1, enemy2, enemy3, enemy4]
    onScreenEnemiesList = []

    #Create Button
    buttonSurface = pygame.image.load("img/button.png")
    buttonSurface = pygame.transform.scale(buttonSurface, (200, 75))

    button = Button(buttonSurface, 500, 500, "Change weapon price : 30", True, 30, Button.ChangeWeapon, imgEnemy)
    button2 = Button(buttonSurface, 900, 700, "Do nothing", False, 0, Button.ChangeWeapon, None)

    buttonList = [button, button2]

    #Initiate dash coordinates
    timerDash = [0 , 0]

    #Initiate score
    score = Score()

    #Import a font
    font = pygame.font.Font(None, 36)

    #Define rotate function for bullet hitboxes
    def rotate(image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        new_image = pygame.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect
    pygame.init()
    running = True
    
    while running:
        # run the game at a constant 60fps
        clock.tick(60)

        #Close window on Escape press
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running=False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    running=False
            if events.type == pygame.MOUSEBUTTONDOWN:
                for button in buttonList:
                    button.checkForInput(pygame.mouse.get_pos(), player)
            for button in buttonList:
                button.changeColor(pygame.mouse.get_pos())
        
        #Play msic in loop
        if bulletHellSound.get_num_channels() == 0:
            bulletHellSound.play()
        
        #screen shake
        if shaking:
            trueScroll += random.randint(0, screenShake) - screenShake/2

        for i in range(0, tilesHeight):
            for j in range(0, tilesWidth):
                screen.blit(backGround, (j*backGround.get_width(), i*backGround.get_height() - trueScroll))
        
        trueScroll += 1
        # reset scroll
        if trueScroll >= backGround.get_height():
            trueScroll = 0

        # Slow movement and dash
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LSHIFT]:
            player.speed = player.slowSpeed
        elif pressed[pygame.K_SPACE] and timerDash[1] == 0:
            timerDash[1] = player.cooldownDash
            timerDash[0] = player.timeDash
            player.speed = player.dashSpeed
        elif timerDash[0] == 0: 
            player.speed = player.basicSpeed

        if timerDash[0] > 0:
            timerDash[0] -= 1
        elif timerDash[0] == 0 and timerDash[1] > 0:
            timerDash[1] -= 1

        #PLAYER Y movement
        if pressed[pygame.K_UP]:
            velY = -1
        elif pressed[pygame.K_DOWN]:
            velY = 1
        else :
            velY = 0

        # PLAYER X movement
        if pressed[pygame.K_RIGHT]:
            velX = 1
        elif pressed[pygame.K_LEFT]:
            velX = -1
        else :
            velX = 0
            
        player.move(velX, velY)
        playerHitbox = pygame.Rect(0,0, player.size/8, player.size/8)
        # center the hitbox on the ship's cockpit
        playerRect = pygame.Rect(player.X+player.size/2 - playerHitbox.width/2, player.Y+player.size/2, playerHitbox.width, playerHitbox.height)

        #Add enemies at the right time
        if enemyDelayList != [] and enemyDelayList[0][2] <= 0 and enemyList != []:
            onScreenEnemiesList.append(enemyList.pop(0))
            enemyDelayList.pop(0)

        for bullet in projectileList:
            if bullet.update(onScreenEnemiesList) == True:
                projectileList.pop(projectileList.index(bullet))
            #rotated_image = pygame.transform.rotate(bullet.image, bullet.angle)
            bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.image.get_width(), bullet.image.get_height())
            rotated_image, bulletRect = rotate(bullet.image, bulletRect, bullet.angle)
            screen.blit(rotated_image, (bullet.x, bullet.y))
            if bullet.isPlayer == False:
                #pygame.draw.rect(screen, (255,0,0), bulletRect)
                if playerRect.colliderect(bulletRect):
                    player.getHit()
                    projectileList.pop(projectileList.index(bullet))
        
        #Enemy
        for enemy in onScreenEnemiesList:
            enemy.update(player)
            rect = pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)
            
            screen.blit(enemy.image, (enemy.x, enemy.y))
            if enemy.y > enemy.displayHeight:
                enemy.health = 0
                onScreenEnemiesList.pop(onScreenEnemiesList.index(enemy))

            #Collision bullet & enemy
            for bullet in projectileList:
                if bullet.isPlayer == True:
                    bulletRect = pygame.Rect(bullet.x, bullet.y, bullet.size, bullet.size)
                    if rect.colliderect(bulletRect):
                        enemy.takeDmg(bullet.damage, onScreenEnemiesList)
                        score.score_increment(10)
                        projectileList.pop(projectileList.index(bullet))

                    if(enemy.health <= 0):
                        player.money += 10
                        score.score_increment(enemy.score)
                        break
            if rect.colliderect(playerRect):
                player.getHit()
                score.score_increment(10)
                onScreenEnemiesList.pop(onScreenEnemiesList.index(enemy))
                
        for particle in particleList:
            if(particle.draw(screen, projectileList)):
                particleList.pop(particleList.index(particle))
                shaking = False
            else:
                shaking = True
            
            if(particle.doDamage):
                for enemy in onScreenEnemiesList:
                    enemy.takeDmg(player.ultimateDmg, onScreenEnemiesList)

        #Add a bullet to the projectileList list on press
        if pressed[pygame.K_w]:
            if player.cooldown <= 0:
                player.shoot()
                player.cooldown = player.timeBetweenShots
        if pressed[pygame.K_x]:
            if player.missileCooldown <= 0:
                player.shootHoming()
                player.missileCooldown = player.timeBetweenMissiles
        if pressed[pygame.K_c]:
            if player.ultimateCooldown <= 0:
                #play sfx
                ultimateSound.play()
                player.shootUltimate(particleList)
                player.ultimateCooldown = player.timeBetweenUltimates
        
        player.cooldown -= 1
        player.missileCooldown -= 1
        player.ultimateCooldown -= 1

        if enemyDelayList != []:
            enemyDelayList[0][2] -= 1

        #Score grows automatically
        if pygame.time.get_ticks() - scoreTime >= 3000:
            score.score_increment(30)
            scoreTime = pygame.time.get_ticks()
            
        #Draw player model on screen
        screen.blit(imgPlayer, (player.X, player.Y))
        
        #Write player's score & remaining lives
        scoreText = font.render(f'Score: {score.score}', True, (255, 255, 255))
        screen.blit(scoreText, (10, 10))
        livesText = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
        screen.blit(livesText, (10, 30))
        ultimateText = font.render(f'Ultimate in: {math.ceil(player.ultimateCooldown/60)}', True, (255, 255, 255))
        screen.blit(ultimateText, (10, 50))
        moneyText = font.render(f'Money: {player.money}', True, (255, 255, 255))
        screen.blit(moneyText, (10, 70))

        for button in buttonList:
            screen.blit(button.image, button.rect)
            screen.blit(button.text, button.text_rect)
        
        pygame.display.update()
    bulletHellSound.stop()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()