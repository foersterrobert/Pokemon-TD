import pygame
import pygame.font
from settings import *

class TaubsiIMG:
    def __init__(self, screen, price, x, y):
        self.name = 'Taubsi'
        self.screen = screen
        self.price = price
        self.font = pygame.font.SysFont(None, 24)
        self.image = pygame.image.load("./images/towers/taubsi.png")
        self.image = pygame.transform.scale(self.image, (150, 150)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, towerChoose):
        if towerChoose == self.name:
            pygame.draw.rect(self.screen, GOLD, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))
        
        else:
            pygame.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))
        
        self.screen.blit(self.image, self.rect)
        self.msg_image = self.font.render(f'{self.name}: {self.price}$', True, BLACK, None)
        self.screen.blit(self.msg_image, (self.rect.x + 5, self.rect.y + 155))

class GlumandaIMG:
    def __init__(self, screen, price, x, y):
        self.name = 'Glumanda'
        self.screen = screen
        self.price = price
        self.font = pygame.font.SysFont(None, 24)
        self.image = pygame.image.load("./images/towers/charmander.png")
        self.image = pygame.transform.scale(self.image, (150, 150)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, towerChoose):
        if towerChoose == self.name:
            pygame.draw.rect(self.screen, GOLD, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))
        
        else:
            pygame.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))
        
        self.screen.blit(self.image, self.rect)
        self.msg_image = self.font.render(f'{self.name}: {self.price}$', True, BLACK, None)
        self.screen.blit(self.msg_image, (self.rect.x + 5, self.rect.y + 155))


class DratiniIMG:
    def __init__(self, screen, price, x, y):
        self.name = 'Dratini'
        self.screen = screen
        self.price = price
        self.font = pygame.font.SysFont(None, 24)
        self.image = pygame.image.load("./images/towers/dratini.png")
        self.image = pygame.transform.scale(self.image, (150, 150)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, towerChoose):
        if towerChoose == self.name:
            pygame.draw.rect(self.screen, GOLD, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))
        
        else:
            pygame.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))
        
        self.screen.blit(self.image, self.rect)
        self.msg_image = self.font.render(f'{self.name}: {self.price}$', True, BLACK, None)
        self.screen.blit(self.msg_image, (self.rect.x + 5, self.rect.y + 155))