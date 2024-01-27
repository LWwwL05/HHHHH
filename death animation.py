import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Death Animation")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Character parameters
character_size = 50
character_x = width // 2 - character_size // 2
character_y = height // 2 - character_size // 2
character_color = white

# Death animation parameters
death_animation_active = False
death_animation_frames = 60  # Number of frames for death animation
frame_count = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Trigger death animation on key press (for demonstration purposes)
        if event.type == pygame.KEYDOWN and not death_animation_active:
            death_animation_active = True

    # Update logic
    if death_animation_active:
        if frame_count < death_animation_frames:
            # Animate the character (shrink and fade away)
            character_size -= 1
            character_color = (255, 255, 255, int(255 - frame_count * (255 / death_animation_frames)))
            frame_count += 1
        else:
            # Reset after the death animation is complete
            death_animation_active = False
            frame_count = 0
            character_size = 50
            character_color = white

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, character_color, (character_x, character_y, character_size, character_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
