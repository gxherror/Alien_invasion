class Settings:
    def __init__(self):
        self.screen_width=1280
        self.screen_height=720
        self.bg_color=(230,230,230)
        self.ship_speed=1
        self.bullet_speed = 1.5
        self.bullet_speed_up_scale= 1.5
        self.bullet_height=15
        self.bullet_width=3
        self.bullet_color=(60,60,60)
        self.bullets_max =10
        self.alien_speed_x_up_scale=0.2
        self.alien_speed_y_up_scale =0.1
        self.alien_point_mul_scale =1.2
        self.ship_limit=3

    def initialize_sys_settings(self):
        self.bullet_speed = 2
        self.alien_speed_x = 0.5
        self.alien_speed_y = 0.2
        self.alien_point=50


    def increase_level(self):
        self.alien_speed_x+=self.alien_speed_x_up_scale
        self.alien_speed_y+=self.alien_speed_y_up_scale
        self.bullet_speed+=self.bullet_speed_up_scale
        self.alien_point*=self.alien_point_mul_scale