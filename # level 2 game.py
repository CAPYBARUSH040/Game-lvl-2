import pygame

# Game is save the sisters puzzle
# Author: Thomas Thornley
# Date: 24/07/2024
# Version 1

# Initialize Pygame
pygame.init()

# Define the screen size
SCREEN_WIDTH = 1316
SCREEN_HEIGHT = 740

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Level 2 - Save the Sisters!")

# Set up the player square
x = 50  # Starting position
y = SCREEN_HEIGHT - 60  # Start near the bottom
player_size = 50  # Size of the player
vel = 10   # Player movement speed

# Gravity and jumping mechanics
gravity = 0.5
jump_strength = 10
is_jumping = False
vertical_velocity = 0

# Create a list of platforms
platforms = [
    pygame.Rect(100, 600, 200, 20),   # Platform 1
    pygame.Rect(350, 500, 200, 20),   # Platform 2
    pygame.Rect(600, 400, 200, 20),   # Platform 3
    pygame.Rect(850, 300, 200, 20),   # Platform 4
    pygame.Rect(400, 200, 200, 20),   # Platform 5
    pygame.Rect(700, 150, 200, 20),   # Platform 6
    pygame.Rect(1000, 100, 200, 20),  # Platform 7
]

# Create a clock to control the frame rate
clock = pygame.time.Clock()
FPS = 60

# Function to draw the player
def draw_player(surface, x, y, size):
    pygame.draw.rect(surface, (255, 0, 0), (x, y, size, size))

# Main game loop
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Player movement based on key presses (WASD and Arrow Keys)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if not is_jumping:
            is_jumping = True
            vertical_velocity = -jump_strength

    # Handle jumps and gravity
    if is_jumping:
        vertical_velocity += gravity
        y += vertical_velocity

    # Edge cases for player position (Keep player within screen bounds)
    if x < 0:
        x = 0
    elif x > SCREEN_WIDTH - player_size:
        x = SCREEN_WIDTH - player_size

    # Check collision with platforms and apply gravity
    on_platform = False 
    for platform in platforms:
        if pygame.Rect(x, y + vertical_velocity, player_size, player_size).colliderect(platform):
            if vertical_velocity >= 0:  # Player is falling down 
                y = platform.top - player_size  # Place player on top of the platform
                vertical_velocity = 0  # Reset vertical velocity since we've landed
                is_jumping = False
                on_platform = True
                break

    # Apply gravity if not on any platform
    if not on_platform:
        y += vertical_velocity

    # Prevent player from falling below the ground
    if y >= SCREEN_HEIGHT - player_size:
        y = SCREEN_HEIGHT - player_size
        is_jumping = False
        vertical_velocity = 0  # Reset vertical velocity when hitting the bottom

    # Draw the player
    draw_player(screen, x, y, player_size)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, (0, 0, 0), platform)  # Drawing black platforms

    # Update the display with the latest changes
    pygame.display.update()

# Quit the game cleanly when done
pygame.quit()