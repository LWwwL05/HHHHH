import pygame
import sys
from settings import *
from level import Level
from player import Player


class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        
        self.button_image = pygame.image.load('img/button.png').convert_alpha()
        self.button_rect = self.button_image.get_rect(center=(WIDTH // 2, HEIGTH // 2))

        
        self.font = pygame.font.Font(None, 100)

        
        self.is_playing = False

       
        self.current_screen = 0
        self.screens = [
            {'image': pygame.image.load('img/open.png').convert_alpha(),
             'text': 'Click screen',
             },  
            {'image': pygame.image.load('img/second.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/third.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/four.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/five.png').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/victory_screen1.jpg').convert_alpha(),
             'text': ''},
            {'image': pygame.image.load('img/victory_screen2.png').convert_alpha(),
             'text': ''}
        ]
        self.victory_images = [
            {'image': pygame.image.load('img/victory_screen1.jpg').convert_alpha(),
             'text': ''}
    ]
        self.end_images = [
            {'image': pygame.image.load('img/end_screen1.jpg').convert_alpha(),
             'text': ''}
    ]
        self.current_victory_image = 0 
        self.current_end_image = 0 

        
        


    def run(self):
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Move to the next screen on click
                    self.current_screen += 1
                    if self.current_screen == len(self.screens) - 2:
                        # Start the game when reaching the last screen
                        self.is_playing = True
                        self.current_screen += 1

            self.screen.fill(WATER_COLOR)
            raccoon_count_result = self.level.check_raccoon_count()
            if self.current_screen < len(self.screens):
                background_image = self.screens[self.current_screen]['image']
                background_rect = background_image.get_rect()
                self.screen.blit(background_image, background_rect)

            if raccoon_count_result == 0:
                self.is_playing = False
                victory_image = self.victory_images[self.current_victory_image]['image']
                self.screen.blit(victory_image, (0, 0))

            if self.is_playing:
                self.level.run()
            else:
                background_image = self.screens[self.current_screen]['image']
                background_rect = background_image.get_rect()
                self.screen.blit(background_image, background_rect)

                
                if self.screens[self.current_screen].get('button', False) :
                    self.screen.blit(self.button_image, self.button_rect)

                
                text = self.font.render(self.screens[self.current_screen]['text'], True, (255, 255, 255))
                self.screen.blit(text, (WIDTH // 2 - 200, HEIGTH // 2 + 50))

            pygame.display.update()
            self.clock.tick(FPS)
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

if __name__ == '__main__':
    game = Game()
    game.run()
