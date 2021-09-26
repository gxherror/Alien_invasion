import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,sys_settings,screen):
        super(Ship, self).__init__()
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)#rect只能够存储整式型
        self.centery = float(self.rect.centery)  # rect只能够存储整式型
        self.speed =sys_settings.ship_speed
        self.move_right=False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_right and self.centerx<self.screen_rect.right-25:
            self.centerx+=self.speed
        if self.move_left and self.centerx>self.screen_rect.left+25:
            self.centerx-=self.speed
        if self.move_up and self.centery>self.screen_rect.top+25:
            self.centery-=self.speed
        if self.move_down and self.centery<self.screen_rect.bottom-25:
            self.centery+=self.speed

        self.rect.centerx=self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom