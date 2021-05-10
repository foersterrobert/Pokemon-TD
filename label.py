import pygame.font
from settings import *

class Label():
    def __init__(self, screen, x, y, msg=None):
        self.x, self.y = x, y
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg = msg

        self.font = pygame.font.SysFont(None, 40)

    def draw(self, nmsg=None):
        if nmsg:
            self.msg_image = self.font.render(nmsg, True, BLACK, None)
            self.screen.blit(self.msg_image, (self.x, self.y))

        else:
            self.msg_image = self.font.render(self.msg, True, BLACK, None)
            self.screen.blit(self.msg_image, (self.x, self.y))

