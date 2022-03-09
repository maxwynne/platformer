import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
# correcting font / font type, font size
test_font = pygame.font.Font('Pixeltype.ttf', 50)
sky_surface = pygame.image.load('sky.png').convert()
ground_surface = pygame.image.load('ground.png').convert()
# text info / anti-alias / colour

score_surf = test_font.render('my game', False, (64,64,64))
# centre score text by using rectangles
score_rect = score_surf.get_rect(center=(400,50))

# set alpha values, respect white and black
snail_surf = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600,300))

player_surf = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # check mouse position
        # check if mouse is over player rectangle
        # if event.type == pygame.MOUSEMOTION:
            # if player_rect.collidepoint(event.pos): print('collision')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')

        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    # draw rectangle
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    # pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
    # pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),10)
    screen.blit(score_surf,score_rect)

    snail_rect.x -= 4
    # move back to right of screen
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)

    # player
    player_gravity += 1
    
    screen.blit(player_surf,player_rect)

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
        #print('jump')

    #if player_rect.colliderect(snail_rect):
        #print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
