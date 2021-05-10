import pygame
from settings import *

class Mauzi:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.i = 0
        self.image = pygame.image.load("./images/enemies/mauzi.png")
        self.image = pygame.transform.scale(self.image, (round(GAP*.6), round(GAP*.6)))
        self.rect = self.image.get_rect()
        
        self.max_hp = 100
        self.hp = self.max_hp
        self.speed = 5
        self.bounty = 20

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.hp < self.max_hp:
            pygame.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y - 20, round(GAP*.6), 10))
            pygame.draw.rect(self.screen, RED, (self.rect.x, self.rect.y - 20, round(GAP*.6)*(self.hp/self.max_hp), 10))


class Smogmog:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.i = 0
        self.image = pygame.image.load("./images/enemies/smogmog.png")
        self.image = pygame.transform.scale(self.image, (round(GAP*.6), round(GAP*.6)))
        self.rect = self.image.get_rect()
        self.max_hp = 350
        self.hp = self.max_hp
        self.speed = 3
        self.bounty = 30

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.hp < self.max_hp:
            pygame.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y - 20, round(GAP*.6), 10))
            pygame.draw.rect(self.screen, RED, (self.rect.x, self.rect.y - 20, round(GAP*.6)*(self.hp/self.max_hp), 10))



class Woingenau:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.i = 0
        self.image = pygame.image.load("./images/enemies/woingenau.png")
        self.image = pygame.transform.scale(self.image, (round(GAP*.6), round(GAP*.6)))
        self.rect = self.image.get_rect()
        self.max_hp = 1400
        self.hp = self.max_hp
        self.speed = 2
        self.bounty = 50
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.hp < self.max_hp:
            pygame.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y - 20, round(GAP*.6), 10))
            pygame.draw.rect(self.screen, RED, (self.rect.x, self.rect.y - 20, round(GAP*.6)*(self.hp/self.max_hp), 10))