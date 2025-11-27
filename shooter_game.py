# ? Создай собственный Шутер!

from pygame import *
from random import randint

display.set_caption("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
window = display.set_mode((700,500))
background = transform.scale(image.load("backround_leoooo.png"), (700,500))#leo_backround.jpg

lost = 0

#?music
mixer.init()
mixer.music.load("Masayoshi-Minoshima-Bad-Apple-_Instrumental_.ogg")
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")

#!главный спрайт 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, size_x, size_y, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image , (self.rect.x , self.rect.y))

#TODO игрок
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed



    def fire(self):
        bullet = Bullet("bullet.png",  15 ,20 ,self.rect.centerx ,self.rect.top , -15)
        bullets.add(bullet)



class Boost(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 600)
            self.rect.y = 0
            



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 600)
            self.rect.y = 0
            lost = lost + 1



class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


bullets = sprite.Group()

#?спрайты          
monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy("Duck.jpg", 50, 80, randint(80, 600),0 , randint(1,3))
    monsters.add(monster)

boosts = sprite.Group()

for i in range(1,2):
    boost = Boost("star_shy.png", 50, 80, randint(80,600),0 , randint(7,10))
    boosts.add(boost)




player = Player("Shiho_ggg.png" , 100, 100, 100, 370, 15)

finish = False
run = True

font.init()
font2 = font.SysFont("Arial", 36)
score = 0

font3 = font.SysFont("Arial", 80)
win = font3.render("YOU WIN", True, (255, 255, 255))
lose = font3.render("DUCKS WIN", True, (255, 255, 255))


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                fire_sound.play()
                

    if not finish:
        window.blit(background, (0,0))

        text = font2.render("Счёт:" + str(score), 1, (255,255,255))
        window.blit(text, (10,20))
        text2 = font2.render("Пропущено:" + str(lost), 1, (255,255,255))
        window.blit(text2, (10,50))


        player.update()
        monsters.update()
        boosts.update()
            
            
        monsters.draw(window)
        boosts.draw(window)
        
            
        player.reset()
        bullets.update()
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)

        collides1 = sprite.groupcollide(boosts, bullets,True, True)
        
        for c in collides:
            score += 1
            monster = Enemy("Duck.jpg", 50, 80, randint(80, 600), 0, randint(1,5))
            monsters.add(monster)

        #if sprite.spritecollide(player, boosts, True, True):
            #lost = lost - 1

        for i in collides1:
            lost -= 1
            boost = Boost("star_shy.png", 50, 80, randint(80,600),0 , randint(7,12))
            boosts.add(boost)

            #!проигрыш sprite.spritecollide(player, monster, False) or
        if  lost >= 3:
            finish = True
            window.blit(lose, (200, 200)) 

            #*выйгрыш
        if score >= 56:
            finish = True
            window.blit(win, (200,200))    
        display.update()
    else:
        finish = False
        lost = 0
        score = 0
        for b in bullets:
            b.kill()

        for m in monsters:
            m.kill()

        for o in boosts:
            o.kill()

        time.delay(3000)

        for i in range(1,6):
            monster = Enemy("Duck.jpg", 50, 80, randint(80, 600),0 , randint(1,3))
            monsters.add(monster)




        
    time.delay(50)







