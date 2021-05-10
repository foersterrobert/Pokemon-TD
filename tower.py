import pygame
from settings import *

class Tower:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.image = pygame.image.load("./images/towers/taubsi.png")
        self.image = pygame.transform.scale(self.image, (GAP, GAP))

        self.bulletIMG = None

        self.rect = self.image.get_rect()
        self.rect.x = self.x * GAP
        self.rect.y = self.y * GAP
        self.bullets = []
        

    def draw(self, money):
        self.screen.blit(self.image, self.rect)

        for l in range(self.maxLevel):
            if l + 1 <= self.level:
                pygame.draw.circle(self.screen, GOLD, (self.rect.x + l*15 + 8, self.rect.y + 10), 6)

            elif l == self.level and money >= self.upgradeCost[l - 1]:
                pygame.draw.circle(self.screen, GREEN, (self.rect.x + l*15 + 8, self.rect.y + 10), 6)

            else:
                pygame.draw.circle(self.screen, GREY, (self.rect.x + l*15 + 8, self.rect.y + 10), 6)

    def upgrade(self):
        self.level += 1

        if self.level == 2:
            self.image = pygame.image.load("./images/towers/tauboga.png")
            self.image = pygame.transform.scale(self.image, (GAP, GAP))
            self.damage = 10
            self.range = 190
            self.ammo = 3
            self.bsize = 5
            self.speed = 25
            self.price += self.upgradeCost[self.level - 2]

        elif self.level == 3:
            self.image = pygame.image.load("./images/towers/tauboss.png")
            self.image = pygame.transform.scale(self.image, (GAP, GAP))
            self.damage = 15
            self.range = 200
            self.ammo = 5
            self.bsize = 8
            self.speed = 30
            self.price += self.upgradeCost[self.level - 2]

class Taubsi(Tower):
    def __init__(self, screen, x, y):
        Tower.__init__(self, screen, x, y)
        self.image = pygame.image.load("./images/towers/taubsi.png")
        self.image = pygame.transform.scale(self.image, (GAP, GAP)) 
        
        self.bsize = 10
        self.level = 1
        self.maxLevel = 3
        self.price = 80
        self.upgradeCost = [120, 160]
        self.damage = 15
        self.range = 150
        self.ammo = 1
        self.speed = 20

    def draw(self, money):
        self.screen.blit(self.image, self.rect)

        for l in range(self.maxLevel):
            if l + 1 <= self.level:
                pygame.draw.circle(self.screen, GOLD, (self.rect.x + l*15 + 8, self.rect.y + 10), 6)

            elif l == self.level and money >= self.upgradeCost[l - 1]:
                pygame.draw.circle(self.screen, GREEN, (self.rect.x + l*15 + 8, self.rect.y + 10), 6)

            else:
                pygame.draw.circle(self.screen, GREY, (self.rect.x + l*15 + 8, self.rect.y + 10), 6)

    def upgrade(self):
        self.level += 1

        if self.level == 2:
            self.image = pygame.image.load("./images/towers/tauboga.png")
            self.image = pygame.transform.scale(self.image, (GAP, GAP))
            self.damage = 10
            self.range = 190
            self.ammo = 3
            self.bsize = 5
            self.speed = 25
            self.price += self.upgradeCost[self.level - 2]

        elif self.level == 3:
            self.image = pygame.image.load("./images/towers/tauboss.png")
            self.image = pygame.transform.scale(self.image, (GAP, GAP))
            self.damage = 15
            self.range = 200
            self.ammo = 5
            self.bsize = 8
            self.speed = 30
            self.price += self.upgradeCost[self.level - 2]


class Glumanda(Tower):
    def __init__(self, screen, x, y):
        Tower.__init__(self, screen, x, y)

        self.image = pygame.image.load("./images/towers/charmander.png")
        self.image = pygame.transform.scale(self.image, (GAP, GAP)) 
        self.rect = self.image.get_rect()
        self.rect.x = self.x * GAP
        self.rect.y = self.y * GAP

        self.bsize = 12
        self.bulletIMG = 'Fire'
        self.level = 1
        self.maxLevel = 3
        self.price = 140
        self.upgradeCost = [170, 340]
        self.speed = 35
        self.damage = 15
        self.range = 320
        self.ammo = 1

    def draw(self, money):
        self.screen.blit(self.image, self.rect)
        for l in range(self.maxLevel):
            if l + 1 <= self.level:
                pygame.draw.circle(self.screen, GOLD, (self.rect.x + l*15, self.rect.y + 10), 6)

            elif l == self.level and money >= self.upgradeCost[l - 1]:
                pygame.draw.circle(self.screen, GREEN, (self.rect.x + l*15, self.rect.y + 10), 6)

            else:
                pygame.draw.circle(self.screen, GREY, (self.rect.x + l*15, self.rect.y + 10), 6)

    def upgrade(self):
        self.level += 1

        if self.level == 2:
            self.image = pygame.image.load("./images/towers/charmeleon.png")
            self.image = pygame.transform.scale(self.image, (GAP, GAP))
            self.damage = 25
            self.speed = 60
            self.price += self.upgradeCost[self.level - 2]

        elif self.level == 3:
            self.image = pygame.image.load("./images/towers/charizard.png")
            self.image = pygame.transform.scale(self.image, (GAP, GAP))
            self.damage = 25
            self.speed = 60
            self.price += self.upgradeCost[self.level - 2]



class Dratini(Tower):
    def __init__(self, screen, x, y):
        Tower.__init__(self, screen, x, y)

        self.image = pygame.image.load("./images/towers/dratini.png")
        self.image = pygame.transform.scale(self.image, (GAP, GAP)) 

        self.bulletIMG = 'Lazer'
        self.bsize = 20
        self.level = 1
        self.maxLevel = 3
        self.speed = 15
        self.price = 190
        self.upgradeCost = [230, 300]
        self.damage = 50
        self.range = 135
        self.ammo = 1

    def draw(self, money):
        self.screen.blit(self.image, self.rect)

        for l in range(self.maxLevel):
            if l + 1 <= self.level:
                pygame.draw.circle(self.screen, GOLD, (self.rect.x + l*15, self.rect.y + 10), 6)

            elif l == self.level and money >= self.upgradeCost[l - 1]:
                pygame.draw.circle(self.screen, GREEN, (self.rect.x + l*15, self.rect.y + 10), 6)

            else:
                pygame.draw.circle(self.screen, GREY, (self.rect.x + l*15, self.rect.y + 10), 6)

    def upgrade(self):
        self.level += 1

        if self.level == 2:
            self.image = pygame.image.load("./images/towers/dragonir.png")
            self.image = pygame.transform.scale(self.image, (GAP, GAP))
            self.damage = 200
            self.range = 140
            self.bsize = 40
            self.speed = 18
            self.price += self.upgradeCost[self.level - 2]

        elif self.level == 3:
            self.image = pygame.image.load("./images/towers/dragoran.png")
            self.image = pygame.transform.scale(self.image, (GAP, GAP))
            self.damage = 200
            self.range = 140
            self.bsize = 40
            self.speed = 18
            self.price += self.upgradeCost[self.level - 2]
