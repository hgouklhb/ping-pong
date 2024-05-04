#Создай собственный Шутер!

from pygame import *

win_width = 700
win_height = 500
display.set_caption("PIN_PONG")
window = display.set_mode((win_width, win_height))
back = (234,23,45)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y, player_speed, width, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


racket1 = Player('raketka.jpg', 30, 200, 4, 50, 80)
racket2 = Player('raketka.jpg', 620, 200, 4, 50, 80)
ball = GameSprite('ball.jpeg', 200, 200, 4, 50, 30)


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()


        display.update()
    time.delay(50)


