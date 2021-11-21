#Создай собственный Шутер!
from pygame import *
from random import randint

finish=False



font.init()
font = font.Font(None, 36)

win=font.render('YOU WIN!', True, (255, 215, 0))
p=0
u=0
bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width, player_height))
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.width= player_width
        self.height=player_height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def gol(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 750:
            self.rect.y +=self.speed
    def gor(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 750:
            self.rect.y +=self.speed

ball = GameSprite("Daco_4417029.png", 500, 700, 10, 100, 100)       
Rocket1 = Player("Tower_Dire_model.png", 10, 10, 10, 125, 300)
Rocket2 = Player("Tower_Radiant_model.png", 1400, 10, 10, 125, 300)
#создай окно игры
window = display.set_mode((1500, 900))
display.set_caption("ping")
background = transform.scale(
    image.load("Minimap_7.29.png"),
    (1500, 900)
)
speed_x = 10
speed_y = 10

o1=0
o2=0



events = event.get()
#задай фон сцены
clock= time.Clock()
FPS=300
clock.tick(FPS)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    if finish != True:
        window.blit(background, (0, 0))
        
        Rocket1.reset()
        Rocket1.gol()
        Rocket2.reset()
        Rocket2.gor()
        ball.reset()
        score1=font.render('Очки:' + str(o1), 1, (255, 215, 0))
        score2=font.render('Очки:' + str(o2), 1, (255, 215, 0))
        window.blit(score1, (1400, 50))
        window.blit(score2, (0, 50))
        display.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(Rocket1, ball) or sprite.collide_rect(Rocket2, ball):
        speed_x*=-1
    if ball.rect.y<0 or ball.rect.y>800:
        speed_y*=-1
    if ball.rect.x<0:
        o1+=1
        ball.kill()
        ball = GameSprite("Daco_4417029.png", 500, 700, 10, 100, 100) 
    elif ball.rect.x>1500:
        o2+=1
        ball.kill()
        ball = GameSprite("Daco_4417029.png", 500, 700, 10, 100, 100) 
    
