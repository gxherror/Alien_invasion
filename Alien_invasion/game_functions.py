import pygame
import  sys
from alien import Alien
from  bullet import  Bullet
from time import sleep

def check_events(sys_settings,screen,stats,sb,play_button,ship,aliens,bullets):
     for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            check_keydown_event(event,sys_settings,screen,stats,sb,ship,aliens,bullets)

        if event.type==pygame.KEYUP:
            check_keyup_event(event, ship)

        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(sys_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

        if event.type==pygame.QUIT:
            sys.exit()

def start_game(sys_settings,screen,stats,sb,ship,aliens,bullets):##存在bug
    print('START')
    sys_settings.initialize_sys_settings()
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True
    sb.prep_level()
    sb.prep_ships()
    sb.prep_score()
    aliens.empty()
    bullets.empty()
    create_fleet(sys_settings, screen, ship, aliens)
    ship.center_ship()

def check_play_button(sys_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        start_game(sys_settings, screen, stats,sb, ship, aliens, bullets)


def check_keydown_event(event,sys_settings,screen,stats,sb,ship,aliens,bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    if event.key == pygame.K_UP:
        ship.move_up = True
    if event.key == pygame.K_DOWN:
        ship.move_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(sys_settings, screen, ship, bullets)
    if event.key==pygame.K_ESCAPE:
        sys.exit()
    if event.key== pygame.K_RETURN and stats.game_active==False:
        start_game(sys_settings, screen, stats,sb, ship, aliens, bullets)


def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False
    if event.key == pygame.K_UP:
        ship.move_up = False
    if event.key == pygame.K_DOWN:
        ship.move_down = False

def update_screen(sys_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(sys_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def create_alien(sys_settings,screen,aliens,alien_number,row_number):
    alien = Alien(sys_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    alien.y =alien.rect.height+2*alien.rect.height*row_number
    alien.rect.y = alien.y
    aliens.add(alien)

def get_number_aliens_x(sys_settings,alien_width):
    available_space_x = sys_settings.screen_width - (2 * alien_width)
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def create_fleet(sys_settings,screen,ship,aliens,stats):
    alien=Alien(sys_settings,screen)
    number_aliens_x=get_number_aliens_x(sys_settings,alien.rect.width)
    number_rows=get_number_rows(sys_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(sys_settings,screen,aliens,alien_number,row_number)

def get_number_rows(sys_settings,ship_height,alien_height):
    available_number_y=(sys_settings.screen_height-ship_height-3*alien_height)
    number_rows=int(available_number_y/(2*alien_height))
    return number_rows

def update_bullets(sys_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():##漏了会导致遗漏分数
            stats.score+=sys_settings.alien_point*len(aliens)
            sb.prep_score()
            check_high_score(stats,sb)
    if len(aliens)==0:
        bullets.empty()
        create_fleet(sys_settings,screen,ship,aliens)
        sys_settings.increase_level()
        stats.level+=1
        sb.prep_level()

def fire_bullet(sys_settings, screen, ship,bullets):
    if len(bullets) < sys_settings.bullets_max:
        new_bullet = Bullet(sys_settings, screen, ship)
        bullets.add(new_bullet)

def  update_aliens(sys_settings,stats,sb,screen,ship,aliens,bullets):
    check_fleet_edges(sys_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        print("GAME OVER!")
        ship_hit(sys_settings,stats,sb,screen,ship,aliens,bullets)


def ship_hit(sys_settings,stats,sb,screen,ship,aliens,bullets):
    stats.ship_left-=1
    sb.prep_ships()
    aliens.empty()
    bullets.empty()
    create_fleet(sys_settings, screen, ship, aliens)
    ship.center_ship()
    sleep(3)
    if stats.ship_left==0:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_fleet_edges(sys_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges_x():
            sys_settings.alien_speed_x=sys_settings.alien_speed_x*(-1)
            break
        if alien.check_edges_y():
            sys_settings.alien_speed_y = sys_settings.alien_speed_y * (-1)
            break

def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()

