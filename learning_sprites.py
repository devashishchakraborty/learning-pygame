import pygame
import sys
import random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/2, self.image.get_height()/2))
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("shooting.wav")
        
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/2, self.image.get_height()/2))

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class GameState():
    def __init__(self):
        self.state = "intro"
    
    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'
        
        pygame.display.flip()

        # Drawing
        screen.blit(background, (0,0))
        screen.blit(ready_text, (screen_width/2-115, screen_height/2-33))
        crosshair_group.draw(screen)
        crosshair_group.update()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()

        pygame.display.flip()

        screen.blit(background, (0,0))
        target_group.draw(screen)

        crosshair_group.draw(screen)
        crosshair_group.update()
    
    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()


# General Setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

# Game Screen
screen_height = 108*6
screen_width = 192*6
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("BG.png")
background = pygame.transform.scale(background, (screen_width, screen_height))
ready_text = pygame.image.load("PNG/HUD/text_ready.png")

# Crosshair
crosshair = Crosshair("crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for _ in range(20):
    new_target = Target("target_red3.png", random.randrange(0,screen_width), random.randrange(0,screen_height))
    target_group.add(new_target)

while True:
    game_state.state_manager()
    clock.tick(60)
