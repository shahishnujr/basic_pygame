import pygame
pygame.init()
screen_width = 1024
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))

player = pygame.Rect((0,0,50,50))

pygame.display.set_caption("Basic box")
run = True
while run:

    screen.fill((0,0,0))
    pygame.draw.rect(screen,(16,173,212),player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True or key[pygame.K_LEFT] == True  :
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True or key[pygame.K_RIGHT] == True :
        player.move_ip(1,0)
    elif key[pygame.K_w] == True or key[pygame.K_UP] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True or key[pygame.K_DOWN] == True:
        player.move_ip(0,1)

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()            