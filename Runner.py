import pygame
import sys
import players
import player_group
import name_sprites
import thread_moving_sprites
import thread_animations


background = 'stage.jpg'  # the file path of the background image||except it understands if in same folder
win_size = (1500,480)  # window size
pygame.init()
screen = pygame.display.set_mode(win_size, 0, 32)
pygame.display.set_caption("Freet Strighter")
color_red = (217,47,10)
color_white = (255,255,255)
colliding = False
ryu_hitbox_cord = (0,0)
ken_hitbox_cord = (0,0)
has_perried = False


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
                if not colliding:
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
                if not colliding:
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
    frame_hurtbox_Ryu = {
        'punch2':      (8,79,71,28),
        'kick2':       (8,127,63,75),
        'uppunch2':    (43,10,50,91),
        'upkick3':     (6,28,84,110),
        'downpunch2':  (32,150,63,28),
        'downkick2':   (5,211,82,44),
        'jumppunch1':  (53, 132, 53, 55),
        'jumpkick1':   (34, 171, 81, 52),
    }
    frame_hurtbox_ken = {
        'punch2':      (122,81,67,31),
        'kick2':       (131,122,67,77),
        'uppunch2':    (116,4,50,92),
        'upkick3':     (121,37,68,103),
        'downpunch2':  (109,139,63,29),
        'downkick2':   (117,213,82,44),
        'jumppunch1':  (77,158,55,54),
        'jumpkick1':   (82,215,61,42),
    }
    #SPRITES.COLLIDE_MASK() R-hitsprite and k-player
    colliding = False if pygame.sprite.collide_mask(player_one,player_two) is None else True
    #make a collide variable in plar set it here
    player_two.is_colliding = colliding
    player_one.is_colliding = colliding
    if player_one.image_name in frame_hurtbox_Ryu and frame_hurtbox_Ryu[player_one.image_name] is not None:
        ryu_hitbox = pygame.Surface((frame_hurtbox_Ryu[player_one.image_name][2],frame_hurtbox_Ryu[player_one.image_name][3]))
        ryu_hitbox_cord = (frame_hurtbox_Ryu[player_one.image_name][0] + player_one.rect.x, frame_hurtbox_Ryu[player_one.image_name][1] + player_one.rect.y)
    else:
        ryu_hitbox = None
        ryu_hitbox_cord = None
    if player_two.image_name in frame_hurtbox_ken and frame_hurtbox_ken[player_two.image_name] is not None:
        ken_hitbox = pygame.Surface((frame_hurtbox_ken[player_two.image_name][2],frame_hurtbox_ken[player_two.image_name][3]))
        ken_hitbox_cord = (frame_hurtbox_ken[player_two.image_name][0] + player_two.rect.x, frame_hurtbox_ken[player_two.image_name][1] + player_two.rect.y)
    else:
        ken_hitbox = None
        ken_hitbox_cord = None
    #check actual collisions of hitbox masks
    if ken_hitbox is not None:
        ken_mask = pygame.mask.from_surface(ken_hitbox)
        ken_mask.fill()
    else:
        ken_mask = None
    if ryu_hitbox is not None:
        ryu_mask = pygame.mask.from_surface(ryu_hitbox)
        ryu_mask.fill()
    else:
        ryu_mask = None
    #parry
    if (ken_mask is not None) and (ryu_mask is not None) and (ken_mask.overlap(ryu_mask,(ryu_hitbox_cord[0]-ken_hitbox_cord[0],ryu_hitbox_cord[1]-ken_hitbox_cord[1])) is not None):
        # a parry has happened
        # do hurt animation for both
        # no damage
        has_perried = True
        print('get fuggin perryied')
    else:
        has_perried = False
    #check for contact to sprite
    ken_urt_box = pygame.mask.from_surface(player_two.image)
    ryu_urt_box = pygame.mask.from_surface(player_one.image)
    if not has_perried and ken_mask is not None and not player_one.image_name == 'hit1':
        if ken_mask.overlap(ryu_urt_box, (player_one.rect.x - ken_hitbox_cord[0], player_one.rect.y - ken_hitbox_cord[1])) is not None:
            print('ken lands a hit')
            player_two.cur_health -= .5
            print(percur2)
            percur1 = player_one.cur_health * 100 / player_one.max_health
            percur2 = player_two.cur_health * 100 / player_two.max_health

    if not has_perried and ryu_mask is not None and not player_two.image_name == 'hit1':
        if ryu_mask.overlap(ken_urt_box, (player_two.rect.x - ryu_hitbox_cord[0], player_two.rect.y - ryu_hitbox_cord[1])) is not None:
            print('ryu lands a hit')
            player_one.cur_health -= .5
            print(percur1)
            percur1 = player_one.cur_health * 100 / player_one.max_health
            percur2 = player_two.cur_health * 100 / player_two.max_health

    #End MASK SECTION


    for pressed in keys:
        if keys[pressed]:
            player_group.move(pressed)
    screen.blit(pygame.image.load(background), (0, 0))
    player_group.draw(screen)
    name_group.draw(screen)
    if ken_hitbox_cord is not None:
        mask_size = ken_mask.get_size()
        pygame.draw.rect(screen, color_red, (ken_hitbox_cord[0], ken_hitbox_cord[1], mask_size[0], mask_size[1]))

    if ryu_hitbox_cord is not None:
        mask_size = ryu_mask.get_size()
        pygame.draw.rect(screen, color_red, (ryu_hitbox_cord[0], ryu_hitbox_cord[1], mask_size[0], mask_size[1]))

    for player in player_group.sprites():
        pygame.draw.rect(screen, color_white, (23, 23, 503, 28), 2)
        pygame.draw.rect(screen, color_white, (973, 23, 503, 28), 2)

        pygame.draw.rect(screen, color_red,(25,25,percur1 * 5,25))
        pygame.draw.rect(screen,color_red,(975,25,percur2 * 5,25))



    pygame.display.update()
pygame.quit()
sys.exit()