import pygame
from random import randint
wd = pygame.display.set_mode((700,500))
background = pygame.transform.scale(pygame.image.load('pngtree-football-green-field-both-sides-standing-background-picture-image_2425367.jpg'),(700,500))
clock = pygame.time.Clock()
fps = 60
game = True
finish = False
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, plear_x, plear_y, player_speed, wight, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = plear_x
        self.rect.y = plear_y
    def reset(self):
        wd.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 370:
            self.rect.y += self.speed
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 370:
            self.rect.y += self.speed
ball = GameSprite('ball.png', 320, 215, 8, 40, 40)
stena1 = Player('blue.wall.png', 35, 175, 6, 55, 125)
stena2 = Player('green.wall.png', 635, 175, 6, 35, 125)
ball_x = randint(-5,5)
ball_y = 8
pygame.font.init()
font1 = pygame.font.Font(None, 72)
lose_blue = font1.render('lose blue!', True, (255,0,0))
lose_green = font1.render('lose green!', True, (255,0,0))
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if finish != True:
        wd.blit(background, (0,0))
        stena1.update_l()
        stena2.update_r()
        ball.rect.x += ball_x
        ball.rect.y += ball_y
        if pygame.sprite.collide_rect(stena1, ball):
            ball_x *= -1
            ball_y *= 1
        if pygame.sprite.collide_rect(stena2, ball):
            ball_x *= -1
            ball_y *= 1
        if ball.rect.y > 460 or ball.rect.y < 5:
            ball_y *= -1 
        if ball.rect.x < -5:
            finish = True
            wd.blit(lose_blue,(240, 210))
        if ball.rect.x > 705:
            finish = True
            wd.blit(lose_green,(240, 210))
        stena1.reset()
        stena2.reset()
        ball.reset()
    pygame.display.update()
    clock.tick(fps)