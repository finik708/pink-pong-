from random import randint
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, rocket_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(rocket_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y <400:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y <400:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

window=display.set_mode((700, 500))
display.set_caption("шутер")
rakcet = Player('racket.png', 0, 400, 40, 100, 10)
rakcet2 = Player('racket.png', 650, 400, 40, 100, 10)

monsters = sprite.Group()
asteroids = sprite.Group()
bullets = sprite.Group()
font.init()
font = font.SysFont('Arial', 30)
centorx = rakcet.rect.centerx
centory = rakcet.rect.top


clock = time.Clock()
mixer.init()
ubitie = mixer.Sound('fire.ogg')
mixer.music.load('space.ogg')
mixer.music.play()
FPS = 60
background=transform.scale(image.load("galaxy.jpg"), (700, 500))
lives = 3
lose = 0
probil = 0
game=True
finish = False
while game:    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            rokcet.fire()
            ubitie.play()
    if finish != True:
        
        window.blit(background, (0, 0))
        rakcet.reset()
        rakcet.update_l()
        rakcet2.reset()
        rakcet2.update_r()
        monsters.update()
        monsters.draw(window)
        asteroids.update()
        asteroids.draw(window)
        losetext = font.render('propustil:' + str(lose), True, (255, 215, 0))
        probitie = font.render('zagnulos:' + str(probil), True, (255, 215, 0))
        zhisn = font.render('zhizn:' + str(lives), True, (255, 215, 0))

        bullets.update()
        if sprite.spritecollide(rakcet, monsters, True) or sprite.spritecollide(rakcet, asteroids, True):
            lives = lives - 1
        if  lives < 1:
            finish = True

        stolp = sprite.groupcollide(asteroids, bullets, False, True)
        stolp = sprite.groupcollide(monsters, bullets, True, True)
        for i in stolp:
            enemy = Enemy('ufo.png', randint(0,650), 0, 50, 50, randint(2,5))
            monsters.add(enemy)
        bullets.draw(window)
        window.blit(losetext, (0, 0))
        window.blit(probitie, (0, 40))
        window.blit(zhisn, (0, 90))
        clock.tick(FPS)
    if finish == True:
        window.blit(background, (0, 0))
        over = font.render('game over', True, (255, 0, 0))
        window.blit(over, (200, 200))
        rokcet.kill()
        
    display.update() 