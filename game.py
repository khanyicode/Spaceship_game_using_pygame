import pygame
from pygame import mixer
import os


# This is to create the dimensions
WIDTH, HEIGHT = 1000, 600

# This is to set up the screen for pygame
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MINI GAME")
BLUE = (0, 0, 255)
FPS = 70
velocity=10
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


def handle_red_spaceship_movement(keys_pressed):
    global red_x, red_y
    if keys_pressed[pygame.K_a]:  # moving to the left
        red_x -= velocity
    if keys_pressed[pygame.K_d]:  # moving to the right
        red_x += velocity
    if keys_pressed[pygame.K_w]:  # moving up
        red_y -= velocity
    if keys_pressed[pygame.K_s]:  # moving down
        red_y += velocity


def handle_yellow_spaceship_movement(keys_pressed):
    global yellow_x, yellow_y
    if keys_pressed[pygame.K_LEFT]:  # moving to the left
        yellow_x -= velocity
    if keys_pressed[pygame.K_RIGHT]:  # moving to the right
        yellow_x += velocity
    if keys_pressed[pygame.K_UP]:  # moving up
        yellow_y -= velocity
    if keys_pressed[pygame.K_DOWN]:  # moving down
        yellow_y += velocity
    
    
# This is the main function where the whole game runs
def main():
    global red_x, yellow_x, red_y, yellow_y

    YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE = define_ships('spaceship_yellow', 'spaceship_red')

    crash_sound = load_sound('explosion')

    play_game = True
    clock = pygame.time.Clock()
    
    while play_game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
       
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_spaceship_movement(keys_pressed) 
        handle_red_spaceship_movement(keys_pressed)
        drawings(YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE)
       
if __name__ == "__main__":
    main()
    