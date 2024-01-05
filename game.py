import pygame
from pygame import mixer
import os
import time

# This is to create the dimensions
WIDTH, HEIGHT = 1000, 600

# This is to set up the screen for pygame
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MINI GAME")
BLUE = (0, 0, 255)
FPS = 70
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60, 50

# Initial positions of spaceships
red_x, red_y = 100, 300
yellow_x, yellow_y = 700, 300
# Fix the paths and scale the images correctly

def define_ships(spaceship_yellow, spaceship_red):
    YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', f'{spaceship_yellow}.png'))
    YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

    RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', f'{spaceship_red}.png'))
    RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

    return YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE


def drawings(YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE):
    WIN.fill(BLUE)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow_x, yellow_y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red_x, red_y))
    pygame.display.update()


def track_position(red_x, yellow_x):

    # checking for frontal collision
    if red_x + ((SPACESHIP_WIDTH // 2) + 15) >= yellow_x:
        return True
    return False


def load_sound(sound_name):
    crash_sound = mixer.init()
    crash_sound = mixer.Sound(f'Assets/{sound_name}.mp3')
    return crash_sound


# This is the main function where the whole game runs
def main():
    global red_x  # Declare red_x as a global variable

    
    YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE = define_ships('spaceship_yellow', 'spaceship_red')

    crash_sound = load_sound('explosion')

    play_game = True
    clock = pygame.time.Clock()
    
    while play_game:
        clock.tick(FPS)

        # This is for checking all the events that take place in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False

        # Move the red spaceship
        if track_position(red_x, yellow_x):
            crash_sound.play()
            time.sleep(5)
            red_x = 100
            continue
        red_x += 1

        drawings(YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE)

if __name__ == "__main__":
    main() 
    