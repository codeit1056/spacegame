import pygame
import sys
import time
pygame.init()

WIDTH, HEIGHT = 500,550
FPS = 60
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Shooters')
clock = pygame.time.Clock()
font = pygame.font.Font('assets/space_font.ttf',50)

backround_image = pygame.transform.scale(pygame.image.load('assets/backround.png'),(500,550))

player1_image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets/player_1.png'),(65,65)),180).convert_alpha()
player_1 = player1_image.get_rect(center = (250,100))

player2_image = pygame.transform.scale(pygame.image.load('assets/player_2.png'),(65,65)).convert_alpha()
player_2 = player2_image.get_rect(center = (250,450))

bullet_image = pygame.transform.rotate(pygame.image.load('assets/bullet.png'),180).convert_alpha()
bullet_image_2 = pygame.image.load('assets/bullet.png')

player1_bullets = []
player2_bullets = []

bullet_vel = 4
vel = 2.75

player1_health = 5
player2_health = 5

player1_won_message = font.render('Blue has won!',False,'White')
player1_won = player1_won_message.get_rect(center = (250,275))

player2_won_message = font.render('Green has won!',False,'White')
player2_won = player2_won_message.get_rect(center = (250,275))

draw_message = font.render('Draw!',False,'White')
draw = draw_message.get_rect(center = (250,275))

player1_health_bars = [pygame.Rect(470,25,30,25),pygame.Rect(440,25,30,25),pygame.Rect(410,25,30,25),pygame.Rect(380,25,30,25),pygame.Rect(350,25,30,25)]
player2_health_bars = [pygame.Rect(470,500,30,25),pygame.Rect(440,500,30,25),pygame.Rect(410,500,30,25),pygame.Rect(380,500,30,25),pygame.Rect(350,500,30,25)]

red_health_bar = pygame.image.load('assets/red_bar.xcf').convert()
player1_red_health_bar = red_health_bar.get_rect(topright = (500,25))
player2_red_health_bar = red_health_bar.get_rect(bottomright = (500,525))

def player_1_movement(keys):
    if keys[pygame.K_w] and player_1.y >= 0:
        player_1.y -= vel
    if keys[pygame.K_a] and player_1.x >= 0:
        player_1.x -= vel
    if keys[pygame.K_s] and player_1.bottom <= 260:
        player_1.y += vel
    if keys[pygame.K_d] and player_1.right <= 500:
        player_1.x += vel

def player_2_movement(keys):
    if keys[pygame.K_UP] and player_2.y >= 275:
        player_2.y -= vel
    if keys[pygame.K_LEFT] and player_2.x >= 0:
        player_2.x -= vel
    if keys[pygame.K_DOWN] and player_2.bottom <= 550:
        player_2.y += vel
    if keys[pygame.K_RIGHT] and player_2.right <= 500:
        player_2.x += vel

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c and len(player1_bullets) < 3:
                bullet_rect = bullet_image.get_rect(center = (player_1.centerx,player_1.centery))
                player1_bullets.append(bullet_rect)

            if event.key == pygame.K_m and len(player2_bullets) < 3:
                bullet_rect_2 = bullet_image_2.get_rect(center = (player_2.centerx,player_2.centery))
                player2_bullets.append(bullet_rect_2)


        
    window.blit(backround_image,(0,0))

    window.blit(red_health_bar,player1_red_health_bar)
    window.blit(red_health_bar,player2_red_health_bar)

    window.blit(player1_image,player_1)
    window.blit(player2_image,player_2)

    keys = pygame.key.get_pressed()
    player_1_movement(keys)
    player_2_movement(keys)

    
    for i in range(len(player1_health_bars)):
        (x,y,w,h) = player1_health_bars[i]
        pygame.draw.rect(window,'Green', pygame.Rect(x,y,w,h)) 
    for i in range(len(player2_health_bars)):
        (x,y,w,h) = player2_health_bars[i]
        pygame.draw.rect(window,'Green', pygame.Rect(x,y,w,h)) 

    for bullet in player1_bullets:
        window.blit(bullet_image,bullet)
        bullet.y += bullet_vel
        if bullet.y >= 600:
            player1_bullets.remove(bullet)
        if pygame.Rect.colliderect(bullet,player_2):
            player2_health -= 1
            player1_bullets.remove(bullet)
            player2_health_bars.remove(player2_health_bars[player2_health])

    for bullet in player2_bullets:
        window.blit(bullet_image_2,bullet)
        bullet.y -= bullet_vel
        if bullet.y <= -100:
            player2_bullets.remove(bullet)   
        if pygame.Rect.colliderect(bullet,player_1):
            player1_health -= 1
            player2_bullets.remove(bullet)
            player1_health_bars.remove(player1_health_bars[player1_health])

    
    if player2_health == 0:
        window.blit(player1_won_message,player1_won)
        pygame.display.update()
        time.sleep(3)
        after_start = pygame.time.get_ticks()
        player1_bullets.clear()
        player2_bullets.clear()
        player1_health = 5
        player2_health = 5
        player_1.centerx, player_1.centery = 250,100
        player_2.centerx, player_2.centery = 250,450
        player1_health_bars.clear()
        player2_health_bars.clear()
        player1_health_bars = [pygame.Rect(470,25,30,25),pygame.Rect(440,25,30,25),pygame.Rect(410,25,30,25),pygame.Rect(380,25,30,25),pygame.Rect(350,25,30,25)]
        player2_health_bars = [pygame.Rect(470,500,30,25),pygame.Rect(440,500,30,25),pygame.Rect(410,500,30,25),pygame.Rect(380,500,30,25),pygame.Rect(350,500,30,25)]


        #if time_passed >= 5000:
            #gameover = False

    if player1_health == 0:
        window.blit(player2_won_message,player2_won)
        pygame.display.update()
        time.sleep(3)
        player1_bullets.clear()
        player2_bullets.clear()
        player1_health = 5
        player2_health = 5
        player_1.centerx, player_1.centery = 250,100
        player_2.centerx, player_2.centery = 250,450
        player1_health_bars.clear()
        player2_health_bars.clear()
        player1_health_bars = [pygame.Rect(470,25,30,25),pygame.Rect(440,25,30,25),pygame.Rect(410,25,30,25),pygame.Rect(380,25,30,25),pygame.Rect(350,25,30,25)]
        player2_health_bars = [pygame.Rect(470,500,30,25),pygame.Rect(440,500,30,25),pygame.Rect(410,500,30,25),pygame.Rect(380,500,30,25),pygame.Rect(350,500,30,25)]


    pygame.display.update()
    clock.tick(FPS)
