import pygame
from pygame.sprite import  Sprite
class Alien(Sprite):
    def __init__(self,sys_settings,screen):
        super(Alien, self).__init__()
        self.screen=screen
        self.direction_x=1
        self.direction_y=1
        self.sys_settings=sys_settings
        self.image=pygame.image.load("images/alien.bmp")
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        self.y = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edges_x(self):
        screen_rect=self.screen.get_rect()
        if self.rect.x>=screen_rect.right:
            return True
        if self.rect.x<=0:
            return True

    def check_edges_y(self):
        screen_rect=self.screen.get_rect()
        if self.rect.y>=screen_rect.bottom:
            return True
        if self.rect.y<=0:
            return True





    def update(self):
        self.x+=self.sys_settings.alien_speed_x
        self.y += self.sys_settings.alien_speed_y
        self.rect.x=self.x
        self.rect.y =self.y

