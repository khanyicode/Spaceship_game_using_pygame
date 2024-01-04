import pygame
import os

# This is to create the dimensions
WIDTH, HEIGHT = 1000, 600

# This is to set up the screen for pygame
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MINI GAME")
BLUE = (0, 0, 255)
FPS = 70
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60, 50

# Fix the paths and scale the images correctly
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Initial positions of spaceships
red_x, red_y = 100, 300
yellow_x, yellow_y = 700, 300

def drawings():
    WIN.fill(BLUE)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow_x, yellow_y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red_x, red_y))
    pygame.display.update()

# This is the main function where the whole game runs
def main():
    global red_x  # Declare red_x as a global variable

    play_game = True
    clock = pygame.time.Clock()
    
    while play_game:
        clock.tick(FPS)

        # This is for checking all the events that take place in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False

        # Move the red spaceship
        red_x += 1

        drawings()

if __name__ == "__main__":
    main() 
    