import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# initialize the pygame library
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# setup the display window of 500 width & 500 height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# run the loop until user closes the window
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((75,75))
        # self.surf.fill((255, 255, 255))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

player = Player()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # user clicked escape to stop loop
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
    
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # fill the screen with white background color
    screen.fill((255, 255, 255))

    # surf = pygame.Surface((50, 50))
    # surf.fill((0, 0, 0))
    # rect = surf.get_rect()

    # surf_center = (
    #     ((SCREEN_WIDTH - surf.get_width()) / 2),
    #     ((SCREEN_HEIGHT - surf.get_height()) / 2)
    # )

    screen.blit(player.surf, player.rect)

    # flip the display
    pygame.display.flip()


# at last quit from pygame
pygame.quit()