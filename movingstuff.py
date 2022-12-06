import pygame, sys


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Create the display surface
screen = pygame.display.set_mode((800,800))
second_surface = pygame.Surface((100,200))

duck = pygame.image.load("PNG/Objects/duck_white.png")
duck_rect = duck.get_rect(topleft=[100,200])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255,255,255))
    screen.blit(second_surface,(100,100))
    screen.blit(duck, duck_rect)
    duck_rect.right += 1
    

    pygame.display.flip()
    clock.tick(60)