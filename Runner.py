import pygame
import sys
import players
import player_group
import name_sprites


background = 'stage.jpg'  # the file path of the background image||except it understands if in same folder
win_size = (1500,480)  # window size
pygame.init()
screen = pygame.display.set_mode(win_size, 0, 32)
pygame.display.set_caption("Freet Strighter")
color_red = (217,47,10)
color_white = (255,255,255)



screen.blit(pygame.image.load(background), (0, 0))  # loading background

# create players
player_group = player_group.Player_Group()
player_one = players.Players(700, 200, 10,'ryu',1)  # ryu player one
player_two = players.Players(400, 200, 10, 'ken',2)  # ken player two
player_group.add(player_one, player_two)

percur1 = player_one.cur_health * 100/player_one.max_health
percur2 = player_two.cur_health * 100/player_two.max_health

ken_ui = pygame.image.load('ui/KenName.png')
ryu_ui = pygame.image.load('ui/RyuName.png')
name_group = pygame.sprite.Group()
ken_ui = name_sprites.Name_Sprites(550,10 ,'KenName')
ryu_ui = name_sprites.Name_Sprites(860,10,'RyuName')

name_group.add(ken_ui,ryu_ui)

#create hitsprites



running = True
keys = {'w':False,'a':False,'s':False,'d':False,'space':False,'i':False,'o':False,'p':False,'left':False,'right':False,'up':False,'down':False,'4':False,'5':False,'6':False,'0':False}
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        elif evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_a:
                keys['a'] = True
                player_two.jump_dir = 'left'
            elif evt.key == pygame.K_s:
                keys['s'] = True
            elif evt.key == pygame.K_d:
                keys['d'] = True
                player_two.jump_dir = 'right'
            elif evt.key == pygame.K_w:
                keys['w'] = True
            elif evt.key == pygame.K_i:
                player_group.move('i')
            elif evt.key == pygame.K_o:
                player_group.move('o')
            elif evt.key == pygame.K_p:
                player_group.move('p')
            elif evt.key == pygame.K_LEFT:
                keys['left'] = True
                player_one.jump_dir = 'left'
            elif evt.key == pygame.K_RIGHT:
                keys['right'] = True
                player_one.jump_dir = 'right'
            elif evt.key == pygame.K_UP:
                keys['up'] = True
            elif evt.key == pygame.K_DOWN:
                keys['down'] = True
            elif evt.key == pygame.K_KP4:
                player_group.move('4')
            elif evt.key == pygame.K_KP5:
                player_group.move('5')
            elif evt.key == pygame.K_KP6:
                player_group.move('6')
            elif evt.key == pygame.K_SPACE:
                keys['space'] = True
            elif evt.key == pygame.K_KP0:
                keys['0'] = True
        elif evt.type == pygame.KEYUP:
            if evt.key == pygame.K_a:
                keys['a'] = False
                player_two.jump_dir = 'None'
            elif evt.key == pygame.K_s:
                keys['s'] = False
                player_group.move('undown')
            elif evt.key == pygame.K_d:
                keys['d'] = False
                player_two.jump_dir = 'None'
            elif evt.key == pygame.K_w:
                keys['w'] = False
                player_two.up_atck = False
            elif evt.key == pygame.K_LEFT:
                keys['left'] = False
                player_one.jump_dir = 'None'
            elif evt.key == pygame.K_RIGHT:
                keys['right'] = False
                player_one.jump_dir = 'None'
            elif evt.key == pygame.K_UP:
                keys['up'] = False
                player_one.up_atck = False
            elif evt.key == pygame.K_DOWN:
                keys['down'] = False
                player_group.move('undown')
            elif evt.key == pygame.K_SPACE:
                keys['space'] = False
            elif evt.key == pygame.K_KP0:
                keys['0'] = False

    #Start MASK SECTION

    #make/update hitbox sprites

    #CHECK If my hitbox collides with yours

    # find out what frame im hitting in
    plr_one_frame = player_one.image_name
    plr_two_frame = player_two.image_name
    # move and resize the sprite to fit the frame
    # buncha fuggin ifs - or a loop with one set of ifs

    # make a mask from hitsprite and opponent sprite

    # mask collision with appropriate offsets

    # deduct health

    #End MASK SECTION
    for pressed in keys:
        if keys[pressed]:
            player_group.move(pressed)
    screen.blit(pygame.image.load(background), (0, 0))
    player_group.draw(screen)
    name_group.draw(screen)



    for player in player_group.sprites():
        pygame.draw.rect(screen, color_white, (23, 23, 503, 28), 2)
        pygame.draw.rect(screen, color_white, (973, 23, 503, 28), 2)

        pygame.draw.rect(screen, color_red,(25,25,percur1 * 5,25))
        pygame.draw.rect(screen,color_red,(975,25,percur2 * 5,25))



    pygame.display.update()
pygame.quit()
sys.exit()