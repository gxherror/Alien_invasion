import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    pygame.init()
    sys_settings=Settings()
    screen=pygame.display.set_mode((sys_settings.screen_width,sys_settings.screen_height))  #对象screen是个surface
    stats=GameStats(sys_settings)
    ship = Ship(sys_settings,screen)
    bullets=Group()
    aliens=Group()
    sb=Scoreboard(sys_settings,screen,stats)
    play_button=Button(sys_settings,screen,"Play")
    gf.create_fleet(sys_settings,screen,ship,aliens)
    pygame.display.set_caption("Alien Invasion")
    while 1:
        gf.check_events(sys_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        gf.update_screen(sys_settings, screen, stats, sb,ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_aliens(sys_settings,stats,sb,screen,ship,aliens,bullets)
            gf.update_bullets(sys_settings,screen,stats,sb,ship,aliens,bullets)

run_game()




