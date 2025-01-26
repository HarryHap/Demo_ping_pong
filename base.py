from pygame import *
from spriteClass import GameSprite, Player
'''' variables '''
bkg_color = (200, 255, 255)
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))

clock = time.Clock()

''' objects '''
ball = GameSprite(player_image='./img/ball.png',
                   player_x=250, player_y=250, 
                   width=50, heigth=50, speed=2)

rocket_left = Player(player_image='./img/rocket.jpg',
                   player_x=10, player_y=220, 
                   width=20, heigth=100, speed=4)

rocket_right = Player(player_image='./img/rocket.jpg',
                   player_x=570, player_y=220, 
                   width=20, heigth=100, speed=4)

''' game loop '''

speed_x = 3
speed_y = 3

running = False
while not running:
    window.fill(bkg_color)
    ball.reset(window)
    rocket_left.reset(window)
    rocket_left.update_p_left()

    rocket_right.reset(window)
    rocket_right.update_p_right()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y > win_height - 50 or ball.rect.y < 0:
        speed_y *= -1
    
    if sprite.collide_rect(ball, rocket_right) or sprite.collide_rect(ball, rocket_left):
        speed_x *= -1

    for e in event.get():
        if e.type == QUIT:
            running = True

    display.update()
    clock.tick(60)
