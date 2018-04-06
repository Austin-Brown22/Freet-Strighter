import pygame
import sys
import players
import player_group


background = 'stage.jpg'  # the file path of the background image||except it understands if in same folder
win_size = (1500,480)  # window size
pygame.init()
screen = pygame.display.set_mode(win_size, 0, 32)
pygame.display.set_caption("Freet Strighter")


screen.blit(pygame.image.load(background), (0, 0))  # loading background

# create players
player_group = player_group.Player_Group()
player_one = players.Players(100, 100, 5,'ryu')  # ryu
player_two = players.Players(500, 100, 5, 'ken')  # ken
player_group.add(player_one, player_two)

running = True
keys = {'w':False,'a':False,'s':False,'d':False,'i':False,'o':False,'p':False,'left':False,'right':False,'up':False,'down':False,'4':False,'5':False,'6':False,}
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        elif evt.type == pygame.KEYDOWN:
            if evt.key == pygame.key.K_a:
                keys['a'] = True
            elif evt.key == pygame.key.K_s:
                keys['s'] = True
            elif evt.key == pygame.key.K_d:
                keys['d'] = True
            elif evt.key == pygame.key.K_w:
                keys['w'] = True
            elif evt.key == pygame.key.K_i:
                keys['i'] = True
            elif evt.key == pygame.key.K_o:
                keys['o'] = True
            elif evt.key == pygame.key.K_p:
                keys['p'] = True
            elif evt.key == pygame.key.K_LEFT:
                keys['left'] = True
            elif evt.key == pygame.key.K_RIGHT:
                keys['right'] = True
            elif evt.key == pygame.key.K_UP:
                keys['up'] = True
            elif evt.key == pygame.key.K_DOWN:
                keys['down'] = True
            elif evt.key == pygame.key.K_KP4:
                keys['4'] = True
            elif evt.key == pygame.key.K_KP5:
                keys['5'] = True
            elif evt.key == pygame.key.K_KP6:
                keys['6'] = True
        elif evt.type == pygame.KEYUP:
            if evt.key == pygame.key.K_a:
                keys['a'] = False
            elif evt.key == pygame.key.K_s:
                keys['s'] = False
            elif evt.key == pygame.key.K_d:
                keys['d'] = False
            elif evt.key == pygame.key.K_w:
                keys['w'] = False
            elif evt.key == pygame.key.K_i:
                keys['i'] = False
            elif evt.key == pygame.key.K_o:
                keys['o'] = False
            elif evt.key == pygame.key.K_p:
                keys['p'] = False
            elif evt.key == pygame.key.K_LEFT:
                keys['left'] = False
            elif evt.key == pygame.key.K_RIGHT:
                keys['right'] = False
            elif evt.key == pygame.key.K_UP:
                keys['up'] = False
            elif evt.key == pygame.key.K_DOWN:
                keys['down'] = False
            elif evt.key == pygame.key.K_KP4:
                keys['4'] = False
            elif evt.key == pygame.key.K_KP5:
                keys['5'] = False
            elif evt.key == pygame.key.K_KP6:
                keys['6'] = False
    for pressed in keys:
        if keys[pressed]:
            player_group.move(pressed)


    player_group.draw(screen)
    pygame.display.update()
pygame.quit()
sys.exit()