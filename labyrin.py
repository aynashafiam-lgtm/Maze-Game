from pygame import *

win_lebar = 700
win_tinggi = 500
display.set_caption("Maze Game")
window = display.set_mode((win_lebar, win_tinggi))
back = (255, 255, 255)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        if packman.rect. <- win_width-80 and packman.×_speed > 0 or packman.rect. ›- 0 and packman.*_speed < 0:
            self.rect.x +* self.x_speed
        platforms_touched - sprite.spritecollide(self, barriers, False) 
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right - min(self.rect.right, p.rect.left) 
        elif self.x_ speed < 0:
            for p in platforms_touched:
                self.rect. left - max(self.rect.left, p.rect.right)
        if packman.rect-y <- win_height-80 and packman-y_speed › 0 or packman.rect.y >= 0 and packman-y_speed < 0:
            self.rect.y += self.y_speed
        platforms _touched - sprite.spritecollide(self, barriers, False)
        if self.y_speed › 0:
            for p in platforms_touched:
                self.rect.bottom - min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top - max(self.rect.top, p.rect.bottom) 

w1 - GameSprite('platform2.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('platform2_v.png', 370, 100, 50, 400)
packman - Player('hero-png', 5, win_height - 80, 80, 80, 0, 0)
barriers = sprite.Group() 
monsters = sprite.Group() 
barriers.add(w1) 
barriers.add(w2) 
monster1 = Enemy('black-cat.png', win_width - 80, 150, 80, 780, 5) 
monster2 = Enemy ('black-cat.png', win_width - 80, 230, 80, 80, 5) 
final_sprite = GameSprite('pac-1.png', win_width-85, win_height-100, 80, 80) #tambat
monsters.add (monster1) 
monsters.add (monster2)

finish = False
run = True

while run:
    time.delay(60)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.typr == KEYUP:
            if e.key == K_LEFT:
                packman. x speed = 0
                packman. x speed = 0
            elif e.key == K RIGHT:
                packman.x_speed = 0
            elif e.key == K UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
        if not finish:
            windoow.fill(back)
            barriers.draw(window)
            final_sprite.reset()
            packman.reset()
            packman.update()
            monsters.draw(window)
        if sprite.spritecollide (packman, monsters, False):
            finish = True
            img = image.load('game-over_1.png')
            d = img-get_width() // img.get_height()
            window.fill((255, 255, 255)) 
            window.blit(transform.scale(img, (win_height*d, win_height)), (90, 0))
        if sprite.collide_rect (packman, final_sprite):
            finish = True
            img = image. load('thumb.jpg')
            window. fill((255, 255, 255))
            window.blit(transform.scale(img, (win _width, win height)), (0, 0)) 
            display.update()