from settings import *
import pygame

class Bullet:
    def __init__(self, screen, x, y, ex, ey, bsize, imgB=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
        self.bsize = bsize
        self.imgB = imgB
        self.image = None
        if self.imgB:
            if self.imgB == 'Fire':
                self.image = pygame.image.load("./images/bullets/fire.png")

            elif self.imgB == 'Lazer':
                self.image = pygame.image.load("./images/bullets/Lazer.png")

            self.image = pygame.transform.scale(self.image, (bsize*2, bsize*2))
            self.rect = self.image.get_rect()

    def draw(self):
        if self.image:
            self.rect.centerx = self.x
            self.rect.centery = self.y
            self.screen.blit(self.image, self.rect)

        else:
            pygame.draw.circle(self.screen, (245,245,220), (self.x, self.y), self.bsize)