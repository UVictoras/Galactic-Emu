import pygame
import sys

from Class.button import Button
from Functions.jsonReader import *

buttonSurface = pygame.image.load("img/UI/button.png")
buttonSurface = pygame.transform.scale(buttonSurface, (buttonSurface.get_width()/1.3, buttonSurface.get_height()/1.3))

RESUME_BUTTON = Button(buttonSurface, 960, 850, "Return", False, None, None, buttonSurface)

# Upgrade Button Ship
if get("save.json", "secondaryWeapon1") == "autocanon":
    AUTOCANON_BUTTON = Button(buttonSurface, 800, 550, "Autocanon", True, -1, None, buttonSurface, "A high firerate suspended canon")
else:
    AUTOCANON_BUTTON = Button(buttonSurface, 800, 550, "Autocanon", True, 100, None, buttonSurface, "A high firerate suspended canon")
    
if get("save.json", "secondaryWeapon2") == "shotgun":
    SHOTGUN_BUTTON = Button(buttonSurface, 1150, 700, "Shotgun", True, -1, None, buttonSurface, "Slow firerate but wide angle")
else:
    SHOTGUN_BUTTON = Button(buttonSurface, 1150, 700, "Shotgun", True, 150, None, buttonSurface, "Slow firerate but wide angle")
    
if get("save.json", "secondaryWeapon2") == "phoenix":
    PHOENIX_BUTTON = Button(buttonSurface, 1150, 550, "Phoenix", True, -1, None, buttonSurface, "A strong and fast missile")
else:
    PHOENIX_BUTTON = Button(buttonSurface, 1150, 550, "Phoenix", True, 250, None, buttonSurface, "A strong and fast missile")
    
if get("save.json", "secondaryWeapon1") == "spiral":
    SPIRAL_BUTTON = Button(buttonSurface, 800, 700, "Spiral", True, -1, None, buttonSurface, "Shoots bullets all arround your ship")
else:
    SPIRAL_BUTTON = Button(buttonSurface, 800, 700, "Spiral", True, 50, None, buttonSurface, "Shoots bullets all arround your ship")
    
# SHOTGUN_BUTTON = Button(buttonSurface, 800, 700, "Shotgun", True, 150, None, buttonSurface, "Slow firerate but wide angle")
# PHOENIX_BUTTON = Button(buttonSurface, 1150, 550, "Phoenix", True, 250, None, buttonSurface, "A strong and fast missile")
# SPIRAL_BUTTON = Button(buttonSurface, 1150, 700, "Spiral", True, 50, None, buttonSurface, "Shoots bullets all arround your ship")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)


MENU_TEXT = get_font(100).render("POWER-UP SHOP", True, "#b68f40")
MENU_TEXT_RECT = MENU_TEXT.get_rect(center=(960, 100))
MENU_SLOT1 = get_font(20).render("Slot 1 :", True, "#b68f40")
MENU_SLOT1_RECT = MENU_SLOT1.get_rect(center=(800, 400))
MENU_SLOT2 = get_font(20).render("Slot 2 :", True, "#b68f40")
MENU_SLOT2_RECT = MENU_SLOT2.get_rect(center=(1150, 400))

def shopConsumable(SCREEN, BG, player, main_menu, gameManager, shop):
    running = True
    while running:
        MENU_MONEY = get_font(20).render("Money:" + str(player.money), True, "#b68f40")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)
        SCREEN.blit(MENU_SLOT1, MENU_SLOT1_RECT)
        SCREEN.blit(MENU_SLOT2, MENU_SLOT2_RECT)

        SCREEN.blit(MENU_MONEY, (50,50))
        
        for button in [RESUME_BUTTON, SHOTGUN_BUTTON, PHOENIX_BUTTON, SPIRAL_BUTTON, AUTOCANON_BUTTON]:
            button.changeColor(MENU_MOUSE_POS, SCREEN)
            button.update(SCREEN)
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    shop(SCREEN, BG, player, main_menu, gameManager)
                if AUTOCANON_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "secondaryWeapon1", "autocanon")
                    post("save.json", "money", player.money - AUTOCANON_BUTTON.price)
                    player.secondaryWeapon1 = "autocanon"
                    AUTOCANON_BUTTON.price = -1
                    if SPIRAL_BUTTON.price == -1:
                        SPIRAL_BUTTON.price = 50
                        SPIRAL_BUTTON.isLevelMax = False
                elif SHOTGUN_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "secondaryWeapon2", "shotgun")
                    post("save.json", "money", player.money - SHOTGUN_BUTTON.price)
                    player.secondaryWeapon2 = "shotgun"
                    SHOTGUN_BUTTON.price = -1
                    if PHOENIX_BUTTON.price == -1:
                        PHOENIX_BUTTON.price = 250
                        PHOENIX_BUTTON.isLevelMax = False
                elif PHOENIX_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "secondaryWeapon2", "phoenix")
                    post("save.json", "money", player.money - PHOENIX_BUTTON.price)
                    player.secondaryWeapon2 = "phoenix"
                    PHOENIX_BUTTON.price = -1
                    if SHOTGUN_BUTTON.price == -1:
                        SHOTGUN_BUTTON.price = 150
                        SHOTGUN_BUTTON.isLevelMax = False
                elif SPIRAL_BUTTON.checkForInput(MENU_MOUSE_POS, player):
                    post("save.json", "secondaryWeapon1", "spiral")
                    post("save.json", "money", player.money - SPIRAL_BUTTON.price)
                    player.secondaryWeapon1 = "spiral"
                    SPIRAL_BUTTON.price = -1
                    if AUTOCANON_BUTTON.price == -1:
                        AUTOCANON_BUTTON.price = 100
                        AUTOCANON_BUTTON.isLevelMax = False
        pygame.display.update()