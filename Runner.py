import pygame
import sys
background = "path\something"#the file path of the background image
win_size = (800,800)#window size
pygame.init()
screen = pygame.display.set_mode(win_size,0,32)
pygame.display.set_caption("Freet Strighter")


screen.blit(pygame.image.load(background),(0,0))#loading background


running = True
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
sys.exit()