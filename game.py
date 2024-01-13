import pygame
from pygame import mixer
import os

# This is to create the dimensions
WIDTH, HEIGHT = 1000, 600

# This is to set up the screen for pygame
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MINI GAME")
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 70
velocity = 10
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 60, 50
BULLET_VELOCITY = 8

# Initial positions of spaceships
yellow_x, yellow_y = 700, 300
red_x, red_y = 100, 300


def define_ships(spaceship_yellow, spaceship_red):
    YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', f'{spaceship_yellow}.png'))
    YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

    RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', f'{spaceship_red}.png'))
    RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -270)

    return YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE


def drawings(YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE, yellow_bullets, red_bullets):
    WIN.fill(BLUE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow_x, yellow_y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red_x, red_y))

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255, 255, 0), bullet)  # Yellow color for bullets

    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)  # Red color for bullets

    pygame.display.update()


def track_position(red_x, yellow_x):
    if red_x + ((SPACESHIP_WIDTH // 2) + 15) >= yellow_x:
        return True
    return False


def load_sound(sound_name):
    crash_sound = mixer.init()
    crash_sound = mixer.Sound(f'Assets/{sound_name}.mp3')
    return crash_sound


def handle_red_spaceship_movement(keys_pressed):
    global red_x, red_y

    if keys_pressed[pygame.K_a] and red_x - velocity > 0:  # moving to the left
        red_x -= velocity
    if keys_pressed[pygame.K_d] and red_x + velocity < BORDER.x:  # moving to the right
        red_x += velocity
    if keys_pressed[pygame.K_w] and red_y - velocity > 0:  # moving up
        red_y -= velocity
    if keys_pressed[pygame.K_s] and red_y + velocity < HEIGHT:  # moving down
        red_y += velocity


def handle_yellow_spaceship_movement(keys_pressed):
    global yellow_x, yellow_y

    if keys_pressed[pygame.K_LEFT] and yellow_x - velocity > BORDER.x + 5:  # moving to the left
        yellow_x -= velocity
    if keys_pressed[pygame.K_RIGHT] and yellow_x + velocity < WIDTH:  # moving to the right
        yellow_x += velocity
    if keys_pressed[pygame.K_UP] and yellow_y - velocity > 0:  # moving up
        yellow_y -= velocity
    if keys_pressed[pygame.K_DOWN] and yellow_y + velocity < HEIGHT:  # moving down
        yellow_y += velocity


def handle_bullets(yellow_bullets, red_bullets):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY

    # Remove bullets that go off-screen
    yellow_bullets = [bullet for bullet in yellow_bullets if bullet.x < WIDTH]
    red_bullets = [bullet for bullet in red_bullets if bullet.x > 0]

    return yellow_bullets, red_bullets


def main():
    global red_x, yellow_x, red_y, yellow_y

    YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE = define_ships('spaceship_yellow', 'spaceship_red')

    # Swap initial positions of yellow and red spaceships
    yellow_x, yellow_y = 700, 300
    red_x, red_y = 100, 300

    crash_sound = load_sound('explosion')
    yellow_bullets = []
    red_bullets = []
    num_bullets = 5

    play_game = True
    clock = pygame.time.Clock()

    while play_game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False

            if event.type == pygame.KEYDOWN:
                bullet = pygame.Rect(yellow_x + YELLOW_SPACESHIP_IMAGE.get_width(), yellow_y + YELLOW_SPACESHIP_IMAGE.get_height() / 2 - 2, 10, 5)
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < num_bullets:
                    yellow_bullets.append(bullet)

                bullet = pygame.Rect(red_x - 10, red_y + RED_SPACESHIP_IMAGE.get_height() / 2 - 2, 10, 5)  # Adjusted position for the red spaceship's bullet
                if event.key == pygame.K_RCTRL and len(red_bullets) < num_bullets:
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_spaceship_movement(keys_pressed)
        handle_red_spaceship_movement(keys_pressed)

        yellow_bullets, red_bullets = handle_bullets(yellow_bullets, red_bullets)
        drawings(YELLOW_SPACESHIP_IMAGE, RED_SPACESHIP_IMAGE, yellow_bullets, red_bullets)


if __name__ == "__main__":
    main()