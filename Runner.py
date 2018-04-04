import pygame
import sys
import players


background = 'stage.jpg'  # the file path of the background image||except it understands if in same folder
win_size = (1500,480)  # window size
pygame.init()
screen = pygame.display.set_mode(win_size, 0, 32)
pygame.display.set_caption("Freet Strighter")


screen.blit(pygame.image.load(background), (0, 0))  # loading background

# create players
player_group = pygame.sprite.Group()
player_one = players.Players(100, 100, 5,'ryu')  # ryu
player_two = players.Players(500, 100, 5, 'ken')  # ken
player_group.add(player_one, player_two)

running = True
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
    player_group.update()
    pygame.display.update()
pygame.quit()
sys.exit()