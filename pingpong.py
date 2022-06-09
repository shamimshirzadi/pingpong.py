import pygame

pygame.init()


screen = pygame.display.set_mode((800,600))
caption= pygame.display.set_caption("pong game")
icon= pygame.display.set_icon('icon.png')
pygame.display.set_icon(icon)

#player
player=pygame.image.load('player.png')
enemy = pygame.image.load('player.png')
ball= pygame.image.load('ball.png')

running=True
while running :
    #add player
    screen.blit(player,(50,60))
    #add enemy
    screen.blit(enemy,(10,20))
    #add ball
    screen.blit(ball,(9,15))

    pygame.display.update()