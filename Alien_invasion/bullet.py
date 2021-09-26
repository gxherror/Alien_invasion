import  pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,sys_settings,screen,ship):
        super(Bullet, self).__init__()#父类继承
        self.screen=screen
        self.rect=pygame.Rect(0,0,sys_settings.bullet_width,sys_settings.bullet_height)##自创rect
        self.rect.centerx=ship.rect.centerx##移动正确位置
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=sys_settings.bullet_color
        self.speed=sys_settings.bullet_speed

    def update(self):
        self.y-=self.speed
        self.rect.y=self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)